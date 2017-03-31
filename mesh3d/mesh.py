from vertex import Vertex
from face import Face
import helpers
#import numpy
import pdb


class Mesh(object):

    def __init__(self, vertices, faces):
        self.vertices = vertices
        self.faces = faces
        #self.extremes = self._calculate_extremes()

    def get_area(self, quadrats):
        area = []
        for quadrat in quadrats:
            area.append(self._get_area_of_face_in_quadrat(quadrat))
        return area

    def _get_area_of_face_in_quadrat(self, quadrat):
        area2d = 0.0
        area3d = 0.0
        faces_count = 0
        quadrat_vertices = []
        #pdb.set_trace()
        for face in self.faces:
            if quadrat.contains(face):
                faces_count += 1
                area2d += face.area(is_3d=False)
                area3d += face.area(is_3d=True)
                quadrat_vertices += face.vertices
            else:
                pass

        # z_values = list(map(lambda v: v.z, self.vertices))
        # if len(z_values) > 0:
        #     quadrat.relative_z_avg = numpy.mean(z_values)
        #     quadrat.relative_z_std = numpy.std(z_values)

        #print("area is " + str(area3d))
        #print("faces count is " + str(faces_count))
        return (area3d, area2d, faces_count, len(set(quadrat_vertices)))

    # def _calculate_extremes(self):
    #     pdb.set_trace()
    #     min_x = self.vertices[0]
    #     min_y = self.vertices[0]
    #     max_x = self.vertices[0]
    #     max_y = self.vertices[0]
    #     for vertex in self.vertices:
    #         if helpers.is_min(min_x.x, vertex.x) is False:
    #             min_x = vertex
    #         if helpers.is_min(min_y.y, vertex.y) is False:
    #             min_y = vertex
    #         if helpers.is_max(max_x.x, vertex.x) is False:
    #             max_x = vertex
    #         if helpers.is_max(max_y.y, vertex.y) is False:
    #             max_y = vertex
    #     return (min_x, min_y, max_x, max_y)
