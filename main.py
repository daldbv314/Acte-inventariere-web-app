import streamlit as st

st.set_page_config(page_title='My Application', layout='centered', )
st.title('This is a title')

# --- HIDE STREAMLIT STYLE ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.text_input('Companie', value="", placeholder='e.g. ADAKRON CREATIVE ACCOUNTING', max_chars=5, key='COMPANIE', help='nu adaugati "SRL"')