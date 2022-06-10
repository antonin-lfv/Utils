""" Usage example """
from Interpolations.Linear_interpolation_3D.LinearInterpolation3D import *
import pandas as pd
import numpy as np

m1 = np.fromfunction(lambda x, y: np.sin(x/5)+np.cos(y/5)+0.1, (20, 20))
m2 = np.fromfunction(lambda x, y: np.cos(np.sin(x)+2*y+1)-5, (30, 30))
m3 = np.fromfunction(lambda x, y: np.sqrt(x**2+y**2), (15, 30))

z_data_1 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')
z_data_2 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/3d_line_sample_data.csv', nrows=110, skiprows=10)
z_data_3 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/line_3d_dataset.csv')

if __name__ == "__main__":
    mon_interpolateur = Interpolator(matrix=z_data_1)
    # With color gradient (unique plot)
    f1 = mon_interpolateur.graph_3D_color(display=False)  # display=True to juste plot this figure

    # With lines (unique plot)
    f2 = mon_interpolateur.graph_3D_line(display=False)

    # Subplot with gradient and lines
    mon_interpolateur.subplot_line_gradient()

