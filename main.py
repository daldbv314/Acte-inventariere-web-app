import os
import io
import streamlit as st
from zipfile import ZipFile
from pathlib import Path
from docxtpl import DocxTemplate
from dotenv import load_dotenv

act_consitutiv_path = Path.cwd() / "Templates" / "v2-Act-constitutiv-(asociat-unic)-template.docx"

act_constitutiv_doc = DocxTemplate(act_consitutiv_path)


# Page settings
st.set_page_config(
    page_title='My Application', 
    layout='centered'
)

st.title('This is a title')

zip_buffer = io.BytesIO()

# --- HIDE STREAMLIT STYLE ---
#hide_st_style = """
#            <style>
#            #MainMenu {visibility: hidden;}
#            footer {visibility: hidden;}
#            header {visibility: hidden;}
#            </style>
#            """
#st.markdown(hide_st_style, unsafe_allow_html=True)


with st.form("infiintare_SRL", clear_on_submit=False):
    col1, col2 = st.columns(2)
    col1.text_input('Nume Asociat', value="", placeholder='e.g. POPESCU', max_chars=None, key='AS1_NUME', help='xxxxxx')
    col2.text_input('Prenume Asociat', value="", placeholder='e.g. DANIEL', max_chars=None, key='AS1_PRENUME', help='xxxxxxx')
    col1.text_input('Cetățean', value="român", placeholder=None, max_chars=None, key='AS1_CETATENIE', help='xxxxxxx')
    col2.markdown('''<br/><br/>'''
        , unsafe_allow_html=True
    )
    st.text_input('CNP', placeholder='e.g. 1840722368456', max_chars=13, key='AS1_CNP', help='xxxxxxx')
    col2.selectbox('Tip act', ("CI", "Pașaport", "Permis de ședere"), index=0, key='AS1_ACT_IDENT', help=None)
    st.date_input("Data eliberare", key='AS1_ACT_DATA_ELIB', help=None, format="DD.MM.YYYY",)
    st.text_input('Nume Companie', value="", placeholder='e.g. ADAKRON CREATIVE ACOUNTING', max_chars=None, key='COMPANIE', help='Nu adaugați "SRL"')
    st.write(' ')
    submitted = st.form_submit_button("Pas 1: Crează documentele", type="primary")

#    test = st.session_state.AS1_NUME
#    st.write(f"Value of AS1_NUME: {test}")

#    if submitted:
#        with st.spinner("Generating Clean Room Scripts..."):
#            data_clean_room.prepare_dcr_deployment(True, dcr_version, provider_account, None, consumer_account,
#                                                None, abbreviation, path, dcr_data_selection)
#            data_clean_room.execute()
#
#        # Message dependent on debug or not
#        st.success("Succes! Documentele pot fi downloadate acum!")
#
#        # Populate zip buffer for download buttons
#        load_zip_buffer(data_clean_room, zip_buffer, include_comments)
        
        














st.write("După ce ați primit mesajul de confirmare, puteți downloada documentele sub formă de arhivă.")
st.download_button(label="Pas 2: Downloadează", data=zip_buffer, file_name="Documente.zip", type="primary")

# define "clear_fields" function with "field_key" as parameter. used to clear fields
def clear_fields(field_key):
    #session state variable should match key of input field
    st.session_state.AS1_NUME = field_key
    st.session_state.M_NAME = field_key
    st.session_state.L_NAME = field_key

st.button('Reset', on_click=clear_fields, args=[''], help='Apasa pentru a sterge datele introduse pana acum')


