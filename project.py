import streamlit as st
import pandas as pd
import gdown
import numpy as np

# id = 1AXNrSrH6BUVRo4tvUHIVfeuumEBjDCCR
@st.experimental_memo
def download_data():
  #https://drive.google.com/uc?id=YOURFILEID
  url = "https://drive.google.com/uc?id=1AXNrSrH6BUVRo4tvUHIVfeuumEBjDCCR"
  output = 'data.csv'
  gdown.download(url,output,quiet = False)

download_data()
data = pd.read_csv('data.csv', sep = ',')

st.title('CASOS SÍSMICOS')
st.write('Magnitud')
st.line_chart(data, x = 'FECHA_UTC', y = 'MAGNITUD')
print(data)

st.write('Longitud')
st.line_chart(data, x = 'FECHA_UTC', y = 'LONGITUD')
print(data)

#myfile.py
#$ pip install streamlit --upgrade
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import urllib.request 

#URL
url = "https://raw.githubusercontent.com/aname1ba/proyecto/main/Catalogo1960_2021.csv"
datos = pd.read_csv(url, sep=',')

#TITULO
st.title('Sismos en el Perú desde 1960 hasta el 2021 según el IGP')

#INFORMACIÓN
st.write('A nivel mundial, el Perú es uno de los países de mayor potencial sísmico debido a que forma parte del denominado *Cinturón de Fuego del Pacífico*, región donde la Tierra libera más del 85% de la energía acumulada en su interior debido a los procesos de convección del manto.')

st.write('En este contexto, la actividad sísmica en torno de la placa del Pacífico, es debida a los diversos procesos de convergencia de placas con velocidades de hasta 8 cm/año. En América del Sur, en su borde occidental, son las placas de Nazca y Sudamericana las que convergen y desarrollan el proceso de subducción mediante el cual, la placa oceánica de Nazca se introduce por debajo de la continental o Sudamericana. Este proceso es el causante de la geodinámica activa del país y por ende, de una importante actividad sísmica, volcánica y efectos asociados.')





#MAPA
st.subheader('Datos en el mapa')

df_mapa=pd.read_csv('Catalogo1960_2021.csv')
df =  df_mapa.rename(columns={'LATITUD':'lat', 'LONGITUD':'lon'})
st.map(df)

url2= 'https://raw.githubusercontent.com/aname1ba/proyecto/main/2Catalogo1960_2021-lat%26lon%20-%20copia.csv'
df=pd.read_csv(url2)
