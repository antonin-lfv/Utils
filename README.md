# Documentation

<br>

1. [3D linear interpolation](#3d-linear-interpolation)
2. [Neural Network Vizualisation](#neural-network-vizualisation)

<br>

# 3D linear interpolation

After creating your object with your matrix, 3 methods are available :

```py
m = np.fromfunction(lambda x, y: np.sqrt(x**2+y**2), (15, 30))
MyInterp = Interpolator(matrix=m)
```

```py
# With color gradient (unique plot)
MyInterp.graph_3D_color(display=True)  # display=True to juste plot this figure
```
<p align="center">
<img width="1296" alt="Capture d’écran 2022-03-29 à 21 43 32" src="https://user-images.githubusercontent.com/63207451/160694388-3b37ea93-064b-4d68-ba09-bc84802cf319.png">
  <p/>

```py
# With lines (unique plot)
MyInterp.graph_3D_line(display=True)
```

<p align="center">
<img width="862" alt="Capture d’écran 2022-03-29 à 21 39 50" src="https://user-images.githubusercontent.com/63207451/160693810-e26f25df-d6cb-4434-b9e3-955eb766625e.png">
  <p/>
  

```py
# Subplot with gradient and lines
MyInterp.subplot_line_gradient()
```

<p align="center">
<img width="1368" alt="Capture d’écran 2022-03-29 à 21 38 48" src="https://user-images.githubusercontent.com/63207451/160693661-d86cadcb-edcf-4ea6-ab35-25123add55cd.png">
  <p/>
  
If Display is False, then the function will return the plotly.fig object

# Neural Network Vizualisation

After creating your object with your model, use the method called plot to vizualise your network

```py
# Model
model = Sequential()
model.add(Dense(8, activation='relu'))
model.add(Dense(7, activation='relu'))
model.add(Dense(13, activation='relu'))
model.add(Dense(17, activation='relu'))
model.add(Dense(4, activation='relu'))
model.add(Dense(4, activation='relu'))
model.add(Dense(1))

MyFirstNN = VizNN(model)
MyFirstNN.plot_NN()
```

<p align="center">
<img width="1390" alt="Capture d’écran 2022-03-29 à 21 31 21" src="https://user-images.githubusercontent.com/63207451/160692553-f7931493-fc5a-47e9-be17-585574785d98.png">
  <p/>
