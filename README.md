<p align="center">
	<img src="https://user-images.githubusercontent.com/63207451/114284722-45901b80-9a52-11eb-8a0c-e99fc8681436.gif" height="80" width="140">
	<p/>

<h1 align="center">Tools documentation</h1>

<br>

### Index


1. [Interpolations](#Interpolations)
	1. [3D linear interpolation](#3d-linear-interpolation)
	2. [3D Bezier interpolation](#3d-Bezier-interpolation)
2. [Bezier curves](#Bezier-curves)
	1. [2D Bezier curves](#2d-Bezier-curves)
	2. [3D Bezier curves](#3d-Bezier-curves)
3. [Keras Network Vizualisation](#keras-network-vizualisation)
4. [Simple ANN Vizualisation](#simple-ann-vizualisation) (**New !**)
5. [Graph plot with Plotly](#graph-plot-with-plotly)
   1. [2D graph plot](#2d-graph-plot)
   2. [3D graph plot](#3d-graph-plot)
6. [Circles intersection](#circles-intersection)
7. [Plot N points with distances between](#plot-n-points-with-distances-between)
8. [3D structure generation wizard](#3d-structure-generation-wizard) (**New !**)

<br>

<br>

# Interpolations


## 3D linear interpolation

[🔗 code source](https://github.com/antonin-lfv/Utils/blob/main/Interpolations/Linear_interpolation_3D/LinearInterpolation3D.py)

After creating your object with your matrix (creates with numpy and lambda functions or just with a $n*m$ numpy matrix), 3 methods are available :

```python
# m is a numpy matrix
MyInterp = Interpolator(matrix=m)
```


```py
# 1. With color gradient (unique plot)
MyInterp.graph_3D_color(display=True)  # display=True to juste plot this figure
```
<p align="center">
<img width="1296" alt="Capture d’écran 2022-03-29 à 21 43 32" src="https://user-images.githubusercontent.com/63207451/160694388-3b37ea93-064b-4d68-ba09-bc84802cf319.png">
  <p/>

<br>

```py
# 2. With lines (unique plot)
MyInterp.graph_3D_line(display=True)
```

<p align="center">
<img width="862" alt="Capture d’écran 2022-03-29 à 21 39 50" src="https://user-images.githubusercontent.com/63207451/160693810-e26f25df-d6cb-4434-b9e3-955eb766625e.png">
  <p/>
  
<br>

```py
# 3. Subplot with gradient and lines
MyInterp.subplot_line_gradient()
```

<p align="center">
<img width="1368" alt="Capture d’écran 2022-03-29 à 21 38 48" src="https://user-images.githubusercontent.com/63207451/160693661-d86cadcb-edcf-4ea6-ab35-25123add55cd.png">
  <p/>
  
If Display is False, then the function will return the plotly.fig object

<br>

## 3D Bezier interpolation

[🔗 code source](https://github.com/antonin-lfv/Utils/blob/main/Interpolations/Bezier_interpolation_3D/BezierInterpolation3D.py)

With a numpy matrix, you can recreate the surface

```py
from Interpolations.Bezier_interpolation_3D.BezierInterpolation3D import *
import pandas as pd
import numpy as np

# real data
z_data_1 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv',
                       nrows=10)

model = BezierInterpolation(matrix=np.array(z_data_1))
model.show_bezier()
```

<p align="center">
<img width="817" alt="Capture d’écran 2022-06-10 à 22 46 31" src="https://user-images.githubusercontent.com/63207451/173149569-511ee4a0-6327-4e64-9682-27ac5035aa88.png">
  <p/>

<br>

# Bezier curves


## 2D Bezier curves

[🔗 code source](https://github.com/antonin-lfv/Utils/blob/main/BezierCurves/Bezier_curves_2D/BezierCurves2D.py)

With the list of lists of all points

```py
from plotly.offline import plot
from BezierCurves.Bezier_curves_2D.BezierCurves2D import *

Points_control = [[2, 1], [4, 7], [5, 7], [8, 4], [10, 8], [13, 15]]
model = Bezier_2d(points_control=Points_control)
x_b, y_b, fig_b = model.show_bezier()
plot(fig_b)
```

<p align="center">
<img width="1345" alt="Capture d’écran 2022-06-10 à 22 50 20" src="https://user-images.githubusercontent.com/63207451/173150090-bb1e37d8-0727-4596-b234-c7f97cef9d0a.png">
  <p/>

<br>

## 3D Bezier curves

[🔗 code source](https://github.com/antonin-lfv/Utils/blob/main/BezierCurves/Bezier_curves_3D/BezierCurves3D.py)

With the list of lists of all points

```py
from BezierCurves.Bezier_curves_3D.BezierCurves3D import *
from plotly.offline import plot
from numpy import array as a

points_control = a([[0, 0, 0], [1, 4, 2], [2, 2, 4], [2, 1, 0]])
model = Bezier_3d(points_control=points_control, show_control_points=True)
x_curve, y_curve, z_curve, x_pts, y_pts, z_pts, fig_b = model.show_bezier()
plot(fig_b)
```

<p align="center">
<img width="1280" alt="Capture d’écran 2022-06-10 à 22 52 14" src="https://user-images.githubusercontent.com/63207451/173150331-3d442905-7b5c-49c9-b1d5-e9210bb1fb9d.png">
  <p/>

<br>

# Keras Network Vizualisation

[🔗 code source](https://github.com/antonin-lfv/Utils/blob/main/KerasNetworkVizualisation/NNviz.py)

After creating your object with your model, use the method called plot to vizualise your network

```py
# Model
model = Sequential()
model.add(Dense(8, activation='relu'))
model.add(Dense(7, activation='relu'))
model.add(Dense(13, activation='softmax'))
model.add(Dense(10, activation='sigmoid'))
model.add(Dense(4, activation='softmax'))
model.add(Dense(4, activation='relu'))
model.add(Dense(1))

MyFirstNN = VizNN(model)
MyFirstNN.plot_NN()
```

<br>

<p align="center">
<img width="1352" alt="Capture d’écran 2022-03-30 à 11 02 32" src="https://user-images.githubusercontent.com/63207451/160794108-a0619606-0d19-44d3-85b6-ad8457a3336d.png">
  <p/>

<br>

# Simple ANN Vizualisation

[🔗 code source](https://github.com/antonin-lfv/Utils/blob/main/SimpleANNVizualisation/ANNVizualisation.py)

Plot a neural network with the number of neurons per layer

```py
from SimpleANNVizualisation.ANNVizualisation import *

NN = NeuralNetworkPlot(layers_list=[10, 10, 5, 5, 1])
NN.plot_neural_network()
```

<br>

<p align="center">
<img width="1352" alt="ann" src="https://user-images.githubusercontent.com/63207451/204110177-cca6966f-d229-4e78-90b8-1b1677169ca9.png">
  <p/>

<br>

# Graph plot with Plotly


## 2D graph plot

[🔗 code source](https://github.com/antonin-lfv/Utils/blob/main/PlotGraph/D2Graph/D2GraphPlot.py)

To plot your graph, just fill the csv file (aretes_2D, noeuds_2D) with your data, then :

```python
from PlotGraph.D2Graph.D2GraphPlot import *

# Data
node_csv_2d = pd.read_csv('data/noeuds_2D.csv', sep=';')
edge_csv_2d = pd.read_csv('data/aretes_2D.csv', sep=';')
# Plot
fig_2D = graphe_2d(nodes=node_csv_2d, edges=edge_csv_2d, titre="myTitle")
plot(fig_2D)
```

<p align="center">
<img width="1395" alt="Capture d’écran 2022-04-29 à 10 33 51" src="https://user-images.githubusercontent.com/63207451/165910921-6e66ee06-13ec-4529-bfd8-c33844780103.png">  
  </p>

<br>

<br>

## 3D graph plot

[🔗 code source](https://github.com/antonin-lfv/Utils/blob/main/PlotGraph/D3Graph/D3GraphPlot.py)

To plot your graph, just fill the csv file (aretes_3D, noeuds_3D) with your data, then :

```python
from PlotGraph.D3Graph.D3GraphPlot import *

# Data
node_csv_3D = pd.read_csv('data/neouds_3D.csv', sep=';')
edge_csv_3D = pd.read_csv('data/aretes_3D.csv', sep=';')
# Plot
fig_3D = graphe_3d(nodes=node_csv_3D, edges=edge_csv_3D)
plot(fig_3D)
```

<p align="center">
<img width="1005" alt="Capture d’écran 2022-06-08 à 21 13 20" src="https://user-images.githubusercontent.com/63207451/172698309-715d6df6-2ddb-4c8c-9db7-5cb01bc53d85.png">
</p>

<br>

# Circles intersection

[🔗 code source](https://github.com/antonin-lfv/Utils/blob/main/CirclesIntersection/CirclesIntersect.py)

You just need to put the centers coordinates and the radius of each circles. One list for the x, another one for the y, 
and a last for the radius. You will obtain the solution of the system of equations allowing to find the intersection 
of n circles. If the intersection does not exist geometrically, the solution corresponds to the closest point of all circles.

````py
from CirclesIntersection.CirclesIntersect import *
import warnings
warnings.filterwarnings('ignore', 'The iteration is not making good progress')

centres_x = [0, 3, -0.49]
centres_y = [0, 0, 1.93]
rayons = [4.89, 2.89, 4.65]

print(solve_inter_circles(centres_x=centres_x, centres_y=centres_y, rayons=rayons))
````

````bash
OUT : (4.099264653603768, 2.669805721160483)
````

<br>

# Plot N points with distances between

[🔗 code source](https://github.com/antonin-lfv/Utils/blob/main/PlotNpoints/Npoints.py)

If you only know the distance between n points, this code will plot them. (Not the only way to plot them)

````py
from PlotNpoints.Npoints import *

# symmetrical matrix 
# The value of coord i,j gives the distance between the ith and the jth points (ordered by index)
Points = [
    [0, 3, 2, 4.894],
    [3, 0, 4, 2.899113],
    [2, 4, 0, 4.65457],
    [4.894, 2.899113, 4.65457, 0]
]

plotPoints(Points)
````

**Results** 

<p align="center">
<img alt="Capture d’écran 2022-08-30 à 14 29 19" src="https://user-images.githubusercontent.com/63207451/187437949-f3a39c56-46d1-401d-b7be-3456b306b306.png"></p>

<br>

**Proof**

<p align="center">
<img width="600" alt="Capture d’écran 2022-06-08 à 21 13 20" src="https://user-images.githubusercontent.com/63207451/187437960-3c45cffd-c56f-4945-b818-2480bcd98916.png">
</p>

<br>

# 3D structure generation wizard

[🔗 code source](https://github.com/antonin-lfv/Utils/tree/main/3dStructureGeneration/streamlit3dStructureGeneration)

Open the wizard from [here](https://3dstructuregenerationstreamlit3dstructuregenerationhom-q9yptg.streamlitapp.com/) and start creating your 3D structure. You can also import your data, and visualize the generated structure.

<br>

![Capture d’écran 2022-10-01 à 22 09 52](https://user-images.githubusercontent.com/63207451/193426613-65cbcc46-905f-49c3-9fa3-c7fee29bd04b.png)

<br>

<p align="center">
	  <a href="https://antonin-lfv.github.io" class="fancybox" ><img src="https://user-images.githubusercontent.com/63207451/127334786-f48498e4-7aa1-4fbd-b7b4-cd78b43972b8.png" title="Web Page" width="38" height="38"></a>
  <a href="https://github.com/antonin-lfv" class="fancybox" ><img src="https://user-images.githubusercontent.com/63207451/97302854-e484da80-1859-11eb-9374-5b319ca51197.png" title="GitHub" width="40" height="40"></a>
  <a href="https://www.linkedin.com/in/antonin-lefevre-565b8b141" class="fancybox" ><img src="https://user-images.githubusercontent.com/63207451/97303444-b2c04380-185a-11eb-8cfc-864c33a64e4b.png" title="LinkedIn" width="40" height="40"></a>
  <a href="mailto:antoninlefevre45@icloud.com" class="fancybox" ><img src="https://user-images.githubusercontent.com/63207451/97303543-cec3e500-185a-11eb-8adc-c1364e2054a9.png" title="Mail" width="40" height="40"></a>
</p>


---------------------------
