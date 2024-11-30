import streamlit as st

pages = {
    "Your account": [
        st.Page('MainPage.py', title="Main Page"),
        st.Page('Simplificator.py', title="Simplificator"),
    ],
    "Resources": [
        st.Page("Sign.py", title="Learn about us"),
        st.Page("Task.py", title="Try it out"),
    ],
}

pg = st.navigation(pages)
pg.run()