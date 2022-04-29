from PlotGraph.D2Graph.D2GraphPlot import *

# Data
node_csv_2d = pd.read_csv('data/noeuds_2D.csv', sep=';')
edge_csv_2d = pd.read_csv('data/aretes_2D.csv', sep=';')
# Plot
fig_2D = graphe_2d(nodes=node_csv_2d, edges=edge_csv_2d, titre="myTitle")
plot(fig_2D)