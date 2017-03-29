from vertex import Vertex
from face import Face
import numpy


class Mesh(object):

    def __init__(self, vertices, faces):
        self.vertices = vertices
        self.faces = faces
        self.extremes = self._calculate_extremes(vertices)

    def get_area(self, quadrats):
        return map(lambda x: self._get_area_of_face_in_quadrat(x), quadrats)

    def _get_area_of_face_in_quadrat(self, quadrat):
        self.area2d = 0.0
        self.area3d = 0.0
        self.faces_count = 0
        for face in self.faces:
            if quadrat.contains(face.centroid):
                # print("Getting some area action!")
                self.faces_count += 1
                # print("faces count is " + str(self.faces_count))
                self.area2d += face.area(is_3d=False)
                self.area3d += face.area(is_3d=True)
                print("Area = "+ str(self.area3d))
                self.vertices.append(face.vertices[0])
                self.vertices.append(face.vertices[1])
                self.vertices.append(face.vertices[2])

        z_values = map(lambda v: v.z, self.vertices)
        if len(z_values) > 0:
            quadrat.relative_z_avg = numpy.mean(z_values)
            quadrat.relative_z_std = numpy.std(z_values)

        print("area is " + str(self.area3d))
        print("faces count is " + str(self.faces_count))
        return (self.area3d, self.area2d, self.faces_count, len(set(self.vertices)))

    def _calculate_extremes(self, vertices):
        if not vertices:
            return list()
        else:
            return (reduce(lambda v1, v2: v1 if (v1.x > v2.x) else v2, vertices),
                    reduce(lambda v1, v2: v1 if (v1.x > v2.x) else v2, vertices),
                    reduce(lambda v1, v2: v1 if (v1.x < v2.x) else v2, vertices),
                    reduce(lambda v1, v2: v1 if (v1.x < v2.x) else v2, vertices))
