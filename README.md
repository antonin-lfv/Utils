# Documentation

1. [3D linear interpolation](#3d-linear-interpolation)
2. [Neural Network Vizualisation](#neural-network-vizualisation)


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

```py
# With lines (unique plot)
MyInterp.graph_3D_line(display=True)
```

```py
# Subplot with gradient and lines
MyInterp.subplot_line_gradient()
```

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
