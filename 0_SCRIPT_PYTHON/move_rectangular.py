#!/usr/bin/env python3



import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class RectangularPath(Node):
    def __init__(self):
        super().__init__('rectangular_path')
        # Pubblicazione sul topic cmd_vel_2
        self.cmd_vel_publisher = self.create_publisher(Twist, 'cmd_vel_2', 10)
        
        # Delay per assicurarsi che il publisher sia attivo
        time.sleep(1)
        
        # Parametri del movimento
        self.linear_speed = 0.5 # Velocità lineare in m/s
        self.angular_speed = 0.8  # Velocità angolare in rad/s
        self.side_lengths = [2.0, 2.0]  # Lunghezza dei lati del rettangolo (metri)

    def move_forward(self, distance):
        """Muove il robot avanti di una distanza specifica."""
        twist = Twist()
        twist.linear.x = self.linear_speed
        time_duration = distance / self.linear_speed
        self.publish_for_duration(twist, time_duration)

    def turn_90_degrees(self):
        """Ruota il robot di 90 gradi a destra."""
        twist = Twist()
        twist.angular.z = -self.angular_speed  # Rotazione a destra
        time_duration = 1.57 / self.angular_speed  # 90 gradi in rad = π/2 rad ≈ 1.57
        self.publish_for_duration(twist, time_duration)

    def publish_for_duration(self, twist, duration):
        """Pubblica un messaggio Twist per una durata specifica."""
        end_time = time.time() + duration
        while time.time() < end_time:
            self.cmd_vel_publisher.publish(twist)
            time.sleep(0.1)  # Pubblica ogni 100 ms
        # Ferma il movimento
        self.cmd_vel_publisher.publish(Twist())  # Invia un Twist vuoto per fermare il robot
        time.sleep(1)  # Pausa di 1 secondo prima di continuare

    def run_path(self):
        """Esegue la traiettoria rettangolare."""
        for _ in range(2):  # Due lati per ogni lato del rettangolo
            self.move_forward(self.side_lengths[0])  # Lato lungo (2 metri)
            self.turn_90_degrees()
            self.move_forward(self.side_lengths[1])  # Lato corto (1 metro)
            self.turn_90_degrees()

def main(args=None):
    rclpy.init(args=args)
    rectangular_path_node = RectangularPath()
    
    try:
        # Esegui continuamente il percorso rettangolare
        while rclpy.ok():
            rectangular_path_node.run_path()  # Ripete continuamente la traiettoria
    except KeyboardInterrupt:
        pass  # Permette di fermare lo script con Ctrl+C

    # Distruggi il nodo quando lo script viene interrotto
    rectangular_path_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
