# Generation page
import streamlit as st
from utils.fonctions import *

st.set_page_config(page_icon="🤖",
                   layout="wide",
                   )


def convert_df(df):
    # pandas to csv
    return df.to_csv().encode("utf-8")


# Data
node_columns = ["n", "x", "y", "z"]
edge_columns = ["depart", "arrivee"]
if "node_csv_3D" not in st.session_state.keys():
    st.session_state["node_csv_3D"] = []
if "edge_csv_3D" not in st.session_state.keys():
    st.session_state["edge_csv_3D"] = []

# SideBar
st.sidebar.title("Vos données")
st.sidebar.subheader("Points")
node_data_show = st.sidebar.empty()
st.sidebar.subheader("Arêtes")
edge_data_show = st.sidebar.empty()
st.sidebar.write("---")
button_export_points = st.sidebar.empty()
button_export_edges = st.sidebar.empty()
export_caption = st.sidebar.empty()
button_delete = st.sidebar.empty()
st.sidebar.caption("Pour supprimer les données, appuyer deux fois")
st.sidebar.write("###")

# Layout
if not st.session_state["node_csv_3D"]:
    st.info("La structure s'affichera ici après l'ajout de vos données")
    st.write("###")
else:
    st.subheader("Votre structure")
graphe_zone = st.empty()
col1, col2 = st.columns(2)

# Forms
with col1:
    with st.form("Ajouter un point", clear_on_submit=False):
        st.subheader("Ajouter un point")
        index = st.number_input("index", min_value=0, step=1)
        x_val = st.number_input("x")
        y_val = st.number_input("y")
        z_val = st.number_input("z")

        submitted = st.form_submit_button("Submit")
        if submitted:
            if index in [st.session_state["node_csv_3D"][i][0] for i in range(len(st.session_state["node_csv_3D"]))]:
                st.error(f"L'index {index} est déjà utilisé !")
            else:
                st.session_state["node_csv_3D"].append([index, x_val, y_val, z_val])
                st.success(f"Le point numéro {index} a été ajouté !")
    with st.form("Supprimer un point", clear_on_submit=False):
        st.subheader("Supprimer un point")
        index = st.number_input("index", min_value=0, step=1)

        submitted = st.form_submit_button("Submit")
        if submitted:
            if index in [st.session_state["node_csv_3D"][i][0] for i in range(len(st.session_state["node_csv_3D"]))]:
                # delete all edges with this index as depart or arrivee
                for i in range(len(st.session_state["edge_csv_3D"])):
                    if index in st.session_state["edge_csv_3D"][i]:
                        st.session_state["edge_csv_3D"].remove(st.session_state["edge_csv_3D"][i])
                st.session_state["node_csv_3D"].remove([index, x_val, y_val, z_val])
                st.success(f"Le point numéro {index} a été supprimé !")
                st.write(st.session_state["node_csv_3D"])
            else:
                st.error(f"L'index {index} n'existe pas !")

with col2:
    with st.form("Ajouter une arete", clear_on_submit=False):
        st.subheader("Ajouter une arete")
        point1 = st.number_input("index du premier point", min_value=0, step=1)
        point2 = st.number_input("index du deuxième point", min_value=0, step=1)

        submitted = st.form_submit_button("Submit")
        if submitted:
            lstIndex = [st.session_state["node_csv_3D"][i][0] for i in range(len(st.session_state["node_csv_3D"]))]
            if point1 in lstIndex and point2 in lstIndex:
                if point1 != point2:
                    st.session_state["edge_csv_3D"].append([point1, point2])
                    st.success(f"L'arete entre le point {point1} et {point2} a été ajoutée !")
                else:
                    st.error(f"Vous essayez de connecter un point à lui même")
            else:
                st.error(f"Vous essayez de connecter des points qui ne sont pas créés")
    with st.form("Supprimer une arete", clear_on_submit=False):
        st.subheader("Supprimer une arete")
        point1 = st.number_input("index du premier point", min_value=0, step=1)
        point2 = st.number_input("index du deuxième point", min_value=0, step=1)

        submitted = st.form_submit_button("Submit")
        if submitted:
            if [point1, point2] in st.session_state["edge_csv_3D"]:
                st.session_state["edge_csv_3D"].remove([point1, point2])
                st.success(f"L'arete entre le point {point1} et {point2} a été supprimée !")
            else:
                st.error(f"Vous essayez de supprimer une arete qui n'existe pas")


# display graph
def display_graphe():
    if st.session_state["node_csv_3D"]:
        node_csv_3D = pd.DataFrame(st.session_state["node_csv_3D"], columns=node_columns)
        edge_csv_3D = pd.DataFrame(st.session_state["edge_csv_3D"], columns=edge_columns)
        edges_bool = (st.session_state["edge_csv_3D"] != [])
        graphe_zone.plotly_chart(graphe_3d(nodes=node_csv_3D, edges=edge_csv_3D, showEdges=edges_bool),
                                 use_container_width=True)


display_graphe()

# display data in sidebar
node_data_show.dataframe(pd.DataFrame(st.session_state["node_csv_3D"], columns=node_columns),
                         use_container_width=True)
edge_data_show.dataframe(pd.DataFrame(st.session_state["edge_csv_3D"], columns=edge_columns),
                         use_container_width=True)

if st.session_state["node_csv_3D"]:
    button_export_points.download_button(label="Exporter les points en csv",
                                         data=convert_df(
                                             pd.DataFrame(st.session_state["node_csv_3D"], columns=node_columns)),
                                         file_name="node_csv_3D",
                                         mime='text/csv')

if st.session_state["edge_csv_3D"]:
    button_export_edges.download_button(label="Exporter les aretes en csv",
                                        data=convert_df(
                                            pd.DataFrame(st.session_state["edge_csv_3D"], columns=edge_columns)),
                                        file_name="edge_csv_3D",
                                        mime='text/csv')

if st.session_state["node_csv_3D"] or st.session_state["edge_csv_3D"]:
    export_caption.caption("Télécharger les données en csv")

if button_delete.button("Tout effacer"):
    for key in st.session_state.keys():
        del st.session_state[key]
