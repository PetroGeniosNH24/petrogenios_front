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
    
    pg = st.navigation([
        st.Page('MainPage.py', title="Main Page", icon=":material/home:"),
        st.Page('pages/Simplificator.py', title="Simplificador de contenido", icon=":material/search:"),
        st.Page('pages/Task.py', title="Creador de tareas", icon=":material/list:")
    ])
    pg.run()
        
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
                height: 200px;  /* Cambia la altura según sea necesario */
                font-size: 100px;  /* Ajusta el tamaño de la fuente si es necesario */
            }

            /* Estilos para centrar las columnas en el layout */
            .stColumns {
                display: flex;
                justify-content: center;
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

    st.title('BlueHub')

    # Crear las columnas y los botones
    c1, c2, c3 = st.columns(3,vertical_alignment="center")

    with c1:
        
        st.subheader("Simplificador de contenido")
        image_path = 'resources/simplificar2.png'
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        with st.container(border=True):
            st.markdown(f"""
                <a href="/Simplificator" target="_self">
                    <img src="data:image/png;base64,{encoded_string}" alt="Imagen Clickeable" width="150" height="150">
                </a>
            """, unsafe_allow_html=True)

        
        st.subheader("Detector de emociones")
        image_path = 'resources/emociones2.png'
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        with st.container(border=True):
            st.markdown(f"""
                <a href="/Emociones" target="_self">
                    <img src="data:image/png;base64,{encoded_string}" alt="Imagen Clickeable" width="150" height="150">
                </a>
            """, unsafe_allow_html=True)

    with c2:
        st.subheader("Creador de tareas")
        image_path = 'resources/lista2.png'
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        with st.container(border=True):
            st.markdown(f"""
                <a href="/Simplificator" target="_self">
                    <img src="data:image/png;base64,{encoded_string}" alt="Imagen Clickeable" width="150" height="150">
                </a>
            """, unsafe_allow_html=True)

        st.subheader("Añadir")
        image_path = 'resources/add.png'
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        with st.container(border=True):
            st.markdown(f"""
                <a href="/Add" target="_self">
                    <img src="data:image/png;base64,{encoded_string}" alt="Imagen Clickeable" width="150" height="150">
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
