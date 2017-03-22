from shapes.mesh import Mesh
from shapes.face import Face


class ObjReader(object):

    vertices = list()
    faces = list()

    def __init__(self, verbose, order):
        self.verbose = verbose
        self.order = order

    def _create_vertex(self, instructions):
        return self.order.get_vertex(float(instructions[1]),
                                     float(instructions[2]),
                                     float(instructions[3]))

    def _create_face(self, instructions):
        """Create a face using the instructions."""
        v1 = instructions[1].split("/")
        v2 = instructions[1].split("/")
        v3 = instructions[1].split("/")
        return Face(self.vertices[int(v1[0]) - 1], self.vertices[int(v2[0]) - 1], self.vertices[int(v3[0]) - 1])

    def read(self, file):

        self.vertices = list()
        self.faces = list()
        is_zero_vn = False

        for line in file:
            instructions = line.split(" ")
            if len(instructions) > 0:
                if instructions[0] == "v":
                #    if is_zero_vn is False:
                        self.vertices.append(self._create_vertex(instructions))
                # elif instructions[0] == "vn":
                #     if float(instructions[1]) == 0.0:
                #         is_zero_vn = True
                #     else:
                #         is_zero_vn = False
                elif instructions[0] == "f":
                    self.faces.append(self._create_face(instructions))
                else:
                    pass

        if self.verbose:
            print("Vertices: " + len(self.vertices).__str__() + ", Faces: " + len(self.faces).__str__())
        return Mesh(self.vertices, self.faces)
