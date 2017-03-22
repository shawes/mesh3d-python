import math
from line import Line


class Quadrilateral(object):

    def __init__(self, vertex_1, vertex_2, vertex_3, vertex_4):
        self.vertex_1 = vertex_1
        self.vertex_2 = vertex_2
        self.vertex_3 = vertex_3
        self.vertex_4 = vertex_4
        self.vertices = [vertex_1, vertex_2, vertex_3, vertex_4]
        self.edges = [Line(vertex_1, vertex_2), Line(vertex_2, vertex_3),
                      Line(vertex_3, vertex_4), Line(vertex_4, vertex_1)]

    def centroid(self):
        return Line(Line(self.vertex_1, self.vertex_3).midpoint(),
                    Line(self.vertex_2, self.vertex_4).midpoint()).midpoint()

    def contains(self, vertex):
        return _ray_casting(vertex)

    def _ray_casting(self, vertex):
        return _is_odd(sum(_ray_intersect_segment(vertex, edge) for edge in self.edges))

    def _is_odd(number):
        return number % 2 != 0

    def _ray_intersect_segment(vertex, edge):
        '''
        Takes a point p=Pt() and an edge of two endpoints a,b=Pt()
        of a line segment returns boolean.
        '''
        _epsilon = 0.00001

        if edge.start.y > edge.end.y:
            return _ray_intersect_segment(vertex, Line(edge.end, edge.start))
        elif vertex.y == edge.start.y or vertex.y == edge.end.y:
            return _ray_intersect_segment(Vertex(vertex.x, vertex.y + _epsilon, 0), edge)
        elif vertex.y > edge.end.y or vertex.y < edge.start.y or vertex.x > max(edge.start.x, edge.end.x):
            return false
        elif vertex.x < min(edge.start.x, edge.end.x):
            return true
        else:
            left = sys.maxsize
            right = sys.maxsize
            if abs(edge.start.x - vertex.x) > sys.minsize:
                left = (vertex.y - edge.start.y) / (vertex.x - edge.start.x)
            if abs(edge.start.x - edge.end.x) > sys.minsize:
                right = (edge.end.y - edge.start.y) / (edge.end.x - edge.start.x)
            return left >= right

    def __in_bounding_box(self, vertex):
        (vertex.x > self.vertex_1.x and vertex.x < self.vertex_4.x) and (vertex.y > vertex_3.y and vertex.y < vertex_2.y)