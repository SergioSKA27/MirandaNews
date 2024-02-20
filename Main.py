import streamlit as st

st.set_page_config(page_title="Miranda Newswire", page_icon="app/static/favicon.jpg", layout="wide")
st.markdown("""
<style>
    #MainMenu, header {visibility: hidden;}
    .bg {
        background-image: linear-gradient(260deg, #002354 0%, #1F4B9E 100%);
		opacity: 0.95;
        bottom:0;
        left:-50%;
        position:fixed;
        right:-50%;
        top:0;
        z-index:0;
        background-size: cover;
        background-position: center center;
        width: 149%;
        height: 100%;
    }
</style>
<div class="bg"></div>
""", unsafe_allow_html=True)

with open("app/static/logo.png", "rb") as image_file:
    st.image(image_file.read(),width=400)

st.divider()
empresa = st.selectbox("Empresa:", ["Seleccione","Bloomberg","Refinitiv"])
titulo = st.text_input("Título:")

fecha = st.date_input("Fecha:")

idioma = st.selectbox("Idioma:", ["Seleccione","Inglés","Español"])

link = st.text_input("Link:")

codes = """
<option value="MXP000511016:Alfa">Alfa</option>
<option value="MXP001391012:Alsea">Alsea</option>
<option value="MX01KO000002:Coca-Cola FEMSA">Coca-Cola FEMSA</option
><option value="MX01CO0U0028:Cox Energy America">Cox Energy America</option>
<option value="MX01CU010003:Cuervo">Cuervo</option>
<option value="MXFHFH020001:Fhipo">Fhipo</option>
<option value="MXCFFU000001:Fibra Uno">Fibra Uno</option>
<option value="MXP495211262:Grupo Bimbo S.A.B. de C.V.">Grupo Bimbo S.A.B. de C.V.</option>
<option value="MX01HC000001:Hoteles City Express">Hoteles City Express</option>
<option value="USP36035AB29:Mexarrend">Mexarrend</option>
<option value="MXFFFE0K0006:Mexico Infrastructure Partners">Mexico Infrastructure Partners F1 SAPI de CV</option>
<option value="MX01OM000018:OMA">OMA</option>
<option value="USP73699BH55:Operadora de Servicios Mega">Operadora de Servicios Mega</option>
<option value="MX01AG050009:Rotoplas">Rotoplas</option>
<option value="MXCFTE0B0005:Terrafina">Terrafina</option>
<option value="MX01TR0H0006:Traxion">Traxion</option>
<option value="MX00UN000002:Unifin">Unifin</option>
<option value="MX01VI050002:Vinte">Vinte</option>
"""

dicval = {"Alfa":"MXP000511016:Alfa",
        "Alsea":"MXP001391012:Alsea",
        "Coca-Cola FEMSA":"MX01KO000002:Coca-Cola FEMSA",
        "Cox Energy America":"MX01CO0U0028:Cox Energy America",
        "Cuervo":"MX01CU010003:Cuervo",
        "Fhipo":"MXFHFH020001:Fhipo",
        "Fibra Uno":"MXCFFU000001:Fibra Uno",
        "Grupo Bimbo S.A.B. de C.V.":"MXP495211262:Grupo Bimbo S.A.B. de C.V.",
        "Hoteles City Express":"MX01HC000001:Hoteles City Express",
        "Mexarrend":"USP36035AB29:Mexarrend",
        "Mexico Infrastructure Partners F1 SAPI de CV":"MXFFFE0K0006:Mexico Infrastructure Partners",
        "OMA":"MX01OM000018:OMA",
        "Operadora de Servicios Mega":"USP73699BH55:Operadora de Servicios Mega",
        "Rotoplas":"MX01AG050009:Rotoplas",
        "Terrafina":"MXCFTE0B0005:Terrafina",
        "Traxion":"MX01TR0H0006:Traxion",
        "Unifin":"MX00UN000002:Unifin",
        "Vinte":"MX01VI050002:Vinte"}

company = st.selectbox("Compañía:", ["Seleccione"]+list(dicval.keys()))

action = st.selectbox("Acción:", ["Seleccione",'Upsert Bloomberg','Delete Bloomberg','CREATE Refinitiv','UPDATE Refinitiv','DELETE Refinitiv'])



st.text_area("Cuerpo:", height=200)

if st.button("Enviar",use_container_width=True):
    pass
