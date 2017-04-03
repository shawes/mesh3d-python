

class Metric(object):

    def __init__(self):
        self.area3d = 0
        self.area2d = 0
        self.face_count = 0
        self.relative_z_mean = 0.0
        self.relative_z_sd = 0.0

    def rugosity(self):
        if self.area2d > 0:
            return self.area3d / self.area2d
        else:
            return 1
