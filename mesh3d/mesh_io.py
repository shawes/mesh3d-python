import os.path
import itertools
from mesh import Mesh
from face import Face
import metrics
import pdb


def read_obj(file, verbose, order):
    vertices = list()
    faces = list()
    is_zero_vn = False
    for line in file:
        instructions = line.rstrip().split()
        if len(instructions) > 0:
            if instructions[0] == "v":
                #    if is_zero_vn is False:
                # print(instructions)
                vertices.append(_create_vertex(instructions, order))
            # elif instructions[0] == "vn":
            #     if float(instructions[1]) == 0.0:
            #         is_zero_vn = True
            #     else:
            #         is_zero_vn = False
            elif instructions[0] == "f":
                faces.append(_create_face(instructions, vertices))
            else:
                pass
    if verbose is True:
        print("Vertices: " + str(len(vertices)) + ", Faces: " + str(len(faces)))
    return Mesh(vertices, faces)


def _create_vertex(instructions, order):
    return order.get_vertex(float(instructions[1]),
                            float(instructions[2]),
                            float(instructions[3]))

def _create_face(instructions, vertices):
    """Create a face using the instructions."""
    v1 = instructions[1]
    v2 = instructions[2]
    v3 = instructions[3]
    face = Face(vertices[int(v1[0]) - 1],
                vertices[int(v2[0]) - 1], vertices[int(v3[0]) - 1])
    return face

def write_csv(args, quadrats, areas):
    # Strip extensions off filenames
    csv_file = args.out
    files = args.meshes
    quadrat_size = args.size
    names = list(map(lambda x: x.name.split('.')[0], files))

    # write csv headers
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
                   "surface_rugosity\n")

    area_index = 0
    for name in names:
        # print(name)
        for quadrat in quadrats:
            area_info = areas[area_index]
            area3d = area_info[0]
            area2d = area_info[1]
            faces = area_info[2]
            vertices = area_info[3]
            rugosity = metrics.rugosity(area3d,area2d)
            if area3d > 0 and area2d > 0:
                csv_file.write(name)
                csv_file.write(",")
                csv_file.write(str(args.size))
                csv_file.write(",")
                csv_file.write(str(quadrat.id[0]))
                csv_file.write(",")
                csv_file.write(str(quadrat.id[1]))
                csv_file.write(",")
                csv_file.write(str(quadrat.relative_z_mean))
                csv_file.write(",")
                csv_file.write(str(quadrat.relative_z_sd))
                csv_file.write(",")
                csv_file.write(str(quadrat.midpoint.x))
                csv_file.write(",")
                csv_file.write(str(quadrat.midpoint.y))
                csv_file.write(",")
                csv_file.write(str(quadrat.midpoint.z))
                csv_file.write(",")
                csv_file.write(str(faces))
                csv_file.write(",")
                csv_file.write(str(vertices))
                csv_file.write(",")
                csv_file.write(str(area3d))
                csv_file.write(",")
                csv_file.write(str(area2d))
                csv_file.write(",")
                csv_file.write(str(rugosity))
                csv_file.write("\n")

            area_index += 1
            #size_index += 1
    csv_file.close()
