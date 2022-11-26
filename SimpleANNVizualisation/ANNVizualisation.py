import itertools
import networkx as nx
from plotly.offline import plot
import plotly.graph_objects as go


class NeuralNetworkPlot:
    def __init__(self, *, layers_list=None):
        """
        :param layers_list: Liste contenant le nombre de neurones par couche
        exemple : [2, 3, 1] pour 2 entrées, 3 neurones dans la couche cachée et 1 neurone en sortie
        """
        if layers_list is None:
            layers_list = [5, 9, 4, 3, 21, 4, 4, 3]
        self.layers_list = layers_list[::-1]
        self.graph = self.multilayered_graph()

    def multilayered_graph(self):
        """
        Création du réseau avec networkx
        :return: le graphe
        """
        extents = nx.utils.pairwise(itertools.accumulate((0,) + tuple(self.layers_list)))
        layers = [range(start, end) for start, end in extents]
        G = nx.Graph()
        for (i, layer) in enumerate(layers):
            G.add_nodes_from(layer, layer=i)
        for layer1, layer2 in nx.utils.pairwise(layers):
            G.add_edges_from(itertools.product(layer1, layer2))
        return G

    @classmethod
    def get_yi_from_layerNumber(cls, *, i, NumberOfNeuronsInLayer, DistanceBetweenNeurons=1):
        """Retourne l'ordonnée du neurone numéro i sachant que le neurone du milieu est en x=0
        et que le nombre de neurones dans la couche est NumberOfNeuronsInLayer
        :param i: numéro du neurone dans le layer en partant du bas, commence à 0
        :param NumberOfNeuronsInLayer: nombre de neurones dans le layer
        :param DistanceBetweenNeurons: distance entre deux neurones de la même couche
        """
        assert 0 <= i < NumberOfNeuronsInLayer
        return (i - NumberOfNeuronsInLayer / 2) * DistanceBetweenNeurons

    def get_layer_from_neuronIndex(self, *, value):
        """
        Retourne l'index du layer dans lequel se trouve le neurone d'index 'value'
        :param value: index du neurone
        :return: index du layer
        """
        accumulated_layers_list = list(itertools.accumulate(self.layers_list))
        for index, val in enumerate(accumulated_layers_list):
            if value < val:
                return index
        return None

    def plot_neural_network(self, display=True):
        """
        Création du graphe avec plotly
        :param display: affiche le graphe si True sinon retourne l'objet graph_objects de plotly
        :return: plotly graph_objects si display=False
        """
        # ===== Nodes ===== #
        node_x = []
        node_y = []
        for node in self.graph.nodes():
            x, y = self.graph.nodes[node]['layer'], self.get_yi_from_layerNumber(
                i=node - sum(self.layers_list[:self.get_layer_from_neuronIndex(value=node)]),
                NumberOfNeuronsInLayer=self.layers_list[self.graph.nodes[node]['layer']])
            node_x.append(x)
            node_y.append(y)

        node_trace = go.Scatter(
            x=node_y, y=node_x,
            mode='markers',
            marker=dict(
                size=5,
                color='black')
        )

        # ===== Edges ===== #
        edge_x = []
        edge_y = []
        for edge in self.graph.edges():
            x0, y0 = self.graph.nodes[edge[0]]['layer'], self.get_yi_from_layerNumber(
                i=edge[0] - sum(self.layers_list[:self.get_layer_from_neuronIndex(value=edge[0])]),
                NumberOfNeuronsInLayer=self.layers_list[self.graph.nodes[edge[0]]['layer']])
            x1, y1 = self.graph.nodes[edge[1]]['layer'], self.get_yi_from_layerNumber(
                i=edge[1] - sum(self.layers_list[:self.get_layer_from_neuronIndex(value=edge[1])]),
                NumberOfNeuronsInLayer=self.layers_list[self.graph.nodes[edge[1]]['layer']])
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])

        edge_trace = go.Scatter(
            x=edge_y, y=edge_x,
            line=dict(width=0.4, color='#888'),
            mode='lines')

        fig = go.Figure(data=[edge_trace, node_trace],
                        layout=go.Layout(
                            margin=dict(b=20, l=5, r=5, t=40),
                            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                            paper_bgcolor='rgba(0,0,0,0)',
                            showlegend=False
                        )
                        )
        if display:
            plot(fig)
        else:
            return fig
