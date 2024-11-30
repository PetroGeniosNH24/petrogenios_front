import os
import streamlit as st
import base64
import json

BASE_PATH = '.'

def main_page():
    
    
    
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
    
    st.title('BlueHub')
    
    
    # Definir el CSS personalizado
    st.markdown("""
        <style>
            .stButton>button {
                height: 200px;  /* Cambia la altura según sea necesario */
                font-size: 100px;  /* Ajusta el tamaño de la fuente si es necesario */
            }
        </style>
    """, unsafe_allow_html=True)

    # Crear las columnas y los botones
    c1, c2 = st.columns(2)

    with c1:
        with st.container(border=True):
            st.header("Job Assistant")
            st.button('Simplificator1', use_container_width=True, type='primary')        
            st.button('Sign&Flow1', use_container_width=True, type='primary')

    with c2:
        with st.container(border=True):
            st.header("Personal Assistant")
            st.button('Simplificator2', use_container_width=True, type='primary')        
            st.button('Sign&Flow2', use_container_width=True, type='primary')
            
    c1,c2,c3 = st.columns((2,8,2))
    
    with c3:
        st.image(img_bluetab,width=300)

        


    
    
        
    
    
if __name__ == "__main__":
    main_page()