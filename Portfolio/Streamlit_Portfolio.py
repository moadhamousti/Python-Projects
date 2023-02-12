import streamlit as st

# Stating Paths 
from pathlib import Path

# for image import 
from PIL import Image

# for timeline showcase 
from streamlit_timeline import timeline

# For buttons 

from st_functions import *

# buy me coffe button :
from streamlit_extras.buy_me_a_coffee import button

# Graph using plotly :
import plotly.express as px

# Github & stackoverflow badges :
from streamlit_extras.badges import badge

# Colored header for the form :
from streamlit_extras.colored_header import colored_header

# Config.toml for overall look :
import toml

# Constant for the badge :

info = {'Stackoverflow_flair':'''<a href="https://stackoverflow.com/users/21148612/moad-hamousti"><img src="https://stackoverflow.com/users/flair/21148612.png" width="280" height="70" alt="profile for Moad Hamousti at Stack Overflow, Q&amp;A for professional and enthusiast programmers" title="profile for Moad Hamousti at Stack Overflow, Q&amp;A for professional and enthusiast programmers"></a>'''}


# Set the page title
st.set_page_config(page_title="Moad Hamousti Portfolio" , page_icon="🧑🏻", layout="wide")


# config.toml file configuration


@st.cache(allow_output_mutation=True)
def load_config():
    with open(".streamlit/config.toml") as f:
        config = toml.loads(f.read())
    return config

config = load_config()


# Path Settings

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
profile_pic = current_dir / "assets" / "profile-pic(1).png"

# General Settings 
PAGE_TITLE = "Moad Hamousti | PORTFOLIO"
PAGE_ICON = "🚀"
NAME = "Moad Hamousti"
EMAIL = "moadhamousti@gmail.com"
icon_size = 20

# Page Title & icon 

badge(type="github", name="moadhamousti/MyInitialProjects")

# Sidebar Inputs 

# 1------Page Logo :

st.sidebar.image("assets/folio.png", width=200)

# 2------ Email :

st.sidebar.caption('Wish to connect?')
st.sidebar.write("""
<span style="color:black">📧 : moadhamousti@gmail.com</span>
""", unsafe_allow_html=True)

# 3------ Stack Over-flow Flair or Badge :

st.sidebar.markdown(info['Stackoverflow_flair'], unsafe_allow_html=True)

# Other Stuff in the sidebar 

with st.sidebar:
        # Buy Me Cafe Button 
        button(username="moadhamousti", floating=False, width=400)
        
# Load CSS, PDF & Profil Picture
with open(css_file) as f:
   st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
profile_pic = Image.open(profile_pic)

load_css()


col1, col2, col3 = st.columns(3)
col2.image(profile_pic)

st.header("MOAD  HAMOUSTI")



st.info("(●'◡'●)....Hello..! I am Just a beginner learner of Web Developpement who loves to apply HTML and CSS on real world projects. I am currently learning about Python and the framework Streamlit and have a keen interest in Web Developpement and WEB 3.0  🚀.")

st.image("https://cliply.co/wp-content/uploads/2019/12/371903520_SOCIAL_ICONS_TRANSPARENT_400px.gif")

icon_size = 20

st_button('linkedin', 'https://www.linkedin.com/in/moad-hamousti-49136b111/', 'LINKEDIN', icon_size)
st_button('github', 'https://github.com/moadhamousti', 'GITHUB', icon_size)
st_button('facebook', 'https://web.facebook.com/Moad.Hamousti', 'FACEBOOK', icon_size)
st_button('', 'https://mail.google.com/mail/?view=cm&source=mailto&to=moadhamousti@gmail.com', 'moadhamousti@gmail.com', icon_size)



# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("assets/style.css")

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"

# --- LOAD CSS ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
    

# Timeline Section : 

st.subheader('⌛ TIMELINE')

load_css()


with st.spinner(text="Building line"):
    with open('timeline.json', "r") as f:
        data = f.read()
        timeline(data, height=500)
        
# Education Section 

cola,colb,colc = st.columns(3)
with colb:
  st.subheader("🎓 EDUCATION")
st.write("\n")

st.markdown('•  Baccalaureate in science Physics High School Al Amal (TIKIOUINE,AGADIR) : 2015 .')
st.markdown('•  Studying Economics Currently in FSJES AGADIR (AGADIR).')
st.markdown('•  Studying in eWa (Ecole Web Avancée) School of the Web. ')

# Table using pandas 


data = [("AL AMAL High School", "Science Of Physics", "Baccalaureat", 2015),        ("FSJES AGADIR", "Economics", "Ongoing (3rd Year)", 2018),        ("eWa (ADVANCED WEB School)", "Web Development and Multimedia", "Ongoing (1st Year)", 2023)]

df = pd.DataFrame(data, columns=["Institute", "Qualification", "Stream", "Year"])


# Use a style tag to set the font size
st.write("<style>table {font-size: 20px;}</style>", unsafe_allow_html=True)

# Stretch the table to take the whole page
st.write(df.style.set_caption("Table Caption"))



# Daily Routine Section 

cola,colb,colc = st.columns(3)
with colb:
  st.subheader("🗓 DAILY ROUTINE")

graph = """
digraph {
    "Wake up" -> "Check emails / Whatsapp Messages / Facebook"
    "Check emails / Whatsapp Messages / Facebook" -> "eWa School"
    "eWa School" -> "UNIX" -> "Break"
    "Break" -> "Photoshop"
    "Break" -> "Python" -> "HTML/CSS"
    "Break" -> "Photoshop"
    "Lunch" -> "Relax" -> "Random Projects / HomeWork"
    "Break" -> "Relax / Watching TV / Series"
    "UNIX" -> "Snack"
    "Python" -> "Relax"
    "HTML/CSS" -> "Relax"
    "Snack" -> "Body Exercicing"
    "Break" -> "Snack"
    "running errands" -> "HTML/CSS"
    "Break" -> "Surfing Internet / Reading"
    "Random Projects / HomeWork" -> "End work"
    "End work" -> "Dinner" -> "Relax" -> "Sleep"
}
"""
st.graphviz_chart(graph)


# Skills and Tools Section 
st.subheader("👨🏻‍💻 SKILLS & TOOLS")

cola,colb,colc = st.columns(3)
with colb:
    st.image("https://spansystech.com/images/hero/banner3.gif", width=250, clamp=False, channels="RGB")
st.write("\n")

skills=["Python","Adobe illustrator", "After Effects", "Photoshop","Adobe Premiere","Git", "Algorithms", "Statistics", "Word", "Excel", "Linux/Ubuntu","Streamlit"]

for i in range(0, len(skills), 4):
    cola,colb,colc,cold=st.columns(4)
    with cola:
        st.button(skills[i])
    with colb:
        try:
            st.button(skills[i+1])
        except:
            pass
    with colc:
        try:
            st.button(skills[i+2])
        except:
            pass
    with cold:
        try:
            st.button(skills[i+3])
        except:
            pass
st.write("\n")

# Hard Skills using Pandas :
        
cola,colb,colc = st.columns(3)
with colb:
    data = {"Skills": ["Python", "Adobe illustrator", "Excel","after effects", "JavaScript", "Photoshop","Streamlit", "Linux/Ubuntu", "Statistics","Algorithme", "Git", "Adobe Premiere"], "Percentage of Mastery": 
    [10,40,98,60,5,75,15,50,60,60,70,90]}
    df = pd.DataFrame(data)

    colors = ['#424bff ', 'goldenrod', '#2dab90', '#2d90ab', '  #b7d638  ', ' #4a92d5 ', 'lightskyblue', ' #769c9d ', ' #62f16d ', ' #425f44 ', ' #ba7c00 ', ' #2f45ff ']

#  Hard Skills Graph using Plotly :

st.title("📊 HARD SKILLS MASTERY")
st.write(px.bar(df, x="Skills", y="Percentage of Mastery", color="Skills", color_discrete_sequence=colors))

# SOFT SKILLS Section :
cola,colb,colc = st.columns(3)
with colb:
  st.subheader("🤵🏻‍♂️   SOFT SKILLS")
st.markdown('➤  PROBLEM-SOLVING : ⭐ ⭐ ⭐ ⭐ ')
st.markdown('➤  ADAPTABILITY : ⭐ ⭐ ⭐ ')
st.markdown('➤  CREATIVITY : ⭐ ⭐ ⭐ ⭐ ')
st.markdown('➤  MOTIVATION : ⭐ ⭐ ⭐ ⭐ ⭐')
st.markdown('➤  ATTENTION TO DETAILS : ⭐ ⭐ ⭐ ')
st.markdown('➤  ADAPTABILITY : ⭐ ⭐ ⭐ ⭐')
st.markdown('➤  INTERPERSONAL SKILLS : ⭐ ⭐ ')
st.markdown('➤  TIME MANAGEMENT : ⭐ ⭐ ⭐ ')





# Athletics Section :

cola,colb,colc = st.columns(3)
with colb:
  st.subheader("🏃‍♂️  ATHLETICS")
st.markdown('➡  Won A Medal In a Regional Competition In KUNGFU (Việt Võ Đạo) In Middle School.')
st.markdown('➡  Practiced KARATE and Taekwondo For The First 2 Years Of High School.')
st.markdown('➡  Practicing CALISTHENICS & BODYBUILDING At The Moment To Stay In Shape.')


# get in touch Form section :

colored_header(
    label=":mailbox: GET IN TOUCH WITH ME!",
    description="Feel free to send me any message you want :smile:",
    color_name="blue-70",
)
        


contact_form = """
<form action="https://formsubmit.co/YOUREMAIL@EMAIL.COM" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)



# Portfolio signature 

cola,colb,colc = st.columns(3)
with colb:
    st.image("https://miro.medium.com/max/1400/0*s7-847-cMWNrfnyH.gif", width=240)



