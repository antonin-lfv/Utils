from plotly.offline import plot
from BezierCurves.Bezier_curves_2D.BezierCurves2D import *

if __name__ == "__main__":
    Points_control = [[2, 1], [4, 7], [5, 7], [8, 4], [10, 8], [13, 15]]
    model = Bezier_2d(points_control=Points_control)
    x_b, y_b, fig_b = model.show_bezier()
    plot(fig_b)
