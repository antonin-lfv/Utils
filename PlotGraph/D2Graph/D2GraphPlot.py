#  ___    _____
# |__ \  |  __ \
#    ) | | |  | |
#   / /  | |  | |
#  / /_  | |__| |
# |____| |_____/


import plotly.graph_objects as go
from plotly.offline import plot
import pandas as pd


def search_node_from_coord(x, y, nodes):
    """Get node's number from coordinates"""
    return int(nodes.loc[(nodes['x'] == x) & (nodes['y'] == y)]['n'])


def graphe_2d(nodes, edges, titre):
    """Plot graph - with dijkstra path if not none"""
    edge_x_temp, edge_y_temp = [], []
    edge_x, edge_y = [], []
    for row in range(len(edges)):
        edge_x_temp.append(float(nodes[nodes['n'] == float(edges.loc[row][['depart']])]['x']))
        edge_x_temp.append(float(nodes[nodes['n'] == float(edges.loc[row][['arrivee']])]['x']))
        edge_y_temp.append(float(nodes[nodes['n'] == float(edges.loc[row][['depart']])]['y']))
        edge_y_temp.append(float(nodes[nodes['n'] == float(edges.loc[row][['arrivee']])]['y']))

    for i in range(len(edge_x_temp)):
        if i == 0:
            edge_x.append(edge_x_temp[i])
            edge_y.append(edge_y_temp[i])
        elif i % 2 == 0:
            edge_x.append(None)
            edge_y.append(None)
            edge_x.append(edge_x_temp[i])
            edge_y.append(edge_y_temp[i])
        else:
            edge_x.append(edge_x_temp[i])
            edge_y.append(edge_y_temp[i])

    fig = go.Figure()

    # Edges (Arrow)
    for i in range(0, len(edge_x), 3):
        fig.add_annotation(
            ax=edge_x[i],  # départ
            ay=edge_y[i],  # départ
            x=edge_x[i + 1],  # arrivée
            y=edge_y[i + 1],  # arrivée
            xref='x',
            yref='y',
            axref='x',
            ayref='y',
            text='',  # if you want only the arrow
            showarrow=True,
            arrowhead=3,
            arrowsize=1,
            arrowwidth=1,
            arrowcolor='grey',
            opacity=0.3
        )

    node_x, node_y, num_node = nodes['x'].to_list(), nodes['y'].to_list(), nodes['n'].to_list()

    # traçage des noeuds
    fig.add_scatter(
        x=node_x, y=node_y,
        mode='markers',
        hoverinfo='text+x+y',
        text=num_node,
        name="",
        hovertemplate="noeud n°%{text}<br>" + "x: %{x}<br>" + "y: %{y}<br>",
        marker=dict(
            color='red',
            size=8,
            line_width=1))

    fig.update_layout(
        title=titre,
        font=dict(
            size=15,
            color="Black"),
        titlefont_size=16,
        showlegend=False,
        hovermode='closest',
        xaxis=dict(showgrid=False, zeroline=False,
                   showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False,
                   showticklabels=False),
        autosize=False,
        width=1200, height=650,
        margin=dict(l=40, r=50, b=40, t=40),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
    )

    return fig
