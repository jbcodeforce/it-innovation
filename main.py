import streamlit as st
import json
from PIL import Image
from streamlit_lottie import st_lottie
from st_pages import Page, show_pages

# find emojis https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title='IT Innovation Consulting',page_icon="👥", layout="wide")

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

with st.sidebar:
    
    show_pages(
    [
        Page("Main.py", "Home", "🏠"),
        Page("pages/1_services.py", "Services",":question:"),
        Page("pages/2_courses.py", "Courses", ":school:"),
        Page("pages/3_blogs.py", "Blogs", ":book:"),
        Page("pages/4_contact.py", "Contact", ":email:"),
    ]
)
    
with st.container():
    st.title("IT Innovation Consulting")
    st.subheader("Welcome to Innovation")
    st.markdown("Are you looking to transform your business and harness the full potential of the Cloud? Our expert consultants specialize in AWS Cloud architecture and application modernization, helping businesses like yours thrive in the digital era.")
   
lottie_coding = load_lottiefile("images/an-1.json") 

with st.container():
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
        # st.write("Image created by StableDiffusionXL")

with st.container():
    st.write("---")
    st.header("Digital Innovations")
    left_column, right_column = st.columns((1,2))
    with left_column:
        st_lottie(
            lottie_coding,
            speed=1,
            reverse=False,
            loop=True,
            quality="low", # medium ; high
            height=200,
            width=None,
            key="Coding",
        )
        st.write("Annimation from Lottiefiles.com.")

    with right_column:
        st.subheader("Microservice")
        st.write("""
            Move from your existing application to smaller microservice using application decomposition. 
            Microservice implementations may become complex to manage. We start our projects with a strong foundation 
            by adopting domain-driven design practices, and we use iterative and incremental
            methodology to drive innovation. Combining with test-driven development, we design and build our 
            systems with testing as a primary concern. 
            """)

with st.container():
    st.subheader("Event-driven")
    left_column, right_column = st.columns(2)
    with left_column:
        st.image("images/eda-hl.png",width=380)
    with right_column:
        st.write("""
            Event-driven solution are for scaling and decreasing coupling between components. But once we design with events,
            we have new design patterns to consider. With our experience in implementing solutions based on event-sourcing,
             command query representation segregation, saga patterns, we will help you improve your solutions and complement
             with real-time analytics and complex event processing. Our unique expertize in rule engine, messaging and streaming middleware
             helps hundred of customers to be successful.
            """)
        
with st.container():
    st.subheader("AI - Machine Learning - Generative AI")
    left_column, right_column = st.columns((1,1))
    with left_column:
        st.write("""
            
            """)
    with right_column:
        st.image("images/llm-ra-1.png",width=400)
        