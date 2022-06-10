# Documentation

<br>

1. [Interpolations](#Interpolations)
	1. [3D linear interpolation](#3d-linear-interpolation)
	2. [3D Bezier interpolation](#3d-Bezier-interpolation)
2. [Bezier curves](#Bezier-curves)
	1. [2D Bezier curves](#2d-Bezier-curves)
	2. [3D Bezier curves](#3d-Bezier-curves)
3. [Neural Network Vizualisation](#neural-network-vizualisation)
4. [Graph plot with Plotly](#graph-plot-with-plotly)
   1. [2D graph plot](#2d-graph-plot)
   2. [3D graph plot](#3d-graph-plot)

<br>

# Interpolations

<br>

## 3D linear interpolation

After creating your object with your matrix, 3 methods are available :

```py
m = np.fromfunction(lambda x, y: np.sqrt(x**2+y**2), (15, 30))
MyInterp = Interpolator(matrix=m)
```

<br>

```py
# With color gradient (unique plot)
MyInterp.graph_3D_color(display=True)  # display=True to juste plot this figure
```
<p align="center">
<img width="1296" alt="Capture d’écran 2022-03-29 à 21 43 32" src="https://user-images.githubusercontent.com/63207451/160694388-3b37ea93-064b-4d68-ba09-bc84802cf319.png">
  <p/>

<br>

```py
# With lines (unique plot)
MyInterp.graph_3D_line(display=True)
```

<p align="center">
<img width="862" alt="Capture d’écran 2022-03-29 à 21 39 50" src="https://user-images.githubusercontent.com/63207451/160693810-e26f25df-d6cb-4434-b9e3-955eb766625e.png">
  <p/>
  
<br>

```py
# Subplot with gradient and lines
MyInterp.subplot_line_gradient()
```

<p align="center">
<img width="1368" alt="Capture d’écran 2022-03-29 à 21 38 48" src="https://user-images.githubusercontent.com/63207451/160693661-d86cadcb-edcf-4ea6-ab35-25123add55cd.png">
  <p/>
  
If Display is False, then the function will return the plotly.fig object

<br>

## 3D Bezier interpolation

<br>

# Bezier curves

<br>

## 2D Bezier curves

<br>

## 3D Bezier curves

<br>

# Neural Network Vizualisation

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

# Graph plot with Plotly

## 2D graph plot

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

<p align="center">
	  <a href="https://antonin-lfv.github.io" class="fancybox" ><img src="https://user-images.githubusercontent.com/63207451/127334786-f48498e4-7aa1-4fbd-b7b4-cd78b43972b8.png" title="Web Page" width="38" height="38"></a>
  <a href="https://github.com/antonin-lfv" class="fancybox" ><img src="https://user-images.githubusercontent.com/63207451/97302854-e484da80-1859-11eb-9374-5b319ca51197.png" title="GitHub" width="40" height="40"></a>
  <a href="https://www.linkedin.com/in/antonin-lefevre-565b8b141" class="fancybox" ><img src="https://user-images.githubusercontent.com/63207451/97303444-b2c04380-185a-11eb-8cfc-864c33a64e4b.png" title="LinkedIn" width="40" height="40"></a>
  <a href="mailto:antoninlefevre45@icloud.com" class="fancybox" ><img src="https://user-images.githubusercontent.com/63207451/97303543-cec3e500-185a-11eb-8adc-c1364e2054a9.png" title="Mail" width="40" height="40"></a>
</p>


---------------------------
