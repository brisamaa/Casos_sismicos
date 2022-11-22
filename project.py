import streamlit as st
import pandas as pd
import gdown

# id = 1AXNrSrH6BUVRo4tvUHIVfeuumEBjDCCR
@st.experimental_memo
def download_data():
  #https://drive.google.com/uc?id=YOURFILEID
  url = "https://drive.google.com/uc?id=1AXNrSrH6BUVRo4tvUHIVfeuumEBjDCCR"
  output = 'data.csv'
  gdown.download(url,output,quiet = False)

download_data()
data = pd.read_csv('data.csv', sep = ';', nrows = 1000000, parse_dates = ['FECHA_UTC','FECHA_CORTE'])
st.dataframe(data.head(50))
magnitud = data['MAGNITUD']
st.line_chart(magnitud)
