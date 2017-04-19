import os.path
import itertools
from .mesh import Mesh
from .face import Face
from .metric import Metric
import pdb


def read_obj(file, verbose, order):
    vertices = []
    faces = []
    is_zero_vn = False
    for line in file:
        instructions = line.rstrip().split()
        if len(instructions) > 0:
            if instructions[0] == "v" and is_zero_vn is False:
                vertices.append(_create_vertex(instructions, order))
            elif instructions[0] == "f":
                faces.append(_create_face(instructions, vertices))
            elif instructions[0] == "vn":
                if (float(instructions[1]) == 0.0):
                    is_zero_vn = True
                else:
                    is_zero_vn = False
            else:
                pass

    mesh = Mesh(faces)
    if verbose is True:
        print("Vertices: " + str(len(vertices)) + ", Faces: " + str(len(faces)))

    return mesh


def _create_vertex(instructions, order):
    return order.get_vertex(float(instructions[1]),
                            float(instructions[2]),
                            float(instructions[3]))


def _create_face(instructions, vertices):
    """Create a face using the instructions (removes 1 for the index)"""
    vertex1_index = instructions[1].split("//")[0]
    vertex2_index = instructions[2].split("//")[0]
    vertex3_index = instructions[3].split("//")[0]
    face_recipe = (int(vertex1_index), int(vertex2_index), int(vertex3_index))
    face = Face(vertices[face_recipe[0] - 1], vertices[face_recipe[1] - 1], vertices[face_recipe[2] - 1])
    return face


def write_csv(args, meshes):
    # Strip extensions off filenames
    csv_file = args.out
    files = args.meshes
    quadrat_size = args.size
    mesh_names = list(map(lambda x: x.name.split('.')[0], files))

    # Write csv headers
    csv_file.write("mesh_name," +
                   "quadrat_size_m," +
                   "quadrat_rel_x," +
                   "quadrat_rel_y," +
                   "quadrat_rel_z_mean," +
                   "quadrat_rel_z_sd," +
                   "quadrat_abs_x," +
                   "quadrat_abs_y," +
                   "quadrat_abs_z," +
                   "num_faces," +
                   "num_vertices," +
                   "3d_surface_area," +
                   "2d_surface_area," +
                   "surface_rugosity," +
                   "faces\n")

    for index, mesh in enumerate(meshes):
        for metric in mesh:
            if metric.area3d > 0 and metric.area2d > 0:
                csv_file.write(mesh_names[index].split("/")[-1])
                csv_file.write(",")
                csv_file.write(str(args.size))
                csv_file.write(",")
                csv_file.write(str(metric.quadrat_id[0]))
                csv_file.write(",")
                csv_file.write(str(metric.quadrat_id[1]))
                csv_file.write(",")
                csv_file.write(str(metric.relative_z_mean))
                csv_file.write(",")
                csv_file.write(str(metric.relative_z_sd))
                csv_file.write(",")
                csv_file.write(str(metric.quadrat_midpoint.x))
                csv_file.write(",")
                csv_file.write(str(metric.quadrat_midpoint.y))
                csv_file.write(",")
                csv_file.write(str(metric.quadrat_midpoint.z))
                csv_file.write(",")
                csv_file.write(str(metric.face_count))
                csv_file.write(",")
                csv_file.write(str(metric.vertices_count))
                csv_file.write(",")
                csv_file.write(str(metric.area3d))
                csv_file.write(",")
                csv_file.write(str(metric.area2d))
                csv_file.write(",")
                csv_file.write(str(metric.surface_rugosity()))
                csv_file.write("\n")
    csv_file.close()
