import streamlit as st

from PIL import Image
from streamlit_lottie import st_lottie

from menu import menu

from utils import load_lottiefile

st.set_page_config(page_title='Intelligent Automation Consulting',page_icon="👥", layout="wide")

if "role" not in st.session_state:
    st.session_state.role = None

st.title("Intelligent Automation Consulting")
st.subheader("Welcome to Innovation")
st.markdown("""
Are you looking to transform your business and harness the full potential of the Cloud? 
Our expert consultants specialize in Hybrid Cloud architecture and application modernization, helping businesses like yours thrive in the digital era.
""")

st.write("---")

left_column, right_column = st.columns(2)
with left_column:
      st.header("Architecture consultancy")
      st.markdown("""
      Our clients benefit from our experience of delivering highly resilient and scalable systems in many different industries.
      We can guide you in adopting the correct strategies for successful development and choosing the right technologies for your business needs.
      Review your scalability needs, your requirements around high availability, disaster recovery, or data consistency.
      """)
      st.write("##")
with right_column:
      st.image("images/it-consultant-service.jpg",width=400)

menu()