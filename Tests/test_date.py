import datetime
import streamlit as st

day = st.date_input("When's your birthday", datetime.datetime.today(), format="DD.MM.YYYY")
year = day.year
formatted_date = day.strftime("%d.%m.%Y")
st.write('Your birthday is:', formatted_date)
st.write(f"st.write.f string - The year is: {year}")
st.write('st.write - The year is:', year)
#st.markdown('Markdown - This is regular text', year)
