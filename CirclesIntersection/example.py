from CirclesIntersection.CirclesIntersect import *
import warnings
warnings.filterwarnings('ignore', 'The iteration is not making good progress')

centres_x = [0, 3, -0.49]
centres_y = [0, 0, 1.93]
rayons = [4.89, 2.89, 4.65]

print(solve_inter_circles(centres_x=centres_x, centres_y=centres_y, rayons=rayons))
