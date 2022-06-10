import plotly.graph_objects as go
from plotly.offline import plot


class Bezier_2d:
    def __init__(self, points_control, N=50, t=5e-3, echantillonnage=1000, show_control_points=True):
        """
        :param points_control: list of list of size 2, with x, y of each point
        :param N: Bezier param
        :param t: Bezier param
        :param echantillonnage: Amount of points in Bezier curve
        """
        self.points_control = points_control
        self.N = N
        self.t = t
        self.echantillonnage = echantillonnage
        self.show_control_points = show_control_points

    def combinaison_lineaire(self, A, B, u, v):
        return [A[0] * u + B[0] * v, A[1] * u + B[1] * v]

    def interpolation_lineaire(self, A, B, t):
        return self.combinaison_lineaire(A, B, t, 1 - t)

    def reduction(self, points_control, t):
        points_sortie = []
        N = len(points_control)
        for i in range(N - 1):
            points_sortie.append(self.interpolation_lineaire(points_control[i], points_control[i + 1], 1 - t))
        return points_sortie

    def point_bezier_n(self, points_control, t):
        n = len(points_control)
        while n > 1:
            points_control = self.reduction(points_control, t)
            n = len(points_control)
        return points_control[0]

    def courbe_bezier_n(self, points_control, N):
        n = len(points_control)
        dt = 1.0 / N
        t = dt
        points_courbe = [points_control[0]]
        while t < 1.0:
            points_courbe.append(self.point_bezier_n(points_control, t))
            t = t + dt
        points_courbe.append(points_control[n - 1])
        return points_courbe

    def plot_points(self, points_courbe):
        x, y = [], []
        for p in points_courbe:
            x.append(p[0])
            y.append(p[1])
        return x, y

    def show_bezier(self):
        fig = go.Figure()
        # === vertical
        Pi = self.points_control
        points = self.courbe_bezier_n(Pi, self.echantillonnage)
        x_bezier, y_bezier = self.plot_points(points)
        fig.add_scatter(y=y_bezier,
                        x=x_bezier,
                        mode="lines",
                        name="Bezier curve"
                        )
        if self.show_control_points:
            x_control_pts, y_control_pts = self.plot_points(Pi)
            fig.add_scatter(y=y_control_pts,
                            x=x_control_pts,
                            mode="lines+markers",
                            name="Control points",
                            marker=dict(size=3)
                            )

        fig.update_layout(showlegend=True)
        return x_bezier, y_bezier, fig
