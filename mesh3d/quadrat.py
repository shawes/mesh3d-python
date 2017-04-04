from quadrilateral import Quadrilateral
from vertex import Vertex
from metric import Metric


class Quadrat(Quadrilateral):

    def __init__(self, id, size, midpoint):
        self.id = id
        self.size = size
        self.midpoint = midpoint
        ##self.metric = Metric()
        self.vertices_inside = list()
        Quadrilateral.__init__(self,
            Vertex(midpoint.x - (size / 2), midpoint.y - (size / 2), midpoint.z),
            Vertex(midpoint.x + (size / 2), midpoint.y - (size / 2), midpoint.z),
            Vertex(midpoint.x + (size / 2), midpoint.y + (size / 2), midpoint.z),
            Vertex(midpoint.x - (size / 2), midpoint.y + (size / 2), midpoint.z))

    def contains(self, vertex):
        if self._within(vertex) is True:
            return True
        elif self._bump(vertex) is True:
            return True
        else:
            return False

    def _within(self, vertex):
        inside_x = vertex.x > self.vertex_1.x and vertex.x < self.vertex_2.x
        inside_y = vertex.y > self.vertex_1.y and vertex.y < self.vertex_4.y
        inside = inside_x and inside_y
        return inside

    def _bump(self, vertex):
        _bump_amount = 0.00001
        vertex_bumped = Vertex(vertex.x + _bump_amount,
                               vertex.y + _bump_amount,
                               0)
        return self._within(vertex)

    def area(self):
        return size*size

    def __eq__(self, other):
        return self.midpoint == other.midpoint and self.id == other.id

    def __hash__(self):
        return hash(self.id)
