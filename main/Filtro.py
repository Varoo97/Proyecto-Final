import base64
import streamlit as st
import plotly.express as px
import streamlit as st
import pandas as pd
import pylab as plt
from PIL import Image
import webbrowser
import urllib.request

df = px.data.iris()

@st.experimental_memo
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("MC.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://static.vecteezy.com/system/resources/thumbnails/006/423/395/small/light-blue-gradient-blur-background-vector.jpg");
background-size: 180%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)


import pandas as pd




recetas = pd.read_csv('../recetas_uno.csv')

df = pd.read_csv('../recetas.csv')

st.title('LA NEVERA INTELIGENTE')

st.header('¿Cansado de llegar a tu nevera y no saber que preparar con los ingredientes que tienes a mano?') 

st.image('https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/como-almacenar-colocar-alimentos-nevera-1626171839.gif')

st.write('#### ¡Pues eso se ha acabado! Con nuestra nevera inteligente podrás decirle los ingredientes de los que dispones y ella misma te dirá las recetas que puedes realizar')

st.write("Las recetas han sido sacadas de 'Monsieur Cuisine', la thermomix del Lidl")

st.image('https://s03.s3c.es/imag/_v0/770x420/8/c/a/Monsieur-cuisine-Connect.jpg')

st.caption('### Para más información')
url = 'https://fr.monsieur-cuisine.com/es/recetas'
if st.button('Monsieur Cuisine Web'):
    webbrowser.open_new_tab(url)




st.subheader('Selecciona los ingredientes')





columnas = df.columns
selection = st.multiselect('Ingredientes', columnas)

re = selection
if len(re) == 2:
    re.append('Título')
    re.append('Duración')
    re.append('Dificultad')
    re.append('link_recetas')
    st.dataframe(df[re][(df[re][re[0]] == 1) & (df[re][re[1]] == 1)][['Título','Duración','Dificultad','link_recetas']])
    
    
elif len(re) == 1:
    re.append('Título')
    re.append('Duración')
    re.append('Dificultad')
    re.append('link_recetas')
    st.dataframe(df[re][df[re][re[0]] == 1][['Título','Duración','Dificultad','link_recetas']])
    
elif len(re) == 3:
    re.append('Título')
    re.append('Duración')
    re.append('Dificultad')
    re.append('link_recetas')
    st.dataframe(df[re][(df[re][re[0]] == 1) & (df[re][re[1]] == 1) & (df[re][re[2]] == 1)][['Título','Duración','Dificultad','link_recetas']])
    
    
elif len(re) == 4:
    re.append('Título')
    re.append('Duración')
    re.append('Dificultad')
    re.append('link_recetas')
    st.dataframe(df[re][(df[re][re[0]] == 1) & (df[re][re[1]] == 1) & (df[re][re[2]] == 1) & (df[re][re[3]] == 1)]     [['Título','Duración','Dificultad','link_recetas']])
    

st.caption('# Siguientes pasos del proyecto')
st.write('Filtrar por tipo de alimento y valores nutricionales')
st.write('Realizar el mismo proceso, pero añadiendole reconocimiento de imagenes')




