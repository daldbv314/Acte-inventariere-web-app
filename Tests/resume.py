# https://afnanxkhan.medium.com/build-a-personalized-resume-generator-with-streamlit-and-docxtemplate-dafd4e430743

import streamlit as st
from docxtpl import DocxTemplate
from io import BytesIO

# Define the questions
questions = [
    "What is your full name?",
    "What is your email address?",
    "What is your phone number?",
    "What is your current job title?",
    "What is your work experience?",
    "What are your key skills?",
    "What is your education background?",
    "What are your certifications and awards?",
    "What is your desired job position?",
    "What are your hobbies and interests?",
    "Do you have any references? If so, please provide their contact information."
]

# Define the template file
template_file = "/path/to/resume_template.docx"

# Define helper functions for rendering the form and generating the resume
def render_form():
    with st.form("resume-form"):
        col1, col2 = st.columns(2)
        responses = []
        for i, q in enumerate(questions):
            if i <= 5:
                response = col1.text_input(q)
            else:
                response = col2.text_input(q)
            responses.append(response)
        #col1.write("")
        #col2.write("")
        submitted = st.form_submit_button("Generate Resume")
    return submitted, responses

def generate_resume(responses):
    doc = DocxTemplate(template_file)
    context = {
        'full_name': responses[0],
        'email': responses[1],
        'phone_number': responses[2],
        'current_job_title': responses[3],
        'work_experience': responses[4],
        'key_skills': responses[5],
        'education_background': responses[6],
        'certifications_awards': responses[7],
        'desired_job_position': responses[8],
        'hobbies_interests': responses[9],
        'references': responses[10]
    }
    doc.render(context)
    doc_bytes = BytesIO()
    doc.save(doc_bytes)
    return doc_bytes.getvalue()

#About 

#def about():
#    st.title("About")
#    st.write("This app is a Resume Generator built with Streamlit and DocxTemplate. It allows you to generate a personalized resume/CV by filling out a form with your information.")
#    st.write("""
#    Made with :heart: by AfnanKhan
#    """, unsafe_allow_html=True)


# Define the main function to run the app
def main():
    
    st.set_page_config(page_title="Resume Generator", page_icon=":guardsman:", layout="wide")
    st.title("Resume Generator")
    st.write("Welcome to the Resume Generator! Please fill out the form below to generate a personalized resume/CV.")

    submitted, responses = render_form()

    if submitted:
        st.write("Generating your resume... Please wait.")
        resume_buffer = generate_resume(responses)
        st.write("Resume successfully generated!")
        st.download_button(label="Download Generated Resume", data=resume_buffer, file_name="generated_resume.docx")
        
        

## Add a button to link to the About page
#    st.sidebar.button("About", on_click=about)
    
if __name__ == "__main__":
    main()