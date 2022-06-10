from BezierCurves.Bezier_curves_3D.BezierCurves3D import *
from plotly.offline import plot
from numpy import array as a

if __name__ == "__main__":
    points_control = a([[0, 0, 0], [1, 4, 2], [2, 2, 4], [2, 1, 0]])
    model = Bezier_3d(points_control=points_control, show_control_points=True)
    x_curve, y_curve, z_curve, x_pts, y_pts, z_pts, fig_b = model.show_bezier()
    plot(fig_b)
