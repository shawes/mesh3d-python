from vertex import Vertex
from face import Face
import helpers
import numpy
import pdb


class Mesh(object):

    def __init__(self, vertices, faces):
        self.vertices = vertices
        self.faces = faces
        self.quadrats = list()
        #self.extremes = self._calculate_extremes()

    def calculate_metrics(self, quadrats):
        self.quadrats = quadrats
        for face in self.faces.tolist():
            for quadrat in self.quadrats:
                if quadrat.contains(face.centroid) is True:
                    quadrat.metric.area3d += face.area3d
                    quadrat.metric.area2d += face.area2d
                    quadrat.metric.face_count += 1
                    quadrat.vertices_inside += face.vertices
                    break
                else:
                    pass

        for quadrat in self.quadrats:
            quadrat.vertices_inside = list(set(quadrat.vertices_inside)) # get unique vertices
            z_values = list(map(helpers.get_z_value, quadrat.vertices_inside))
            if len(z_values) > 0:
                quadrat.metric.relative_z_mean = numpy.mean(z_values)
                quadrat.metric.relative_z_sd = numpy.std(z_values)
        #return quadrats


    #def _get_metrics_for_quadrat(self, quadrat):


        # z_values = list(map(lambda v: v.z, self.vertices))
        # if len(z_values) > 0:
        #     quadrat.relative_z_avg = numpy.mean(z_values)
        #     quadrat.relative_z_std = numpy.std(z_values)

        #print("area is " + str(area3d))
        #print("faces count is " + str(faces_count))

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
