def write_obj_file(vertices, faces, file_path):
    with open(file_path, 'w') as f:
        for vertex in vertices:
            f.write(f"v {vertex[0]} {vertex[1]} {vertex[2]}\n")
        
        for face in faces:
            f.write("f")
            for vertex_index in face:
                f.write(f" {vertex_index + 1}")
            f.write("\n")

def create_lamp():
    side_length = int(input("Enter the width of the lamp (side length): "))
    height_pole = int(input("Enter the height of the lamp: "))
    height_base = int(input("Enter the height of the base: "))

    # BASE OF THE LAMP: Generate the vertices for the base of the base of the 
    base_vertices = [
        (-side_length/2, -side_length/2, 0),
        (side_length/2, -side_length/2, 0),
        (-side_length/2, side_length/2, 0),
        (side_length/2, side_length/2, 0)
    ]
    
    # BASE OF THE LAMP: Generate the vertices for the top
    top_vertices = [
        (-side_length/2, -side_length/2, height_base),
        (side_length/2, -side_length/2, height_base),
        (-side_length/2, side_length/2, height_base),
        (side_length/2, side_length/2, height_base)
    ]

    # BASE OF THE LAMP: Combine the vertices
    vertices = base_vertices + top_vertices

    # BASE OF THE LAMP: Generate the faces for the base
    base_faces = [
        (0, 1, 3),
        (0, 3, 2),
        (0, 1, 5),
        (0, 5, 4),
        (1, 3, 7),
        (1, 7, 5),
        (2, 3, 7),
        (2, 7, 6),
        (0, 2, 6),
        (0, 6, 4),
        (4, 5, 7),
        (4, 7, 6)
    ]

    # BASE OF THE LAMP: Generate the faces for the top
    top_faces = [
        (8, 9, 11),
        (8, 11, 10)
    ]

    # BASE OF THE LAMP: Combine the faces
    faces = base_faces + top_faces

    # Write to OBJ file
    write_obj_file(vertices, faces, "lamp.obj")

# Call the function to create the lamp and write it to an OBJ file
create_lamp()