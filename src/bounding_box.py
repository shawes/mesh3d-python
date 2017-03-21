from quadrilateral import Quadrilateral
from vertex import Vertex


class BoundingBox(Quadrilateral):

    def __init__(self, meshes):
        v1 = Vertex(map(lambda x: (x.extremes[2]).sort(key=float, reverse=False), meshes)[0],
                    map(lambda x: (x.extremes[3]).sort(key=float, reverse=False), meshes)[0],
                    0)
        v2 = Vertex(map(lambda x: (x.extremes[2]).sort(key=float, reverse=False), meshes)[0],
                    map(lambda x: (x.extremes[1]).sort(key=float, reverse=False), meshes)[-1],
                    0)
        v3 = Vertex(map(lambda x: (x.extremes[0]).sort(key=float, reverse=False), meshes)[-1],
                    map(lambda x: (x.extremes[1]).sort(key=float, reverse=False), meshes)[-1],
                    0)
        v4 = Vertex(map(lambda x: (x.extremes[0]).sort(key=float, reverse=False), meshes)[-1],
                    map(lambda x: (x.extremes[3]).sort(key=float, reverse=False), meshes)[0],
                    0)
        Quadrilateral.__init__(self, v1, v2, v3, v4)
