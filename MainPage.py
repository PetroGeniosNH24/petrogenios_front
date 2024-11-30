import os
import streamlit as st
import base64
import json
import webbrowser
BASE_PATH = '.'

def main_page():

    img_favicon = os.path.join(BASE_PATH,'resources','favicon_bluetab.png')
    img_bluetab = os.path.join(BASE_PATH,'resources','bluetab.png')
    lupa = os.path.join(BASE_PATH,'resources','lupa.png')

    
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
        with st.container():
            st.subheader("Simplificador")
            image_url = "https://cdn-icons-png.flaticon.com/512/1150/1150652.png"

            st.markdown(f"""
                <a href="/Simplificator" target="_self">
                    <img src="{image_url}" alt="Imagen Clickeable" width="150" height="150">
                </a>
            """, unsafe_allow_html=True)

            st.subheader("Sign&Flow")
            image_url2 = "https://lh5.ggpht.com/weRG9vc_0ffvIrTo-ydgIEsn5gdyQOBjlHvExOIx2JmYhxsuB_P1HDRqh6OTS2xatqw=w300"

            st.markdown(f"""
                <a href="/Sign" target="_self">
                    <img src="{image_url2}" alt="Imagen Clickeable" width="150" height="150">
                </a>
            """, unsafe_allow_html=True)

    with c2:
        with st.container():
            
            st.subheader("Task creator")
            image_url4 = "https://cdn-icons-png.flaticon.com/512/1345/1345063.png"

            st.markdown(f"""
                <a href="/" target="_self">
                    <img src="{image_url4}" alt="Imagen Clickeable" width="150" height="150">
                </a>
            """, unsafe_allow_html=True)

            st.subheader("Detección de emociones")
            image_url3 = "https://cdn-icons-png.flaticon.com/512/1457/1457326.png"

            st.markdown(f"""
                <a href="/" target="_self">
                    <img src="{image_url3}" alt="Imagen Clickeable" width="150" height="150">
                </a>
            """, unsafe_allow_html=True)
            
    c1,c2,c3 = st.columns((2,8,2))
    
    with c3:
        st.image(img_bluetab,width=300)

    
if __name__ == "__main__":
    main_page()