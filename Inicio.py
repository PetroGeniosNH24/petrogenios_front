import os
import streamlit as st
import base64
import webbrowser
from st_pages import add_page_title
from st_pages import add_page_title, get_nav_from_toml


BASE_PATH = '.'

def main_page():
    
    


    img_favicon = os.path.join(BASE_PATH, 'resources', 'favicon_bluetab.png')
    img_bluetab = os.path.join(BASE_PATH, 'resources', 'bluetab.png')
    lupa = os.path.join(BASE_PATH, 'resources', 'lupa.png')

    st.set_page_config(page_title='Hackaton', page_icon=img_favicon, layout='wide' )
    
    # pg = st.navigation([
    #     st.Page('MainPage.py', title="Main Page", icon=":material/home:"),
    #     st.Page('Simplificator.py', title="Simplificador de contenido", icon=":material/search:"),
    #     st.Page('Task.py', title="Creador de tareas", icon=":material/list:")
    # ])
    # pg.run()
        
    # CSS personalizado para centrar las columnas y ajustar el pie de página
    st.markdown("""
        <style>
            /* Centrar el contenido de las columnas */
            .block-container {
                padding-top: 2.2rem;
                padding-bottom: 0rem;
                padding-left: 5rem;
                padding-right: 5rem;
                display: flex;
                justify-content: center;
            }

            /* Ajustar los estilos de los botones */
            .stButton>button {
                height: 150px !important;  /* Altura fija para los botones */
                width: 200px !important;   /* Ancho fijo para los botones */
                font-size: 20px !important;  /* Tamaño de la fuente fijo */
                border-radius: 8px !important;  /* Bordes redondeados */
                display: flex !important;
                align-items: center !important;
                justify-content: center !important;
                background-color: #4CAF50 !important;  /* Cambiar el fondo para mayor visibilidad */
                color: white !important;  /* Asegura que el texto sea visible */
            }
        
            /* Estilo para las imágenes y botones */
            .button-container {
                display: flex;
                justify-content: center;
                align-items: center;
                flex-direction: column;
                width: 100%;
                height: 100%;
                border-radius: 8px;
                object-fit: contain;  /* Mantiene la proporción de las imágenes */
                margin-bottom: 20px;
            }

            .button-container img {
                width: 100%;
                height: auto;
                border-radius: 8px;
                object-fit: contain;  /* Mantiene la proporción de las imágenes */
                margin-bottom: 20px;
            }
            
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

    st.title('AccessLink')

    # Crear las columnas y los botones
    c1, c2 = st.columns(2,vertical_alignment="center")

    with c1:
        st.markdown('<h3 style="text-align: center;">Simplificador de contenido</h3>', unsafe_allow_html=True)
        #st.subheader("Simplificador de contenido")
        c1_int, c2_int, c3_int = st.columns(3,vertical_alignment="center")
        with c2_int:
            image_path = 'resources/simplificar2.png'
            with open(image_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode()
                with st.container():
                    st.markdown(f"""
                        <a href="/Simplificador" target="_self" style="display: block; text-align: center;">
                            <div class="button-container">
                                <img src="data:image/png;base64,{encoded_string}" alt="Imagen Clickeable">
                            </div>
                        </a>
                    """, unsafe_allow_html=True)

        st.markdown('<h3 style="text-align: center;">Detector de emociones</h3>', unsafe_allow_html=True)

        #st.subheader("Detector de emociones")
        c1_int, c2_int, c3_int = st.columns(3,vertical_alignment="center")
        with c2_int:
            image_path = 'resources/emociones2.png'
            with open(image_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode()
                with st.container():
                    st.markdown(f"""
                        <a href="/Emociones" target="_self" style="display: block; text-align: center;">
                            <div class="button-container">
                                <img src="data:image/png;base64,{encoded_string}" alt="Imagen Clickeable">
                            </div>
                        </a>
                    """, unsafe_allow_html=True)

    with c2:
        
        st.markdown('<h3 style="text-align: center;">Creador de tareas</h3>', unsafe_allow_html=True)
        #st.subheader("Creador de tareas")
        c1_int, c2_int, c3_int = st.columns(3,vertical_alignment="center")
        with c2_int:
            image_path = 'resources/lista2.png'
            with open(image_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode()
                with st.container():
                    st.markdown(f"""
                        <a href="/Tareas" target="_self" style="display: block; text-align: center;">
                            <div class="button-container">
                                <img src="data:image/png;base64,{encoded_string}" alt="Imagen Clickeable">
                            </div>
                        </a>
                    """, unsafe_allow_html=True)

        st.markdown('<h3 style="text-align: center;">Añadir</h3>', unsafe_allow_html=True)
        #st.subheader("Añadir")
        c1_int, c2_int, c3_int = st.columns(3,vertical_alignment="center")
        with c2_int:
            image_path = 'resources/add.png'
            with open(image_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode()
                with st.container():
                    st.markdown(f"""
                        <a href="/Nuevo" target="_self" style="display: block; text-align: center;">
                            <div class="button-container">
                                <img src="data:image/png;base64,{encoded_string}" alt="Imagen Clickeable">
                            </div>
                        </a>
                    """, unsafe_allow_html=True)

    # Pie de página con el logo de Bluetab alineado a la derecha
    st.markdown(f"""
        <div class="footer">
            <img src="data:image/png;base64,{base64.b64encode(open(img_bluetab, 'rb').read()).decode()}" alt="Bluetab logo">
        </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main_page()
