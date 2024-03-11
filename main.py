import streamlit as st
from pathlib import Path
from docxtpl import DocxTemplate

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

st.text_input('Nume Asociat', value="", placeholder='e.g. POPESCU', max_chars=None, key='AS1_NUME', help='xxxxxx')
st.text_input('Prenume Asociat', value="", placeholder='e.g. DANIEL', max_chars=None, key='AS1_PRENUME', help='xxxxxxx')
st.text_input('Cetățean', value="român", placeholder=None, max_chars=None, key='AS1_CETATENIE', help='xxxxxxx')
st.text_input('CNP', placeholder='e.g. 1840722368456', max_chars=13, key='AS1_CNP', help='xxxxxxx')
st.selectbox('Tip act', ("CI", "Pașaport", "Permis de ședere"), index=0, key='AS1_ACT_IDENT', help=None)
st.date_input("Data eliberare", key='AS1_ACT_DATA_ELIB', help=None, format="DD.MM.YYYY",)
st.text_input('Nume Companie', value="", placeholder='e.g. ADAKRON CREATIVE ACOUNTING', max_chars=None, key='COMPANIE', help='Nu adaugați "SRL"')