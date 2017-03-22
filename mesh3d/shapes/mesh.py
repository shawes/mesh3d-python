from vertex import Vertex
from face import Face
import numpy


class Mesh(object):

    def __init__(self, vertices, faces):
        self.vertices = vertices
        self.faces = faces
        self.extremes = self._calculate_extremes()

    def get_area(quadrats_list):
        map(map(_get_area_of_face_in_mesh, quadrats), quadrats_list)

    def _get_area_of_face_in_mesh(quadrat):
        area2d = 0.0
        area3d = 0.0
        faces_count = 0
        iterator = iter(self.faces)
        while True:
            try:
                face = iterator.next()
                if quadrat.contains(face.centroid()):
                    faces_count += 1
                    area2d += face.get_area_2D()
                    area3d += face.get_area_3D()
                    vertices += face.v1
                    vertices += face.v2
                    vertices += face.v3
            except StopIteration:
                break

        z_values = map(lambda v: v.z, self.vertices)
        if len(z_values) > 0:
            quadrat.relative_z_avg = numpy.mean(z_values)
            quadrat.relative_z_std = numpy.std(z_values)

        return (area3d, area2d, faces_count, len(set(vertices)))

    def _calculate_extremes(self):
        return (reduce(lambda v1, v2: v1 if (v1.x > v2.x) else v2, self.vertices),
                reduce(lambda v1, v2: v1 if (v1.x > v2.x)
                       else v2, self.vertices),
                reduce(lambda v1, v2: v1 if (v1.x < v2.x)
                       else v2, self.vertices),
                reduce(lambda v1, v2: v1 if (v1.x < v2.x) else v2, self.vertices))
