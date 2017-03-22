from shapes.quadrilateral import Quadrilateral
from shapes.vertex import Vertex


class BoundingBox(Quadrilateral):

    def __init__(self, meshes):
        v1 = Vertex(min(map(lambda m: m.extremes[2], meshes)).x, min(map(lambda m: m.extremes[3], meshes)).y, 0)
        v2 = Vertex(min(map(lambda m: m.extremes[2], meshes)).x, min(map(lambda m: m.extremes[1], meshes)).y, 0)
        v3 = Vertex(min(map(lambda m: m.extremes[0], meshes)).x, min(map(lambda m: m.extremes[1], meshes)).y, 0)
        v4 = Vertex(min(map(lambda m: m.extremes[0], meshes)).x, min(map(lambda m: m.extremes[3], meshes)).y, 0)
        Quadrilateral.__init__(self, v1, v2, v3, v4)
