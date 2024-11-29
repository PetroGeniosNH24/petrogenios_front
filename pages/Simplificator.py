import os
import streamlit as st
import base64
import json
import requests

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
                   
    st.header('BlueSimplificator')
    
    text = st.text_area("¿Qué quieres simplificar?")

    if text.startswith("https") or text.startswith("http"):
        response = 'Es URL'
    else:
        response = 'No es URL'

    if st.button('Simplify',type='primary'):   
        response = dbutils.notebook.run("/path/to/notebook_simplificador", 60, {"input_text": text})
    
    with st.container(border=True):
        st.subheader('Simplificación:')
        st.text(response)
        
        
    c1,c2,c3 = st.columns((2,8,2))
    
    with c3:
        st.image(img_bluetab,width=300)
    
    
    
    
    
        
    
    
if __name__ == "__main__":
    simplificator()