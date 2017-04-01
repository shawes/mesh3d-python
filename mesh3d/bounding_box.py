from quadrilateral import Quadrilateral
from vertex import Vertex
import pdb


class BoundingBox(Quadrilateral):

    def __init__(self, meshes):

        min_x = 100000 # start with something much higher than expected min
        min_y = 100000
        max_x = -100000 # start with something much lower than expected max
        max_y = -100000

        for mesh in meshes:
            for vertex in mesh.values[0]:
                if vertex.x < min_x:
                  min_x = vertex.x
                if vertex.x > max_x:
                  max_x = vertex.x
                if vertex.y < min_y:
                  min_y = vertex.y
                if vertex.y > max_y:
                  max_y = vertex.y

        Quadrilateral.__init__(self,
                               Vertex(min_x,min_y,0),
                               Vertex(max_x,min_y,0),
                               Vertex(max_x,max_y,0),
                               Vertex(min_x,max_y,0))
