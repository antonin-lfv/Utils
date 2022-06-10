import plotly.graph_objects as go
from plotly.offline import plot
import numpy as np
from numpy import array as a


class Bezier_3d:
    def __init__(self, points_control, echantillonnage=50, show_control_points=True):
        """
        :param points_control: list of list of size 3 with x, y, z coord of each point
        :param echantillonnage: amount of points in Bezier curve
        """
        self.points_control = points_control
        self.echantillonnage = echantillonnage
        self.show_control_points = show_control_points

    def TwoPoints(self, t, P1, P2):
        Q1 = (1 - t) * P1 + t * P2
        return Q1

    def Points(self, t, points):
        n_points = []
        for i1 in range(0, len(points) - 1):
            n_points += [self.TwoPoints(t, points[i1], points[i1 + 1])]
        return n_points

    def Point(self, t, points):
        n_points = points
        while len(n_points) > 1:
            n_points = self.Points(t, n_points)
        return n_points[0]

    def Curve(self, t_values, points):
        curve = np.array([[0.0] * len(points[0])])
        for t in t_values:
            curve = np.append(curve, [self.Point(t, points)], axis=0)
        curve = np.delete(curve, 0, 0)
        return curve

    def show_bezier(self):
        t_points = np.arange(0, 1, 1 / self.echantillonnage)
        curve_bezier = self.Curve(t_points, self.points_control)
        x_curve, y_curve, z_curve = list(curve_bezier[:, 0]), list(curve_bezier[:, 1]), list(curve_bezier[:, 2])
        x_pts, y_pts, z_pts = list(self.points_control[:, 0]), list(self.points_control[:, 1]), list(self.points_control[:, 2])
        # Plotly figure
        fig = go.Figure()
        fig.add_scatter3d(x=x_curve,
                          y=y_curve,
                          z=z_curve,
                          marker=dict(size=4),
                          name="Bezier curve"
                          )
        if self.show_control_points:
            fig.add_scatter3d(x=x_pts,
                              y=y_pts,
                              z=z_pts,
                              marker=dict(size=4),
                              name="Control points"
                              )
        return x_curve, y_curve, z_curve, x_pts, y_pts, z_pts, fig
