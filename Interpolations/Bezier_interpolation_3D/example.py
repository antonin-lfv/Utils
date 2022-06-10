from Interpolations.Bezier_interpolation_3D.BezierInterpolation3D import *
import pandas as pd
import numpy as np

# real data
z_data_1 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv',
                       nrows=10)


if __name__ == "__main__":
    model = BezierInterpolation(matrix=np.array(z_data_1))
    model.show_bezier()
