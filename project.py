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
data = pd.read_csv('data.csv', sep = ',')

st.title('Sismos')
st.write('Sismos')
#st.dataframe(data.head(50))
#magnitud = data['MAGNITUD']
st.line_chart(data, x = 'FECHA_UTC', y = 'MAGNITUD')
print(data)
