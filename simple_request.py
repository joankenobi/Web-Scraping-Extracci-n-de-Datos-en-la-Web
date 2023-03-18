#%%
import requests

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