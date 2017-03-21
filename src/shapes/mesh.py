from vertex import Vertex
from face import Face


class Mesh(object):

    def __init__(self, values, order):
        self.order = order
        self.vertices = self._construct_vertices(values[1])
        self.faces = self._construct_faces(values[0])
        self.extremes = self._calculate_extremes()

    def get_areas_3D(self, quadrats_list):
        total_area = 0.0
        for quadrats in quadrats_list:
            total_area += map(self._get_3D_area_of_faces_in_polygon, quadrats)
        return total_area

    def get_areas_2D(self, quadrats_list):
        total_area = 0.0
        for quadrats in quadrats_list:
            total_area += map(self._get_2D_area_of_faces_in_polygon, quadrats)
        return total_area

    def _calculate_extremes(self):
        return (reduce(self._max_x, self.vertices),
                reduce(self._max_y, self.vertices),
                reduce(self._min_x, self.vertices),
                reduce(self._min_y, self.vertices))

    def _max_x():
        lambda v1, v2: v1 if (v1.x > v2.x) else v2

    def _max_y():
        lambda v1, v2: v1 if (v1.y > v2.y) else v2

    def _min_x():
        lambda v1, v2: v1 if (v1.x < v2.x) else v2

    def _min_y():
        lambda v1, v2: v1 if (v1.x < v2.x) else v2

    def _construct_vertices(self, values):
        vertices = list()
        iterator = values.__iter__()
        while True:
            try:
                iterator.next()
                x = self._get_next_number(iterator)
                y = self._get_next_number(iterator)
                z = self._get_next_number(iterator)
                vertices.append(self._get_ordered_vertex(x, y, z))
            except StopIteration:
                break
        print("Constructed vertices, there were " + vertices.len())
        return vertices

    def _construct_faces(self, values):
        faces = list()
        iterator = values.__iter__()
        while True:
            try:
                face = Face(self.vertices(self._get_next_number(iterator, True)),
                            self.vertices(self._get_next_number(iterator, True)),
                            self.vertices(self._get_next_number(iterator, True)))
                faces.append(face)
                self._get_next_number(iterator, True)  # This is the -1 separator
            except StopIteration:
                break
        print("Constructed faces, there were " + faces.len())
        return faces

    def _get_next_number(iterator, is_int):
        number_builder = list()
        while number_builder.len() == 0 or number_builder[-1] != " ":
            try:
                number_builder.append(iterator.next())
            except StopIteration:
                break
        number = None
        if is_int is True:
            number = int("".join(number))
        else:
            number = float("".join(number))
        return number

    def _get_ordered_vertex(self, x, y, z):
        index = self.order.get_third()
        vertex = None
        if index == 0:
            vertex = Vertex(z, y, x)
        elif index == 1:
            vertex = Vertex(x, z, y)
        else:
            vertex = Vertex(x, y, z)
        return vertex

    def _get_3D_area_of_faces_in_polygon(self, polygon):
        return self._get_area_of_faces_in_polygon(polygon, True)

    def _get_2D_area_of_faces_in_polygon(self, polygon):
        return self._get_area_of_faces_in_polygon(polygon, False)

    def _get_area_of_faces_in_polygon(self, polygon, is_3D):
        area = 0.0
        face_count = 0
        iterator = self.faces.__iter__()
        while True:
            try:
                face = iterator.next()
                if(polygon.contains(face.centroid)):
                    face_count += 1
                    if(is_3D is True):
                        area += face.get_area_3D()
                    else:
                        area += face.get_area_2D()
            except StopIteration:
                break
        return (area, face_count)
