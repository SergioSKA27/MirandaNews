import streamlit as st
from st_tiny_editor import  tiny_editor
from streamlit.components.v1 import html as render_html
import xml.etree.ElementTree as gfg
from lxml import html
import datetime

#Terminar de implementar el código de las pruebas unitarias

st.set_page_config(page_title="Miranda Newswire", page_icon="app/static/favicon.jpg", layout="wide")
st.markdown("""
<style>
    #MainMenu, header {visibility: hidden;}
    button[title="View fullscreen"]{
    visibility: hidden;}
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
    iframe {
        border: 1px;
        border-radius: 15px;
    }
</style>
<div class="bg"></div>
""", unsafe_allow_html=True)



def iter_html(html, parent=None):
    """
    Recursively iterates over an HTML element and its children, creating a new HTML element tree.

    Parameters:
        html (Element): The HTML element to iterate over.
        parent (Element, optional): The parent element to append the new elements to. Defaults to None.

    Returns:
        None
    """
    if parent is None:
        parent = gfg.Element("html")
    for tag in html.iterchildren():
        data = gfg.Element(tag.tag)
        data.text = tag.text
        if len(tag.attrib) > 0:
            data.attrib = dict(tag.attrib)
        parent.append(data)
        iter_html(tag,data)
    return parent

def create_xml(empresa,titulo,fecha,idioma,link,company,action,contenido):
    xml = gfg.Element("item")
    ttype = gfg.Element("type")
    xml.append(ttype)
    ttype.text = "ARTICLE"
    if empresa == "Bloomberg":
        if action == "UPSERT Bloomberg":
            ac = gfg.Element("action")
            xml.append(ac)
            ac.text = "UPSERT"
        elif action == "DELETE Bloomberg":
            ac = gfg.Element("action")
            xml.append(ac)
            ac.text = "DELETE"
    elif empresa == "Refinitiv":
        if action == "CREATE Refinitiv":
            ac = gfg.Element("action")
            xml.append(ac)
            ac.text = "CREATE"
        elif action == "UPDATE Refinitiv":
            ac = gfg.Element("action")
            xml.append(ac)
            ac.text = "UPDATE"
        elif action == "DELETE Refinitiv":
            ac = gfg.Element("action")
            xml.append(ac)
            ac.text = "DELETE"
    guid = gfg.Element("guid")
    xml.append(guid)
    guid.text = 'urn:uuid:1225c695-cfb8-4ebb-aaaa-80da344efa6a'
    pubdate = gfg.Element("pubDate")
    pubdate.text = fecha.strftime("%a, %d %b %Y %H:%M:%S GMT")
    xml.append(pubdate)
    title = gfg.Element("title")
    xml.append(title)
    title.text = titulo
    htmll = gfg.Element("htmltext")
    xml.append(htmll)


    content = html.fromstring(contenido)

    iter_html(content,htmll)
    if empresa == "Bloomberg":
        if action == "UPSERT Bloomberg":
            linkk = gfg.Element("links")
            xml.append(linkk)
            li = gfg.Element("link")
            linkk.append(li)
            li.text = link
            li.attrib = {'type':'html','mime':'text/html'}


    lang = gfg.Element("language")
    xml.append(lang)
    lang.text = 'ES' if idioma == "Español" else 'EN'
    country = gfg.Element("country")
    xml.append(country)
    country.text = 'MX'
    agency = gfg.Element("agency")
    xml.append(agency)
    agency.text = "Miranda Newswire"
    compans = gfg.Element("companies")
    xml.append(compans)
    com = gfg.Element("company")
    compans.append(com)
    compp = company.split(":")
    com.attrib = {'name':compp[1]}
    isn = gfg.Element("isin")
    compans.append(isn)
    isn.text = compp[0]


    return gfg.tostring(xml)






with open("app/static/logo.png", "rb") as image_file:
    st.image(image_file.read(),width=400)

st.divider()

c1 = st.columns(2)
empresa = c1[0].selectbox("Empresa:", ["Seleccione","Bloomberg","Refinitiv"])
action = c1[1].selectbox("Acción:", ["Seleccione",'UPSERT Bloomberg','DELETE Bloomberg','CREATE Refinitiv','UPDATE Refinitiv','DELETE Refinitiv'])


c2 = st.columns(2)

c3 = st.columns(2)
fecha = c3[0].date_input("Fecha:",value=datetime.datetime.now())

hora = c3[1].time_input("Hora:")

titulo = st.text_input("Título:")

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


company = c2[0].selectbox("Compañía:", ["Seleccione"]+list(dicval.keys()))
idioma = c2[1].selectbox("Idioma:", ["Seleccione","Inglés","Español"])



d = tiny_editor(st.secrets["TINY_API_KEY"],
    height=600,
    toolbar = 'undo redo | blocks fontfamily fontsize | bold italic underline strikethrough | link image media table | align lineheight | numlist bullist indent outdent | emoticons charmap | removeformat',
    plugins = ["advlist", "anchor", "autolink", "charmap", "code",
        "help", "image", "insertdatetime", "link", "lists", "media",
        "preview", "searchreplace", "table", "visualblocks", "accordion",'emoticons']
)


style = """
<style>
    body {
        background-color: #f0f2f6;
        font-family: sans-serif;

    }
</style>"""

cols = st.columns([0.8,0.2])

if cols[1].button("Preview",use_container_width=True,help='Vista previa del artículo.' if  d is not None and d != "" else 'Ingrese el contenido del artículo.'):
    if d is not None and d != "":
        st.markdown('<h3 style="color: #ffffff;"> Preview </h3>', unsafe_allow_html=True)
        st.divider()
        render_html(style+d, height=400,scrolling=True)


dis =(empresa == "Seleccione" or titulo == "" or fecha == "" or idioma == "Seleccione" or link == "" or company == "Seleccione" or action == "Seleccione" or d == "" or d is None)

if cols[0].button("Enviar",use_container_width=True,
help='Enviar el artículo a la plataforma de noticias.' if  not dis else 'Complete los campos para enviar el artículo.',
disabled=dis):
    dat = datetime.datetime.combine(fecha,hora)
    xml = create_xml(empresa,titulo,dat,idioma,link,dicval[company],action,d)
    today = datetime.date.today().strftime("%a, %d %b %Y %H:%M:%S GMT")
    st.download_button('Descargar XML', xml, f"newswire_{today.replace(' ','_')}.xml", "xml",use_container_width=True)
    st.balloons()
