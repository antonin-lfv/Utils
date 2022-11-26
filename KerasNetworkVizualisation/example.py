""" Usage example """
from KerasNetworkVizualisation.NNviz import *

if __name__ == '__main__':
    # Model
    model = Sequential()
    model.add(Dense(8, activation='relu'))
    model.add(Dense(7, activation='relu'))
    model.add(Dense(13, activation='softmax'))
    model.add(Dense(10, activation='sigmoid'))
    model.add(Dense(4, activation='softmax'))
    model.add(Dense(14, activation='relu'))
    model.add(Dense(1))

    MyFirstNN = VizNN(model)
    MyFirstNN.plot_NN()