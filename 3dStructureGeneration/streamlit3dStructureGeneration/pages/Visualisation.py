# Generation page
import streamlit as st
from utils.fonctions import *

st.set_page_config(page_icon="👁",
                   layout="wide",
                   )

node_columns = ["n", "x", "y", "z"]
edge_columns = ["depart", "arrivee"]

st.sidebar.write("###")
st.sidebar.title("Saisir les données")
points_upload = st.sidebar.file_uploader(label="Choisir le fichier des points",
                                         type=["csv"],
                                         help="Fichier csv avec les colonnes n; x; y; z")
edges_upload = st.sidebar.file_uploader(label="Choisir le fichier des arêtes (optionnel)",
                                        type=["csv"],
                                        help="Fichier csv avec les colonnes depart; arrivee")

if (points_upload and edges_upload) or points_upload:
    try:
        st.subheader("Votre structure")
        edges_bool, edge_csv_3D = False, None
        node_csv_3D = pd.read_csv(points_upload, engine='python', sep=";")
        node_csv_3D.columns = node_columns
        if edges_upload:
            edge_csv_3D = pd.read_csv(edges_upload, engine='python', sep=";")
            edge_csv_3D.columns = edge_columns
            edges_bool = True
        st.plotly_chart(graphe_3d(nodes=node_csv_3D, edges=edge_csv_3D, showEdges=edges_bool),
                        use_container_width=True)
        with st.expander("Raw data"):
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Points")
                st.dataframe(node_csv_3D, use_container_width=True)
            if edges_upload:
                with col2:
                    st.subheader("Arêtes")
                    st.dataframe(edge_csv_3D, use_container_width=True)
    except:
        st.error("Vos fichiers ne correspondent pas au format attendu")
elif edges_upload and not points_upload:
    st.warning("Il faut ajouter des points !")
else:
    st.write("###")
    st.write("###")
    st.write("###")
    st.info("La structure s'affichera ici après l'ajout de vos données")
