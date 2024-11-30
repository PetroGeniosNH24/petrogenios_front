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
                    padding-top: 2.8rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
                
                .image-container {
                    margin-top: 18px;  /* Ajusta el valor para mover la imagen más o menos */
                }
                
                /* Estilo para centrar el video */
                .video-container {
                    position: relative;
                    padding-bottom: 56.25%; /* Proporción 16:9 */
                    height: 0;
                    overflow: hidden;
                    max-width: 100%;
                    background: #000;
                }
                .video-container iframe {
                    position: absolute;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                }
                .footer img {
                    width: 150px;  /* Ajusta el tamaño de la imagen del pie de página */
                }
        </style>
        """, unsafe_allow_html=True)        
    
    c1,c2,c3 = st.columns((0.5,5.5,6))
    
    with c1:    
        st.markdown('<div class="image-container">', unsafe_allow_html=True)
        st.image('resources/emociones2.png', width=40)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with c2:    
        st.header('BlueEmociones')
        
    
        # ID del video de YouTube
    video_id = "6n4NSRi-gPY"

    # Crear el iframe del video con el parámetro `mute=1` para desactivar el sonido
    video_html = f"""
        <div class="video-container">
            <iframe src="https://www.youtube.com/embed/{video_id}?mute=1&autoplay=1&controls=0&modestbranding=1&rel=0&showinfo=0&iv_load_policy=3" 
                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
            </iframe>
        </div>
        """

    # Insertar el iframe con el video en la aplicación Streamlit
    st.markdown(video_html, unsafe_allow_html=True)


if __name__ == "__main__":
    simplificator()