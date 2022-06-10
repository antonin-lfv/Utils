import plotly.graph_objects as go
from plotly.offline import plot


class BezierInterpolation:
    def __init__(self, matrix, N=50, t=5e-3, show_control_points=True):
        self.matrix = matrix
        self.N = N
        self.t = t
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
        x = []
        y = []
        for p in points_courbe:
            x.append(p[0])
            y.append(p[1])
        return x, y

    def show_bezier(self):
        fig = go.Figure()
        row, col = self.matrix.shape
        # === vertical
        for j in range(row):
            Pi = [[i, (self.matrix[j])[i]] for i in range(col)]
            points = self.courbe_bezier_n(Pi, 1000)
            x_bezier, y_bezier = self.plot_points(points)
            fig.add_scatter3d(y=[j] * len(x_bezier),
                              z=y_bezier,
                              x=x_bezier,
                              mode="lines",
                              name="Bezier curve"
                              )
            if self.show_control_points:
                x_control_pts, y_control_pts = self.plot_points(Pi)
                fig.add_scatter3d(y=[j] * len(x_control_pts),
                                  z=y_control_pts,
                                  x=x_control_pts,
                                  mode="lines+markers",
                                  name="Control points",
                                  marker=dict(size=3)
                                  )
        # === horizontal
        for j in range(col):
            Pi = [[i, (self.matrix[i])[j]] for i in range(row)]
            points = self.courbe_bezier_n(Pi, 1000)
            x_bezier, y_bezier = self.plot_points(points)
            fig.add_scatter3d(x=[j] * len(x_bezier),
                              z=y_bezier,
                              y=x_bezier,
                              mode="lines",
                              name="Bezier curve"
                              )
            if self.show_control_points:
                x_control_pts, y_control_pts = self.plot_points(Pi)
                fig.add_scatter3d(x=[j] * len(x_control_pts),
                                  z=y_control_pts,
                                  y=x_control_pts,
                                  mode="lines+markers",
                                  name="Control points",
                                  marker=dict(size=3)
                                  )

        fig.update_layout(showlegend=False)
        plot(fig)