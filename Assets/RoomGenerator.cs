using UnityEngine;

[ExecuteInEditMode] // Consente l'esecuzione dello script anche in Edit Mode
public class RoomGenerator : MonoBehaviour
{
    public float width = 10f;
    public float height = 10f;
    public float wallHeight = 3f;
    
    public Material wallMaterial;
    public Material floorMaterial;

    // Metodo per rigenerare la stanza
    private void OnValidate()
    {
        ClearRoom();  // Elimina la stanza corrente
        GenerateRoom(); // Genera la stanza con i nuovi parametri
    }

    // Metodo per generare la stanza
    void GenerateRoom()
    {
        // Pavimento
        GameObject floor = GameObject.CreatePrimitive(PrimitiveType.Cube);
        floor.transform.localScale = new Vector3(width, 0.1f, height);
        floor.transform.position = new Vector3(0, 0, 0);
        floor.name = "Floor";
        // floor.GetComponent<Renderer>().material = floorMaterial;

        // // Soffitto
        // GameObject ceiling = GameObject.CreatePrimitive(PrimitiveType.Cube);
        // ceiling.transform.localScale = new Vector3(width, 0.1f, height);
        // ceiling.transform.position = new Vector3(0, wallHeight, 0);
        // ceiling.name = "Ceiling";
        // ceiling.GetComponent<Renderer>().material = wallMaterial;

        // Pareti
        CreateWall(new Vector3(0, wallHeight / 2, height / 2), new Vector3(width, wallHeight, 0.1f), "Wall1");
        CreateWall(new Vector3(0, wallHeight / 2, -height / 2), new Vector3(width, wallHeight, 0.1f), "Wall2");
        CreateWall(new Vector3(width / 2, wallHeight / 2, 0), new Vector3(0.1f, wallHeight, height), "Wall3");
        CreateWall(new Vector3(-width / 2, wallHeight / 2, 0), new Vector3(0.1f, wallHeight, height), "Wall4");
    }

    void CreateWall(Vector3 position, Vector3 scale, string name)
    {
        GameObject wall = GameObject.CreatePrimitive(PrimitiveType.Cube);
        wall.transform.localScale = scale;
        wall.transform.position = position;
        wall.name = name;
        // wall.GetComponent<Renderer>().material = wallMaterial;
    }

    // Metodo per eliminare la stanza corrente (oggetti figli)
    void ClearRoom()
    {
        for (int i = transform.childCount - 1; i >= 0; i--)
        {
            DestroyImmediate(transform.GetChild(i).gameObject);
        }
    }
}
