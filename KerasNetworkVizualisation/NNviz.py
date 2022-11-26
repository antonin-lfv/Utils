import plotly.graph_objects as go
from plotly.offline import plot
import tensorflow as tf
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense


class VizNN:

    def __init__(self, model):
        """
        :param model: tensorflow model
        """
        self.model = model
        self.nb_layers = len(self.model.layers)
        self.neurons_per_layer = [self.model.layers[i].get_config()['units'] for i in range(self.nb_layers)]

    def _create_neurons(self, nb_neurons):
        """
        :param nb_neurons: amount of neuron in this layer
        :return: y position of the layer's neurons in the plot
        """
        nodey = []
        if nb_neurons % 2 == 0:
            nodey += list(range(1, int(nb_neurons / 2) + 1)) + list(range(-1, int(-(nb_neurons / 2)) - 1, -1))
        else:
            nodey += list(range(1, int((nb_neurons - 1) / 2) + 1)) + [0] + list(
                range(-1, int(-((nb_neurons - 1) / 2)) - 1, -1))
        return nodey

    def _create_edges(self, neurons):
        """
        :param neurons: position of all the neurons of the network
        :return: edges between the neurons for the plot
        """
        edgex, edgey = [], []
        for i in range(self.nb_layers - 1):
            for j in neurons[i]:
                for k in neurons[i + 1]:
                    edgex.extend([i, i + 1, None])
                    edgey.extend([j, k, None])
        return edgex, edgey

    def _create_nodes_list(self, neurons):
        """
        :param neurons: position of all the neurons of the network
        :return: nodes lists for plot
        """
        nodex, nodey = [], []
        for i in range(self.nb_layers):
            nodex.extend([i] * len(neurons[i]))
            nodey.extend(neurons[i])
        return nodex, nodey

    def plot_NN(self):
        """
        :return: plot neural network
        """
        dict_neurons = {}
        for i in range(self.nb_layers):
            dict_neurons[i] = self._create_neurons(self.neurons_per_layer[i])

        node_x, node_y = self._create_nodes_list(dict_neurons)
        edge_x, edge_y = self._create_edges(dict_neurons)

        # links
        edge_trace = go.Scatter(
            x=edge_x, y=edge_y,
            line=dict(width=0.5, color='#000000'),
            hoverinfo='none',
            mode='lines')

        # neurons
        node_trace = go.Scatter(
            x=node_x, y=node_y,
            mode='markers',
            hoverinfo='none',
            marker=dict(
                color='#33C4E7',
                size=15,
                line_width=0.5))

        fig = go.Figure(data=[edge_trace, node_trace],
                        layout=go.Layout(
                            titlefont_size=16,
                            showlegend=False,
                            hovermode='closest',
                            margin=dict(b=20, l=5, r=5, t=40),
                            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                            paper_bgcolor='rgba(0,0,0,0)',
                            plot_bgcolor='rgba(0,0,0,0)',
                        )
                        )

        # activation label
        minimum_y_neuron = min([min(dict_neurons[i]) for i in range(self.nb_layers)])
        space_neuron_activation = abs(minimum_y_neuron * 1.1 - minimum_y_neuron)
        for i, j in enumerate(self.model.get_config()['layers']):
            activation = j['config']['activation']
            fig.add_annotation(x=i, y=min(dict_neurons[i]) - space_neuron_activation,
                               text=f'{activation}',
                               showarrow=False,
                               yshift=-1)

        plot(fig)
