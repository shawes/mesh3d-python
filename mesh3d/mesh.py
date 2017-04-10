from .vertex import Vertex
from .face import Face
from .metric import Metric
import .helpers
import pdb

class Mesh(object):

    def __init__(self, faces):
        self.faces = faces

    def calculate_metrics(self, quadrats):
        metrics = list()
        for quadrat in quadrats:
            metric = Metric()
            quadrat_vertices = list()
            metric.quadrat_id = quadrat.id
            metric.quadrat_midpoint = quadrat.midpoint
            for face in self.faces:
                if quadrat.contains(face.centroid):
                    metric.area3d += face.area3d
                    metric.area2d += face.area2d
                    metric.face_count += 1
                    quadrat_vertices += face.vertices
                else:
                    pass
            quadrat_vertices = list(set(quadrat_vertices))
            metric.vertices_count = len(quadrat_vertices)
            z_values = list(map(helpers.get_z_value, quadrat_vertices))
            if len(z_values) > 0:
                metric.relative_z_mean = helpers.mean(z_values)
                metric.relative_z_sd = helpers.sd(z_values, sample=False)
            metrics.append(metric)
        return metrics
