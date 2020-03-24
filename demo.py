import streamlit as st

# Text/Title

st.title("Streamlit Tutorials")

# Header/Subheader

st.header("This is a header")

st.subheader("This is a sub-header")

# Text

st.text("Hello Streamlit")

# Markdown

st.markdown("### This is a Markdown")

# Error/Colorful Text
st.success("Successful")
st.info("Information!")
st.warning("This is  a warning")
st.error("This is an error!")

st.exception("NameError('name three not defined')")

# Get Help Info ABout Pthon

st.help(range)

# Writing Text/Super Fxn
st.write("Text with write")

st.write(range(10))

#Images

from PIL import Image
img = Image.open("example.jpg")

st.image(img, width = 700, caption = "Simple Image")

# Videos
vid_file = open("example.mp4","rb").read()
#vid_bytes = vid_file.read()
st.video(vid_file)

# Audio

#audio_file = open("examplemusic.mp3").read()
#st.audio(audio_file, format = 'mp3')

# Widget

# Checkbox

if(st.checkbox("Show/Hide")):
    st.text("Showing or Hiding Widget")

# Radio Button

status = st.radio("What is your status", ("Active","Inactive"))

if(status == 'Active'):
    st.success("you are Active")
else:
    st.warning("Inactive, Activate")


# SelectBox

occupation = st.selectbox("Your Occupation",["Programmer", "Data Scientist", "Doctor", "Businessman"])
st.write("You Selected this option ", occupation)
# MultiSelect

location = st.multiselect("Where do you  work?",("London", "New York", "Accra", "Kiev", "Nepal"))
st.write("You selected ", len(location), "Locations")

# Slider

level = st.slider("What is your level", 1, 5)

# Buttons
st.button("Simple Button")

if(st.button("About")):
    st.text("Streamlit is Cool")

# Text Input

firstname = st.text_input("Enter Your Firstname", "Type Here..")
if(st.button("Submit")):
    result = firstname.title()
    st.success(result)


# Text Area
message = st.text_area("Enter Your message", "Type Here..")
if(st.button("Submit Message")):
    result = message.title()
    st.success(message)

# Date Input

import datetime
today = st.date_input("Today is", datetime.datetime.now())

# Time

the_time = st.time_input("The time is", datetime.time())

# Displaying JSON

st.text("Display JSON")
st.json({'name':"Jesse", 'gender':"male"})

# Display Raw Code

st.text("Display Raw Code")
st.code("import numpy as np")

# Dislapy Raw Code

with st.echo():
    # This will also show as comment
    import pandas as pd
    df = pd.DataFrame()

# Progress Bar

import time
my_bar = st.progress(0)
for p in range(10):
    my_bar.progress(p + 1)

# Spinner
#with st.spinner("Waiting .."):
#    time.sleep(5)

st.success("Finished!")

# Balloons
#st.balloons()

# SIDEBAR
st.sidebar.header("About")
st.sidebar.text("This is Streamlit Tut")

# Functions
@st.cache
def run_fxn():
    return range(100)

st.write(run_fxn())

# Plot
st.pyplot()

# DataFrames
st.dataFrame(df)

# Tables
st.table(df)