import plotly.graph_objects as go
from plotly.offline import plot


def __zprime(matrix):
    l = []
    for j in reversed(range(25)):
        for i in reversed(range(25)):
            l.append((matrix[i])[j])
    return l

def __data_array(mat):
    c = []
    for i in range(25):
        for j in range(25):
            c.append(i)
            c.append(j)
            c.append(mat[i][j])
    M = np.asarray(c)
    M = M.reshape((25 * 25, 3))
    return M

############
fig = go.Figure()
mat = z_data.values
xp = [i for i in reversed(range(0, 25))]
yl = [i for i in reversed(range(0, 25))]
# make the plot
for i in range(0, 25):
    yp = [i] * 25
    zi = mat[i]
    for j in reversed(range(0, 25)):
        xl = [j] * 25
        ziprime = __zprime(mat)[(j * 25):(j * 25 + 25)]
        fig.add_scatter3d(x=xp, y=yp, z=zi, line=dict(width=1, color='blue'), mode='lines', showlegend=False)
        fig.add_scatter3d(x=xl, y=yl, z=ziprime, line=dict(width=1, color='red'), mode='lines', showlegend=False)

fig.update_layout(
    template='simple_white',
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
)
plot(fig)
############









import plotly.figure_factory as ff
############
mat = z_data.values
fig = go.Figure()
fig.add_surface(z=Z, colorscale='earth')
fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                  highlightcolor="limegreen", project_z=True))
fig.update_layout(
    template='simple_white',
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
)
plot(fig)
############










