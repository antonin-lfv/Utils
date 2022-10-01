import streamlit as st

# Config
st.set_page_config(
    layout="wide",
    page_title="Structure generation",
    menu_items={
        'About': "App made with love by Antonin L"
    },
    page_icon="🏠"
)

st.markdown("""
<style>
.centered_titre {
    font-size:65px !important;
    font-weight: bold;
    box-sizing: border-box;
    text-align: center;
    width: 100%;
}
.text{
    text-align: justify;
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<p class='centered_titre'>3D structure generation</p>",  unsafe_allow_html=True)
st.write("###")
st.markdown("<p class='text'>Bienvenue dans l'application de génération de structures 3D. "
            "Ici, vous pouvez générer une structure depuis la page <b>Generation</b>"
            " et exporter les données en csv.</p>",  unsafe_allow_html=True)
st.markdown("<p class='text'>Vous avez aussi la possibilité d'importer directement les fichiers csv"
            " pour visualiser vos structures depuis la page <b>Visualisation</b>.</p>",  unsafe_allow_html=True)
