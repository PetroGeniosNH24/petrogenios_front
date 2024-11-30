import streamlit as st
import streamlit.components.v1 as components

def run():
    
    c1,c2 = st.columns((9,5))
    with c1:
        iframe_src = "https://dbc-408b9f8f-28d4.cloud.databricks.com/embed/dashboardsv3/01efaebafd8e1cee8aebfa37b53abbec?o=2439438098761605"
        components.iframe(iframe_src,height=1000,width=1000,scrolling=True)
   # You can add height and width to the component of course.

if __name__ == "__main__":
    run()