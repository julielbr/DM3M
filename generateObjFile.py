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
    diameter_pole = int(input("Enter the diameter of the pole: "))

    # BASE OF THE LAMP
    # Generating vertices for the base and top of the lamp base
    base_vertices_lamp_base = [
        (-side_length/2, -side_length/2, 0),
        (side_length/2, -side_length/2, 0),
        (-side_length/2, side_length/2, 0),
        (side_length/2, side_length/2, 0)
    ]
    top_vertices_lamp_base = [
        (-side_length/2, -side_length/2, height_base),
        (side_length/2, -side_length/2, height_base),
        (-side_length/2, side_length/2, height_base),
        (side_length/2, side_length/2, height_base)
    ]
    vertices_lamp_base = base_vertices_lamp_base + top_vertices_lamp_base

    # Generating faces for the lamp base
    base_faces_lamp_base = [
        (0, 1, 3, 2),   
        (4, 6, 7, 5),   
        (0, 4, 5, 1),   
        (1, 5, 7, 3),
        (3, 7, 6, 2),
        (2, 6, 4, 0)
    ]

    # POLE OF THE LAMP
    # Calculate half the diameter for centering the pole
    half_diameter = diameter_pole / 2

    
    base_vertices_lamp_pole = [
        (-half_diameter, -half_diameter, height_base),
        (half_diameter, -half_diameter, height_base),
        (-half_diameter, half_diameter, height_base),
        (half_diameter, half_diameter, height_base)
    ]
    top_vertices_lamp_pole = [
        (-half_diameter, -half_diameter, height_base + height_pole),
        (half_diameter, -half_diameter, height_base + height_pole),
        (-half_diameter, half_diameter, height_base + height_pole),
        (half_diameter, half_diameter, height_base + height_pole)
    ]
    vertices_lamp_pole = base_vertices_lamp_pole + top_vertices_lamp_pole

    # Generating faces for the lamp pole
    base_faces_lamp_pole = [
        (8, 9, 11, 10),   
        (12, 14, 15, 13),   
        (8, 12, 13, 9),   
        (9, 13, 15, 11),
        (11, 15, 14, 10),
        (10, 14, 12, 8)
    ]

    vertices = vertices_lamp_base + vertices_lamp_pole
    faces = base_faces_lamp_base + base_faces_lamp_pole

    # Write to OBJ file
    write_obj_file(vertices, faces, "lamp.obj")
create_lamp()
