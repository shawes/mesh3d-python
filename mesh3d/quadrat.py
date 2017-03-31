from quadrilateral import Quadrilateral
from vertex import Vertex


class Quadrat(Quadrilateral):

    def __init__(self, id, size, midpoint):
        self.id = id
        self.size = size
        self.midpoint = midpoint
        self.relative_z_mean = 0.0
        self.relative_z_sd = 0.0
        Quadrilateral.__init__(self,
            Vertex((midpoint.x - size) / 2, (midpoint.y - size) / 2, midpoint.z),
            Vertex((midpoint.x + size) / 2, (midpoint.y - size) / 2, midpoint.z),
            Vertex((midpoint.x + size) / 2, (midpoint.y + size) / 2, midpoint.z),
            Vertex((midpoint.x - size) / 2, (midpoint.y + size) / 2, midpoint.z))

    def contains(self, face):
        vertex = face.centroid
        inside_x = vertex.x >= self.vertex_1.x and vertex.x <= self.vertex_2.x
        inside_y = vertex.y >= self.vertex_1.y and vertex.y <= self.vertex_4.y
        inside = inside_x and inside_y
        return inside

    def area(self):
        return size*size

    def __eq__(self, other):
        return self.midpoint == other.midpoint and self.id == other.id

    def __hash__(self):
        return hash(self.id) * hash(self.size) * hash(self.midpoint)
