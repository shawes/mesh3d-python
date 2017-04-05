from vertex import Vertex
from quadrat import Quadrat


class QuadratBuilder(object):
    """A class that builds quadrats on a mesh, starting from the centre position."""

    def build(self, box, size):
        """
            Method to contruct a list of quadrats using a given bounding box.
            @param box the bounding box of the meshes to measure
            @param size the size of the square quadrilateral (in the units of the provided mesh)
            @return list of the quadrats that fit the bounding box
        """
        centroid = box.centroid
        edge1_midpoint = _get_midpoint_of_edge(box.vertices[0], box.vertices[1])
        distance_to_edge1 = centroid.distance_to_xyz(edge1_midpoint)
        quadrat_indexes1 = range(int(distance_to_edge1 / size) + 1)

        edge2_midpoint = _get_midpoint_of_edge(box.vertices[0], box.vertices[3])
        distance_to_edge2 = centroid.distance_to_xyz(edge2_midpoint)
        quadrat_indexes2 = range(int(distance_to_edge2 / size) + 1)

        quadrats = list()
        for index_i in quadrat_indexes2:
            for index_j in quadrat_indexes1:
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
                    quadrats_inside = list(filter(lambda x: box.contains(x.midpoint), four_quadrats))
                    quadrats += quadrats_inside
        # print("There are this many quadrats: " + str(len(quadrats)))
        return tuple(set(quadrats))

        def _get_midpoint_of_edge(start, end):
            return Vertex((start.x + end.x) / 2, (start.y + end.y) / 2, (start.z + end.z) / 2)
