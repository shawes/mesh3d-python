from shapes.mesh import Mesh
from shapes.face import Face


class ObjReader(object):

    vertices = list()
    faces = list()

    def __init__(self, verbose, order):
        self.verbose = verbose
        self.order = order

    def _get_index(pos, instructions):
        return int(instructions[pos].split('/')[0]) - 1

    def _create_vertex(self, instructions):
        return self.order.get_vertex(float(instructions[1]),
                                     float(instructions[2]),
                                     float(instructions[3]))

    def _create_face(self, instructions):
        """Create a face using the instructions."""
        return Face(self.vertices(self._get_index(0, instructions)),
                    self.vertices(self._get_index(0, instructions)),
                    self.vertices(self._get_index(0, instructions)))

    def read(self, file):
        file = open(file)
        self.vertices = list()
        self.face = list()
        is_zero_vn = False
        for line in file:
            instructions = line.split(" ")
            if instructions.len() > 0:
                if list[0] == "v":
                    if is_zero_vn is False:
                        self.vertices.append(self._create_vertex(instructions))
                elif list[0] == "vn":
                    if float(instructions(1)) == 0.0:
                        is_zero_vn = True
                    else:
                        is_zero_vn = False
                else:
                    self.faces.append(self._create_face(instructions))
        if self.verbose:
            print("Vertices: " + self.vertices.len() +
                  ", Faces: " + self.faces.len())
        return Mesh(self.vertices, self.faces)
