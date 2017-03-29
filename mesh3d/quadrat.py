from shapes.quadrilateral import Quadrilateral
from shapes.vertex import Vertex


class Quadrat(Quadrilateral):

    relative_z_avg = 0.0
    relative_z_std = 0.0

    def __init__(self, id, size, midpoint):
        self.id = id
        self.size = size
        self.midpoint = midpoint
        Quadrilateral.__init__(self,
            Vertex((midpoint.x - size) / 2, (midpoint.y - size) / 2, midpoint.z),
            Vertex((midpoint.x - size) / 2, (midpoint.y + size) / 2, midpoint.z),
            Vertex((midpoint.x + size) / 2, (midpoint.y - size) / 2, midpoint.z),
            Vertex((midpoint.x + size) / 2, (midpoint.y + size) / 2, midpoint.z))

    def contains(self, vertex):
        x_test = vertex.x > self.vertex_1.x and vertex.x < self.vertex_4.x
        y_test = vertex.y > self.vertex_1.y and vertex.y < self.vertex_2.y
        return x_test and y_test

    def area(self):
        return size*size

    def __eq__(self, other):
        return self.midpoint == other.midpoint and self.id == other.id

    def __hash__(self):
        return hash(self.id) * hash(self.size) * hash(self.midpoint)
