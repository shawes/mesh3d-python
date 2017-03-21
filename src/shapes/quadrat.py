from quadrilateral import Quadrilateral
from vertex import Vertex


class Quadrat(Quadrilateral):

    relative_z_avg = 0.0
    relative_z_std = 0.0

    def __init__(self, id, size, midpoint):
        Quadrilateral.__init__(self,
            Vertex(midpoint.x - size / 2, midpoint.y - size / 2, midpoint.z),
            Vertex(midpoint.x - size / 2, midpoint.y + size / 2, midpoint.z),
            Vertex(midpoint.x + size / 2, midpoint.y - size / 2, midpoint.z),
            Vertex(midpoint.x + size / 2, midpoint.y + size / 2, midpoint.z))
        self.id = id
        self.midpoint = midpoint

    def contains(self, vertex):
        x_test = vertex.x > self.vertex_1.x and vertex.x < self.vertex_4.x
        y_test = vertex.y > self.vertex_1.y and vertex.y < self.vertex_2.y
        return x_test and y_test

    def __eq__(self, other):
        return isinstance(other, Quadrat) and
        self.midpoint == other.midpoint and
        self.id == other.id

    def __hash__(self):
        return hash((tuple(self.id), tuple(self.midpoint)))
