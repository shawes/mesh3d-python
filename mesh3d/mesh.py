from vertex import Vertex
from face import Face
from metric import Metric
import helpers
import numpy
import pdb


class Mesh(object):

    def __init__(self, vertices, faces):
        self.vertices = vertices
        self.faces = faces
        #self.extremes = self._calculate_extremes()

    def calculate_metrics(self, quadrats):
        faces_ids = list()
        metrics = list()
        #print("faces length now: " + str(len(self.faces)))
        for quadrat in quadrats:
            metric = Metric()
            metric.quadrat_id = quadrat.id
            metric.quadrat_midpoint = quadrat.midpoint
            for face_array in numpy.nditer(self.faces, flags=['refs_ok']):
                face = face_array.item(0)
                #pdb.set_trace()
                if quadrat.contains(face.centroid) and not face.inside_quadrat:
                    metric.area3d += face.area3d
                    metric.area2d += face.area2d
                    metric.face_count += 1
                    quadrat.vertices_inside += face.vertices
                    metric.faces.append(face.id)
                    #print("Just added face ID: " + str(face.id) + " to quadrat "+str(quadrat.id))
                    face.inside_quadrat = True

                    #pdb.set_trace()
                else:
                    pass
            metrics.append(metric)

        for quadrat in quadrats:
            for metric in metrics:
                if quadrat.id == metric.quadrat_id:
                    quadrat.vertices_inside = list(set(quadrat.vertices_inside)) # get unique vertices
                    metric.vertices_count = len(quadrat.vertices_inside)
                    z_values = list(map(helpers.get_z_value, quadrat.vertices_inside))
                    if len(z_values) > 0:
                        metric.relative_z_mean = numpy.mean(z_values)
                        metric.relative_z_sd = numpy.std(z_values)
        #print("metrics count = " +str(len(metrics)))
        return metrics


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
