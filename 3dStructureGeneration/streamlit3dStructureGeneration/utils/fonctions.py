import plotly.graph_objects as go
from plotly.offline import plot
import pandas as pd

# Code from https://github.com/antonin-lfv/Utils/blob/main/PlotGraph/D3Graph/D3GraphPlot.py


def graphe_3d(nodes, edges, showEdges=True):
    """Plot graph"""

    data = []

    # ===== edges
    if showEdges:
        edge_x_temp, edge_y_temp, edge_z_temp = [], [], []
        edge_x, edge_y, edge_z = [], [], []
        for row in range(len(edges)):
            edge_x_temp.append(float(nodes[nodes['n'] == float(edges.loc[row][['depart']])]['x']))
            edge_x_temp.append(float(nodes[nodes['n'] == float(edges.loc[row][['arrivee']])]['x']))
            edge_y_temp.append(float(nodes[nodes['n'] == float(edges.loc[row][['depart']])]['y']))
            edge_y_temp.append(float(nodes[nodes['n'] == float(edges.loc[row][['arrivee']])]['y']))
            edge_z_temp.append(float(nodes[nodes['n'] == float(edges.loc[row][['depart']])]['z']))
            edge_z_temp.append(float(nodes[nodes['n'] == float(edges.loc[row][['arrivee']])]['z']))

        for i in range(len(edge_x_temp)):
            if i == 0:
                edge_x.append(edge_x_temp[i])
                edge_y.append(edge_y_temp[i])
                edge_z.append(edge_z_temp[i])
            elif i % 2 == 0:
                edge_x.append(None)
                edge_y.append(None)
                edge_z.append(None)
                edge_x.append(edge_x_temp[i])
                edge_y.append(edge_y_temp[i])
                edge_z.append(edge_z_temp[i])
            else:
                edge_x.append(edge_x_temp[i])
                edge_y.append(edge_y_temp[i])
                edge_z.append(edge_z_temp[i])

        edge_trace = go.Scatter3d(
            x=edge_x, y=edge_y, z=edge_z,
            line=dict(color='#000000'),
            hoverinfo='none',
            mode='lines')

        data.append(edge_trace)

    # ===== nodes
    node_x, node_y, node_z = nodes['x'].to_list(), nodes['y'].to_list(), nodes['z'].to_list()

    node_trace = go.Scatter3d(
        x=node_x, y=node_y, z=node_z,
        text=nodes['n'].to_list(),
        mode='markers',
        hovertemplate='Coord: (%{x};%{y};%{z})<br>Index: %{text}',
        marker=dict(
            color='black',
            size=5),
        name="")

    data.append(node_trace)

    # affichage
    fig = go.Figure(data=data,
                    layout=go.Layout(
                        showlegend=False,
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        autosize=True,
                        margin=dict(r=50),
                    )
                    )

    fig.update_scenes(
        xaxis_visible=False,
        yaxis_visible=False,
    )

    return fig
