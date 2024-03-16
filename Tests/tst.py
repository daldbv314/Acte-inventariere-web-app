import streamlit as st

st.session_state

def submit ():
    st.session_state.last_A = st.session_state.A
    st.session_state.last_B = st.session_state.B
    
if 'show' not in st.session_state:
    st.session_state.show = True

def toggle():
    st.session_state.show = not st.session_state.show

st.button('Show/Hide Form', on_click=toggle)

if st.session_state.show:
    with st.form('my_form'):
        st.text_input('Text', key='A')
        st.number_input('Number', key='B')
        st.form_submit_button('Submit', on_click = submit)

st.button('Page Reload')

st.session_state