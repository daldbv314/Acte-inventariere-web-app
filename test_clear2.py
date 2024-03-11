import streamlit as st


st.text_input('First Name:', key='F_NAME')
st.text_input('Middle Name:', key='M_NAME')
st.text_input('Last Name:', key='L_NAME')

# define set_name function where with name_field as parameter 
def set_name(name_field):
    #NAME must match the key NAME from text_input
    st.session_state.F_NAME = name_field
    st.session_state.M_NAME = name_field
    st.session_state.L_NAME = name_field

st.button('Clear name', on_click=set_name, args=[''])
st.button('Streamlit!', on_click=set_name, args=['Streamlit!!!!'])