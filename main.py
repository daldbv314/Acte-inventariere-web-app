import os
import streamlit as st
from pathlib import Path
from docxtpl import DocxTemplate
from dotenv import load_dotenv

act_consitutiv_path = Path.cwd() / "Templates" / "v2-Act-constitutiv-(asociat-unic)-template.docx"
sediu_social_path = Path.cwd() / "Templates" / "v2-Declaratie-sediu-social-template.docx"
contr_comodat_path = Path.cwd() / "Templates" / "v2-Contract-comodat-sediu-social(asociat-unic)-template.docx"
anexa1_path = Path.cwd() / "Templates" / "v2-anexa_1_inregistrare_fiscala-template.docx"
decl_indep_cond_path = Path.cwd() / "Templates" / "v2-declaratie-indeplinire-conditii-functionare-template.docx"

act_constitutiv_doc = DocxTemplate(act_consitutiv_path)
sediu_social_doc = DocxTemplate(sediu_social_path)
contr_comodat_doc = DocxTemplate(contr_comodat_path)
anexa1_doc = DocxTemplate(anexa1_path)
decl_indep_cond_doc = DocxTemplate(decl_indep_cond_path)

st.set_page_config(page_title='My Application', layout='centered', )
st.title('This is a title')

# --- HIDE STREAMLIT STYLE ---
#hide_st_style = """
#            <style>
#            #MainMenu {visibility: hidden;}
#            footer {visibility: hidden;}
#            header {visibility: hidden;}
#            </style>
#            """
#st.markdown(hide_st_style, unsafe_allow_html=True)

st.text_input('Nume Asociat', value="", placeholder='e.g. POPESCU', max_chars=None, key='AS1_NUME', help='xxxxxx')
st.text_input('Prenume Asociat', value="", placeholder='e.g. DANIEL', max_chars=None, key='AS1_PRENUME', help='xxxxxxx')
st.text_input('Cetățean', value="român", placeholder=None, max_chars=None, key='AS1_CETATENIE', help='xxxxxxx')
st.text_input('CNP', placeholder='e.g. 1840722368456', max_chars=13, key='AS1_CNP', help='xxxxxxx')
st.selectbox('Tip act', ("CI", "Pașaport", "Permis de ședere"), index=0, key='AS1_ACT_IDENT', help=None)
st.date_input("Data eliberare", key='AS1_ACT_DATA_ELIB', help=None, format="DD.MM.YYYY",)
st.text_input('Nume Companie', value="", placeholder='e.g. ADAKRON CREATIVE ACOUNTING', max_chars=None, key='COMPANIE', help='Nu adaugați "SRL"')

st.button("Creaza documentele", type="primary")






# define "clear_fields" function with "field_key" as parameter 
def clear_fields(field_key):
    #NAME must match the key NAME from text_input
    st.session_state.AS1_NUME = field_key
    st.session_state.M_NAME = field_key
    st.session_state.L_NAME = field_key

st.button('Reset', on_click=clear_fields, args=[''], help='Apasa pentru a sterge datele introduse pana acum')


