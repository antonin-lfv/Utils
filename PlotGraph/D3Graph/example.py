from PlotGraph.D3Graph.D3GraphPlot import *

# Data
node_csv_3D = pd.read_csv('data/neouds_3D.csv', sep=';')
edge_csv_3D = pd.read_csv('data/aretes_3D.csv', sep=';')
# Plot
fig_3D = graphe_3d(nodes=node_csv_3D, edges=edge_csv_3D, showEdges=True)
plot(fig_3D)
