import plotly.graph_objects as go
from plotly.offline import plot
import numpy as np
from fastdist import fastdist
from CirclesIntersection.CirclesIntersect import solve_inter_circles


class ConstPlotly:
    xaxis = dict(showgrid=False, zeroline=False,
                 showticklabels=False)
    yaxis = dict(showgrid=False, zeroline=False,
                 showticklabels=False)
    transparent_color = 'rgba(0,0,0,0)'


def distance_eucl(x: list, y: list) -> float:
    """
    Distance euclidienne entre 2 vecteurs
    """
    return round(fastdist.euclidean(np.array(x), np.array(y)), 3)


""" Structure de l'ensemble des n Points -> Matrice d'adjacence (list of lists)
La cellule de coordonnées (i,j) donne la distance entre le point d'indice i et j
"""


def plotPoints(Points):
    fig = go.Figure()
    # Création des points
    points_x = []
    points_y = []
    points_index = []
    # index des neurones existants
    for pts in Points[:]:
        if Points.index(pts) == 0:
            # 1er point à placer
            points_x.append(0)
            points_y.append(0)
            points_index.append(0)
        elif Points.index(pts) == 1:
            # 2e point à placer par rapport au premier
            points_x.append(Points[0][1])
            points_y.append(0)
            points_index.append(1)
        else:
            # jème point à placer par rapport aux j-1 premiers,
            # intersection de j-1 cercles
            x, y = solve_inter_circles(points_x,
                                       points_y,
                                       [Points[Points.index(pts)][j] for j in range(Points.index(pts))])
            points_x.append(x)
            points_y.append(y)
            points_index.append(Points.index(pts))

    fig.add_scatter(x=points_x, y=points_y, mode='markers+text', text=points_index,
                    hovertemplate="<b>%{text}</b><extra></extra>", textposition="bottom center",
                    textfont=dict(
                        size=10,
                    ),
                    marker=dict(
                        color='black'
                    ))

    fig.update_layout(
        xaxis=ConstPlotly.xaxis,
        yaxis=ConstPlotly.yaxis,
        paper_bgcolor=ConstPlotly.transparent_color,
        plot_bgcolor=ConstPlotly.transparent_color,
        showlegend=False
    )
    plot(fig)
