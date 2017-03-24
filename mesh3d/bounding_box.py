from shapes.quadrilateral import Quadrilateral
from shapes.vertex import Vertex
import pdb


class BoundingBox(Quadrilateral):

    def __init__(self, meshes):
        Quadrilateral.__init__(
            self,
            Vertex(min(map(lambda m: m.extremes[2], meshes)).x, min(map(lambda m: m.extremes[3], meshes)).y, 0),
            Vertex(min(map(lambda m: m.extremes[2], meshes)).x, min(map(lambda m: m.extremes[1], meshes)).y, 0),
            Vertex(min(map(lambda m: m.extremes[0], meshes)).x, min(map(lambda m: m.extremes[1], meshes)).y, 0),
            Vertex(min(map(lambda m: m.extremes[0], meshes)).x, min(map(lambda m: m.extremes[3], meshes)).y, 0))
            
