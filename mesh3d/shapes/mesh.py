from vertex import Vertex
from face import Face
import numpy


class Mesh(object):

    def __init__(self, vertices, faces):
        self.vertices = vertices
        self.faces = faces
        self.extremes = self._calculate_extremes()

    def get_area(self, quadrats):
        return map(lambda x: self._get_area_of_face_in_quadrat(x), quadrats)

    def _get_area_of_face_in_quadrat(self, quadrat):
        area2d = 0.0
        area3d = 0.0
        faces_count = 0
        for face in self.faces:
            if quadrat.contains(face.centroid()):
                print("Getting some area action!")
                faces_count += 1
                area2d += face.get_area_2d()
                area3d += face.get_area_3d()
                self.vertices.append(face.v1)
                self.vertices.append(face.v2)
                self.vertices.append(face.v3)


        z_values = map(lambda v: v.z, self.vertices)
        if len(z_values) > 0:
            quadrat.relative_z_avg = numpy.mean(z_values)
            quadrat.relative_z_std = numpy.std(z_values)
        print("area is " + str(area3d))
        return (area3d, area2d, faces_count, len(set(self.vertices)))

    def _calculate_extremes(self):
        return (reduce(lambda v1, v2: v1 if (v1.x > v2.x) else v2, self.vertices),
                reduce(lambda v1, v2: v1 if (v1.x > v2.x)
                       else v2, self.vertices),
                reduce(lambda v1, v2: v1 if (v1.x < v2.x)
                       else v2, self.vertices),
                reduce(lambda v1, v2: v1 if (v1.x < v2.x) else v2, self.vertices))
