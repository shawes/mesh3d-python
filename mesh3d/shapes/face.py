import math
from vertex import Vertex
from edge import Edge
# import pdb


class Face(object):
    """Class representing a face."""

    def __init__(self, vertex1, vertex2, vertex3):
        """Constructor."""
        self.vertices = [vertex1, vertex2, vertex3]
        self.centroid = Vertex((vertex1.x + vertex2.x + vertex3.x) / 3,
                               (vertex1.y + vertex2.y + vertex3.y) / 3,
                               (vertex1.z + vertex2.z + vertex3.z) / 3)
        self.edges = [Edge(vertex1,vertex2),Edge(vertex2,vertex3), Edge(vertex3,vertex1)]
        self.edges_xy = [Edge(vertex1.make_xy(),vertex2.make_xy()),Edge(vertex2.make_xy(),vertex3.make_xy()),
                          Edge(vertex3.make_xy(),vertex1.make_xy())]
        #self.area3d = self._calc_area3d(vertices[0], vertices[1], vertices[2])
        #self.area2d = self._calc_area2d(vertices[0], vertices[1], vertices[2])

    def area(self, is_3d):
        # pdb.set_trace()
        length_edge1 = 0
        length_edge2 = 0
        length_edge3 = 0
        if(is_3d):
            length_edge1 = self.edges[0]
            length_edge2 = self.edges[1]
            length_edge3 = self.edges[2]
        else:
            length_edge1 = edges_xy[0]
            length_edge2 = edges_xy[1]
            length_edge3 = edges_xy[2]
        semiperimeter = (length_edge1 + length_edge2 + length_edge3) * 0.5
        area = math.sqrt(semiperimeter * (semiperimeter - length_edge1) *
                         (semiperimeter - length_edge2) * (semiperimeter - length_edge3))
        # print("SP = " + str(semiperimeter) + ", area of face is: " + str(area))
        if(area == 0.0):
            print("----------")
            print("Size: " + str(is_3d))
            print(str(self.vertices[0]))
            print(str(self.vertices[1]))
            print(str(self.vertices[2]))
            print("----------")
        return area

    def __str__(self):
        print("centroid is " + str(self.centroid))
