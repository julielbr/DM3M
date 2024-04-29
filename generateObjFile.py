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

# BASE OF THE LAMP
    # LAMP BASE: Generate the vertices for the base of the base of the 
    base_vertices_lamp_base = [
        (-side_length/2, -side_length/2, 0),
        (side_length/2, -side_length/2, 0),
        (-side_length/2, side_length/2, 0),
        (side_length/2, side_length/2, 0)
    ]
    # LAMP BASE: Generate the vertices for the top
    top_vertices_lamp_base = [
        (-side_length/2, -side_length/2, height_base),
        (side_length/2, -side_length/2, height_base),
        (-side_length/2, side_length/2, height_base),
        (side_length/2, side_length/2, height_base)
    ]
    # LAMP BASE: Combine the vertices
    vertices_lamp_base = base_vertices_lamp_base + top_vertices_lamp_base
    # LAMP BASE: Generate the faces for the base
    base_faces_lamp_base = [
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
    # LAMP BASE: Generate the faces for the top
    top_faces_lamp_base = [
        (8, 9, 11),
        (8, 11, 10)
    ]
    # LAMP BASE: Combine the faces
    faces_lamp_base = base_faces_lamp_base + top_faces_lamp_base

# POLE OF THE LAMP

# LAMP POLE: Generate the vertices for the base of the base of the 
    base_vertices_lamp_pole = [
        (-2, -2, height_base),
        (2, -2, height_base),
        (-2, 2, height_base),
        (2, 2, height_base)
    ]
    # LAMP POLE: Generate the vertices for the top
    top_vertices_lamp_pole = [
        (-2, -2, height_base+height_pole),
        (2, -2, height_base+height_pole),
        (-2, 2, height_base+height_pole),
        (2, 2, height_base+height_pole)
    ]
    # LAMP POLE: Combine the vertices
    vertices_lamp_pole = base_vertices_lamp_pole + top_vertices_lamp_pole
    # LAMP POLE: Generate the faces for the base
    base_faces_lamp_pole = [
    ]
    # LAMP POLE: Generate the faces for the top
    top_faces_lamp_pole = [
    ]
    # LAMP POLE: Combine the faces
    faces_lamp_pole = base_faces_lamp_pole + top_faces_lamp_pole

    # Write to OBJ file
    write_obj_file(vertices, faces, "lamp.obj")

# Call the function to create the lamp and write it to an OBJ file
create_lamp()