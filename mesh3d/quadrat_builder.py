from shapes.line import Line
from shapes.vertex import Vertex
from quadrat import Quadrat
import pdb


class QuadratBuilder(object):
    """A class that builds quadrats on a mesh, starting from the centre position."""

    def build(self, box, size):
        """
            Method to contruct a list of quadrats using a given bounding box.
            @param box the bounding box of the meshes to measure
            @param size the size of the square quadrilateral (in the units of the provided mesh)
            @return list of the quadrats that fit the bounding box
        """
        centroid = box.centroid()
        print("This is the centroid:" + str(centroid))
        quadrats = list()
        distance_to_edge1 = centroid.distance_to_xyz(Line(box.vertex_4, box.vertex_1).midpoint())
        distance_to_edge2 = centroid.distance_to_xyz(Line(box.vertex_3, box.vertex_4).midpoint())

        quadrat_indexes1 = range(int(distance_to_edge2 / size) + 1)
        quadrat_indexes2 = range(int(distance_to_edge1 / size) + 1)

        #(i <- 0 until (distanceToEdgeCD / size).toInt + 1)

        pdb.set_trace()
        for index_i in quadrat_indexes1:
            for index_j in quadrat_indexes2:
                if index_i == 0 and index_j == 0:
                    quadrats.append(Quadrat((0, 0), size, centroid))
                else:
                    four_quadrats = [Quadrat((index_i, index_j), size,
                                                 Vertex(centroid.x + index_i * size, centroid.y + (index_j * size), centroid.z)),
                                         Quadrat((index_i, index_j * -1), size,
                                                 Vertex(centroid.x + index_i * size, centroid.y - (index_j * size), centroid.z)),
                                         Quadrat((index_i * -1, index_j), size,
                                                 Vertex(centroid.x - index_i * size, centroid.y + (index_j * size), centroid.z)),
                                         Quadrat((index_i * -1, index_j * -1), size,
                                                 Vertex(centroid.x - index_i * size, centroid.y - (index_j * size), centroid.z))]
                    quadrats_inside = filter(lambda x: box.contains(x.midpoint), four_quadrats)
                    quadrats += quadrats_inside
        return list(set(quadrats))
