#%%
import requests
import lxml
from bs4 import BeautifulSoup as bsoup
from bs4.element import Tag


url="https://www.pagina12.com.ar/"

#%%
#Bajamos los datos de la web por metodo http, es basicamente lo que hace un browser
p12=requests.get(url)

#%%
#Resultado del request
p12.status_code

#%%
#texto html de la web

#%%
#Permite ver el contenido de datos que no son textos y son videos o imagenes
p12.content

#%%
#muestra el encabezado de la repuesta, puede ser relevante, COKIES, tipo de datos, info del servidor
p12.headers

#%%
#encabezado de la solicitud, encabezado con el que sale la solicitud, hay paginas que al detectar el user action python los bloquean, por lo que hay que ver el encabezado y cambiarlo.
p12.request.headers

#%%
#metodo de la solicitud
p12.request.method

#%%
#es util ver la URL para ver si un sitio nos redirecciona a otro, y se hace de nuevo la solicitud de forma automatica.
p12.request.url

#%%
#Convierte el requests a un tipo de objeto soup manejado por bs4
# 'html.parser' deberia ser 'lxml' pero no ha funcionado
soup=bsoup(p12.text, 'html.parser')

#%%
#mostramos el soup de forma ordenada como el inspector de los browsers
print(soup.prettify())

#%%
#buscando en la sopa
secciones=soup.find(
    'ul', #trae el primer elemento del tipo ul
    attrs={
        "class":"horizontal-list main-sections hide-on-dropdown"
        }#que coincida con el atributo
    ).find_all(
    "li"
    )#dentro del 'ul' traer todos los 'li'
type(secciones)

#%%
seccion:Tag=secciones[5]
#obtener el link
seccion.find("a"), seccion.a #ambos hacen lo mismo
seccion.a.get("href")
#obtener el texto
seccion.text, seccion.a.get_text() #ambos hacen lo mismo

#%%
# Extraer todas las secciones y subsecciones
links_seccion=[seccion.a.get("href") for seccion in secciones]
sub_seccion_url=links_seccion[2]

#extraer noticias de secciones(subsecciones)
#crear sopa conr equest
subseccion_text=requests.get(sub_seccion_url).text
soup_sebseccion=bsoup(subseccion_text,"html.parser")

articles=soup_sebseccion.find("div", 
                     attrs={
                        "class":"articles-list"
                        }).find_all("div"
                        )
len(articles)