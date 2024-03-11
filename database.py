import streamlit as st  # pip install streamlit
from deta import Deta  # pip install deta

DETA_KEY = "d1TqaNaW_byALYQbvEKC69ypxtXqXqHktNiKPL4CL"

# Initialize with a project key
deta = Deta(DETA_KEY)

# This is how to create/connect a database
db = deta.Base("Customers")



