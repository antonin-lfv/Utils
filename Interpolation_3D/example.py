""" Usage example """
from Interpolation_3D.LinearInterpolation3D import *
import pandas as pd
z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')

Z = np.array([[7.894736842105264, 7.894736842105264, 7.894736842105264, 8.947368421052632, 8.947368421052632, 10.0,
               10.0, 10.0, 10.0, 10.0, 10.0],
              [6.842105263157896, 6.842105263157896, 7.894736842105264, 8.947368421052632, 8.947368421052632,
               8.947368421052632, 10.0, 10.0, 10.0, 10.0, 10.0],
              [5.789473684210527, 5.789473684210527, 5.789473684210527, 6.842105263157896, 6.842105263157896,
               7.894736842105264, 8.947368421052632, 10.0, 10.0, 10.0, 10.0],
              [5.789473684210527, 5.789473684210527, 5.789473684210527, 5.789473684210527, 5.789473684210527,
               6.842105263157896, 6.842105263157896, 8.947368421052632, 10.0, 10.0, 10.0],
              [3.6842105263157894, 4.736842105263158, 4.736842105263158, 5.789473684210527, 5.789473684210527,
               5.789473684210527, 6.842105263157896, 7.894736842105264, 8.947368421052632, 10.0, 10.0],
              [3.6842105263157894, 3.6842105263157894, 3.6842105263157894, 3.6842105263157894, 4.736842105263158,
               5.789473684210527, 5.789473684210527, 6.842105263157896, 8.947368421052632, 8.947368421052632, 8.95],
              [2.6315789473684212, 2.6315789473684212, 2.6315789473684212, 3.6842105263157894, 3.6842105263157894,
               5.789473684210527, 5.789473684210527, 6.842105263157896, 8.947368421052632, 8.947368421052632, 8.95],
              [1.5789473684210527, 1.5789473684210527, 2.6315789473684212, 2.6315789473684212, 3.6842105263157894,
               4.736842105263158, 5.789473684210527, 5.789473684210527, 7.894736842105264, 7.894736842105264, 7.9],
              [0.5263157894736843, 0.5263157894736843, 1.5789473684210527, 2.6315789473684212, 3.6842105263157894,
               4.736842105263158, 5.789473684210527, 5.789473684210527, 6.842105263157896, 7.894736842105264, 7.9],
              [-0.5263157894736843, 0.5263157894736843, 1.5789473684210527, 2.6315789473684212, 3.6842105263157894,
               3.6842105263157894, 5.789473684210527, 5.789473684210527, 6.842105263157896, 7.894736842105264, 7.9]])

if __name__ == "__main__":
    mon_interpolateur = Interpolator(matrix=z_data.values)
    # With color gradient
    f1 = mon_interpolateur.graph_3D_color()
    # With lines
    f2 = mon_interpolateur.graph_3D_line()
    # Plot the 2 fig
    plt.show()