import math

def write_obj_file(vertices, faces, file_path):
    with open(file_path, 'w') as f:
        for vertex in vertices:
            f.write(f"v {vertex[0]} {vertex[1]} {vertex[2]}\n")
        
        for face in faces:
            f.write("f")
            for vertex_index in face:
                f.write(f" {vertex_index + 1}")
            f.write("\n")

def calculate_circle_vertices(radius, y_height, num_segments=32):
    """Calculate the vertices around a circle at a given y height."""
    vertices = []
    for i in range(num_segments):
        theta = 2.0 * math.pi * i / num_segments
        x = radius * math.cos(theta)
        z = radius * math.sin(theta)
        vertices.append((x, y_height, z))
    return vertices

def calculate_cylinder_faces(num_segments, bottom_index, top_index):
    """Calculate the side faces of a cylinder."""
    faces = []
    for i in range(num_segments):
        next_i = (i + 1) % num_segments
        faces.append((bottom_index + i, bottom_index + next_i, top_index + next_i))
        faces.append((top_index + next_i, top_index + i, bottom_index + i))
    return faces

def calculate_rectangle_vertices(length, depth, y_height):
    """Calculate the vertices of a rectangle at a given y height."""
    half_length = length / 2
    half_depth = depth / 2
    return [
        (-half_length, y_height, -half_depth),
        (half_length, y_height, -half_depth),
        (half_length, y_height, half_depth),
        (-half_length, y_height, half_depth)
    ]

def calculate_triangular_faces(start_index):
    """Calculate triangular faces for a rectangular prism."""
    top = start_index + 4
    faces = [
        (start_index, start_index+1, top+1), (start_index, top+1, top),   
        (start_index+1, start_index+2, top+2), (start_index+1, top+2, top+1),   
        (start_index+2, start_index+3, top+3), (start_index+2, top+3, top+2),   
        (start_index+3, start_index, top), (start_index+3, top, top+3), 
        (start_index, start_index+1, start_index+2), (start_index, start_index+2, start_index+3),   
        (top, top+1, top+2), (top, top+2, top+3)   
    ]
    return faces

def create_lamp():
    length_base = float(input("Enter the radius of the lamp base (interpreted as length): "))
    h_base = float(input("Enter the height of the base: "))
    width_base = length_base * 0.5  
    length_pole = float(input("Enter the diameter of the pole (interpreted as length): "))
    h_pole = float(input("Enter the height of the lamp pole: "))
    depth_pole = length_pole * 0.5 
    r_screentop = float(input("Enter the top radius of the lamp screen: "))
    r_screenbottom = float(input("Enter the bottom radius of the lamp screen: "))
    h_screen = float(input("Enter the height of the lamp screen: "))

    # Base
    base_bottom_vertices = calculate_rectangle_vertices(length_base, width_base, 0)
    base_top_vertices = calculate_rectangle_vertices(length_base, width_base, h_base)
    base_faces = calculate_triangular_faces(0)
    
    # Pole
    pole_bottom_vertices = calculate_rectangle_vertices(length_pole, depth_pole, h_base)
    pole_top_vertices = calculate_rectangle_vertices(length_pole, depth_pole, h_base + h_pole)
    pole_faces = calculate_triangular_faces(8)
    

    num_segments = 32
    screen_bottom_vertices = calculate_circle_vertices(r_screenbottom, h_base + h_pole, num_segments)
    screen_top_vertices = calculate_circle_vertices(r_screentop, h_base + h_pole + h_screen, num_segments)
    screen_faces = calculate_cylinder_faces(num_segments, 16, 16 + num_segments)
    
    # Combine all vertices and faces
    vertices = base_bottom_vertices + base_top_vertices + pole_bottom_vertices + pole_top_vertices + screen_bottom_vertices + screen_top_vertices
    faces = base_faces + pole_faces + screen_faces
    
    # Write to OBJ file
    write_obj_file(vertices, faces, "lamp.obj")
    
# Call the function to create the lamp and write it to an OBJ file
create_lamp()
