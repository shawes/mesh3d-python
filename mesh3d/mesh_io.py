import os.path
import itertools
from mesh import Mesh
from face import Face
import numpy
import metrics
import pdb


def read_obj(file, verbose, order):
    vertices = []
    faces_instructions = []
    is_zero_vn = False
    for line in file:
        instructions = line.rstrip().split()
        if len(instructions) > 0:
            if instructions[0] == "v" and is_zero_vn is False:
                vertices.append(_create_vertex(instructions, order))
            elif instructions[0] == "f":
                #pdb.set_trace()
                faces_instructions.append(_create_face(instructions))
            elif instructions[0] == "vn":
                if (float(instructions[1]) == 0.0):
                    is_zero_vn = True
                else:
                    is_zero_vn = False
            else:
                pass

    faces = list()
    for face_recipe in faces_instructions:
        faces.append(Face(vertices[(face_recipe[0])],
                    vertices[(face_recipe[1])], vertices[face_recipe[2]]))

    mesh = Mesh(numpy.asarray(vertices), numpy.asarray(faces))
    if verbose is True:
        print("Vertices: " + str(mesh.vertices.size) + ", Faces: " + str(mesh.faces.size))
    #vertices_array = numpy.asarray(vertices)
    #faces_array = numpy.asarray(faces)
    return mesh


def _create_vertex(instructions, order):
    return order.get_vertex(float(instructions[1]),
                            float(instructions[2]),
                            float(instructions[3]))

def _create_face(instructions):
    """Create a face using the instructions (removes 1 for the index)"""
    #pdb.set_trace()
    return (int(instructions[1][0])-1,int(instructions[2][0])-1,int(instructions[3][0])-1)

    # #pdb.set_trace()
    # return face

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
            pdb.set_trace()
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
