import unittest
import datetime
import xml.etree.ElementTree as gfg
from lxml import html


def iter_html(html,parent=None):
    if parent is None:
        parent = gfg.Element("html")
    for tag in html.iterchildren():
        data = gfg.Element(tag.tag)
        data.text = tag.text
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




class TestCreateXML(unittest.TestCase):
    def test_create_xml_bloomberg_upsert(self):
        empresa = "Bloomberg"
        titulo = "Título de prueba"
        fecha = datetime.datetime(2021, 1, 1, 0, 0, 0)
        idioma = "Español"
        link = "https://www.example.com"
        company = "ABC:Company Name"
        action = "UPSERT Bloomberg"
        contenido = "<p>Contenido de prueba</p>"

        expected_result = '<item><type>ARTICLE</type><action>UPSERT</action><guid /><pubDate>Thu, 01 Jan 2021 00:00:00 GMT</pubDate><title>Título de prueba</title><htmltext><p>Contenido de prueba</p></htmltext><links><link type="html" mime="text/html">https://www.example.com</link></links><language>ES</language><country>MX</country><agency>Miranda Newswire</agency><companies><company name="Company Name" /><isin>ABC</isin></companies></item>'.encode()
        result = create_xml(empresa, titulo, fecha, idioma, link, company, action, contenido)

        self.assertEqual(result, expected_result)

    def test_create_xml_refinitiv_create(self):
        empresa = "Refinitiv"
        titulo = "Título de prueba"
        fecha = datetime.datetime.now()
        idioma = "Español"
        link = "https://www.example.com"
        company = "ABC:Company Name"
        action = "CREATE Refinitiv"
        contenido = "<p>Contenido de prueba</p>"

        expected_result = '<item><type>ARTICLE</type><action>CREATE</action><guid /><pubDate>{}</pubDate><title>{}</title><htmltext><p>Contenido de prueba</p></htmltext><language>ES</language><country>MX</country><agency>Miranda Newswire</agency><companies><company name="Company Name" /><isin>ABC</isin></companies></item>'.format(fecha.strftime("%a, %d %b %Y %H:%M:%S GMT"), titulo).encode()

        result = create_xml(empresa, titulo, fecha, idioma, link, company, action, contenido)

        self.assertEqual(result.decode(), expected_result)

if __name__ == '__main__':
    unittest.main()
