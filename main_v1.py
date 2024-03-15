import os
import io
import streamlit as st
from zipfile import ZipFile
from pathlib import Path
from docxtpl import DocxTemplate
from dotenv import load_dotenv
from io import BytesIO

# Page settings
st.set_page_config(
    page_title='My Application', 
    layout='centered'
)

st.title('Înființare SRL - web app - v1')


# --- HIDE STREAMLIT STYLE ---
#hide_st_style = """
#            <style>
#            #MainMenu {visibility: hidden;}
#            footer {visibility: hidden;}
#            header {visibility: hidden;}
#            </style>
#            """
#st.markdown(hide_st_style, unsafe_allow_html=True)


def var_dictionary ():
    var_dict = {
        'AS1_NUME': AS1_NUME,
        'AS1_PRENUME': AS1_PRENUME,
        'AS1_CETATENIE': AS1_CETATENIE,
        'AS1_CNP': AS1_CNP,
        'AS1_ACT_IDENT': AS1_ACT_IDENT,
        'AS1_ACT_DATA_ELIB': AS1_ACT_DATA_ELIB,
        'COMPANIE': COMPANIE,
    }
    return var_dict

def generate_act_constitutiv():
    act_consitutiv_path = Path.cwd() / "Templates" / "v2-Act-constitutiv-(asociat-unic)-template.docx"
    act_constitutiv_doc = DocxTemplate(act_consitutiv_path)
    context = var_dictionary()
    act_constitutiv_doc.render(context)
    output_act_constitutiv_path = Path.cwd() / "Results" / f"{COMPANIE}-Act-constitutiv.docx"
    act_constitutiv_doc.save(output_act_constitutiv_path)
#    return act_constitutiv_doc

def generate_sediu_social():
    sediu_social_path = Path.cwd() / "Templates" / "v2-Declaratie-sediu-social-template.docx"
    sediu_social_doc = DocxTemplate(sediu_social_path)
    context = var_dictionary()
    sediu_social_doc.render(context)
    output_sediu_social_path = Path.cwd() / "Results" / f"{COMPANIE}-Declaratie-sediu-social.docx"
    sediu_social_doc.save(output_sediu_social_path)
#    return sediu_social_doc

def create_zip_archive():
    results_folder = Path.cwd() / "Results"
    # Create an in-memory zip file
    with io.BytesIO() as zip_buffer:
        with ZipFile(zip_buffer, 'w') as zipf:
            # Iterate through all .docx files in the "Results" folder
            for docx_file in results_folder.glob("*.docx"):
                zipf.write(docx_file, arcname=docx_file.name)
        # Get the zip archive content as bytes
        zip_bytes = zip_buffer.getvalue()
    return zip_bytes

def remove_docx_files():
    # Path to the "Results" folder
    results_folder = Path.cwd() / "Results"

    # Iterate through all .docx files in the "Results" folder
    for docx_file in results_folder.glob("*.docx"):
        # Delete each .docx file
        docx_file.unlink()

# define "clear_fields" function with "field_key" as parameter. used to clear fields
def clear_fields(field_key):
    #session state variable should match key of input field
    st.session_state.AS1_NUME = field_key
    st.session_state.M_NAME = field_key
    st.session_state.L_NAME = field_key

with st.form("infiintare_SRL", clear_on_submit=False):
    col1, col2 = st.columns(2)
    AS1_NUME = col1.text_input('Nume Asociat', value="", placeholder='e.g. POPESCU', max_chars=None, key='AS1_NUME', help='xxxxxx')
    AS1_PRENUME = col2.text_input('Prenume Asociat', value="", placeholder='e.g. DANIEL', max_chars=None, key='AS1_PRENUME', help='xxxxxxx')
    AS1_CETATENIE = col1.text_input('Cetățean', value="român", placeholder=None, max_chars=None, key='AS1_CETATENIE', help='xxxxxxx')
    col2.markdown('''<br/><br/>'''
        , unsafe_allow_html=True
    )
    AS1_CNP = st.text_input('CNP', placeholder='e.g. 1840722368456', max_chars=13, key='AS1_CNP', help='xxxxxxx')
    AS1_ACT_IDENT = col2.selectbox('Tip act', ("CI", "Pașaport", "Permis de ședere"), index=0, key='AS1_ACT_IDENT', help=None)
    AS1_ACT_DATA_ELIB = st.date_input("Data eliberare", key='AS1_ACT_DATA_ELIB', help=None, format="DD.MM.YYYY",)
    COMPANIE = st.text_input('Nume Companie', value="", placeholder='e.g. ADAKRON CREATIVE ACOUNTING', max_chars=None, key='COMPANIE', help='Nu adaugați "SRL"')
    st.write(' ')
    submitted = st.form_submit_button("Pas 1: Crează documentele", type="primary")


#    test = st.session_state.AS1_NUME
#    st.write(f"Value of AS1_NUME: {test}")
#    st.write(f"Value of AS1_NUME: {AS1_NUME}")

if submitted:
    with st.spinner("Se generează documentele..."):
        generate_act_constitutiv()
        generate_sediu_social()
        zip_archive = create_zip_archive()
    st.success("Succes! Documentele pot fi descărcate acum!")
    st.download_button(label="Pas 2: Downloadează", data=zip_archive, file_name=f"{COMPANIE}-documente.zip", mime="docx", type="primary")
    remove_docx_files()

st.button('Resetează campurile', on_click=clear_fields, args=[''], help='Apasa pentru a sterge datele introduse pana acum')