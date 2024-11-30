import os
import streamlit as st
import base64
import json

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
                
                .image-container {
                    margin-top: 18px;  /* Ajusta el valor para mover la imagen más o menos */
                }
                
                /* Imagen como pie de página */
                .footer {
                    position: fixed;
                    bottom: 10px;  /* Ajuste la posición vertical (a 10px del borde inferior) */
                    right: 10px;   /* Ajuste la posición horizontal (a 10px del borde derecho) */
                    width: auto;
                    text-align: right;
                    padding: 10px;
                    background-color: transparent;
                }

                .footer img {
                    width: 150px;  /* Ajusta el tamaño de la imagen del pie de página */
                }
        </style>
        """, unsafe_allow_html=True)            
                   
    
    c1,c2,c3 = st.columns((0.5,5.5,6))
    
    with c1:    
        st.markdown('<div class="image-container">', unsafe_allow_html=True)
        st.image('resources/signos2.png', width=40)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with c2:    
        st.header('BlueSignLanguage')
    
    text = st.text_area("¿Qué quieres simplificar?")
    
    response = ''
    if st.button('Simplify',type='primary'):   
        response = 'Hola'
    
    with st.container(border=True):
        st.subheader('Simplificación:')
        st.text(response)
        
        
    c1,c2,c3 = st.columns((2,8,2))
    
    # Pie de página con el logo de Bluetab alineado a la derecha
    st.markdown(f"""
        <div class="footer">
            <img src="data:image/png;base64,{base64.b64encode(open(img_bluetab, 'rb').read()).decode()}" alt="Bluetab logo">
        </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    simplificator()