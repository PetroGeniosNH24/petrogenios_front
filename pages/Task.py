import os
import streamlit as st
import base64
import json
import requests
from config.config import URL_BACKEND, HEADER_DATABRICK

BASE_PATH = '.'


def simplificator():
    
    img_favicon = os.path.join(BASE_PATH,'resources','favicon_bluetab.png')
    img_bluetab = os.path.join(BASE_PATH,'resources','bluetab.png')
    
    st.set_page_config(page_title='Hackaton',layout='wide',page_icon=img_favicon)
    
    st.markdown("""
        <style>
               .block-container {
                    padding-top: 2.2rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """, unsafe_allow_html=True)            
                   
    st.header('BlueTaskCreator')
    
    text = st.text_area("¿Qué tareas quieres organizar?")

    simplified = ''
    promt = "text"

    if st.button('Task Creator',type='primary'):  
        simplified = requests.post(f"{URL_BACKEND}/simplificator/task", headers=HEADER_DATABRICK, data=json.dumps({"text":text})).json().get("message")
    
    with st.container(border=True):
        st.subheader('Creación de tareas:')
        st.text(simplified)
        
        
    c1,c2,c3 = st.columns((2,8,2))
    
    with c3:
        st.image(img_bluetab,width=300)


if __name__ == "__main__":
    simplificator()