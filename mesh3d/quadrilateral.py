import math
from vertex import Vertex
import sys



class Quadrilateral(object):

    def __init__(self, vertex_1, vertex_2, vertex_3, vertex_4):
        self.vertices = (vertex_1, vertex_2, vertex_3, vertex_4)
        self.vertices_array = ([[vertex_1.x, vertex_1.y],
                         [vertex_2.x, vertex_2.y],
                         [vertex_3.x, vertex_3.y],
                         [vertex_4.x, vertex_4.y]])

    def contains(self, vertex):
        if self._within(vertex) is True:
            return True
        elif self._bump(vertex) is True:
            return True
        else:
            return False

    def _within(self, vertex):
        inside_x = vertex.x > self.vertices[0].x and vertex.x < self.vertices[1].x
        inside_y = vertex.y > self.vertices[0].y and vertex.y < self.vertices[3].y
        inside = inside_x and inside_y
        return inside

    def _bump(self, vertex):
        _bump_amount = 0.00001
        vertex_bumped = Vertex(vertex.x + _bump_amount,
                               vertex.y + _bump_amount,
                               0)
        return self._within(vertex)
