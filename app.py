import streamlit as st
import pandas as pd
from io import StringIO
import datetime

 




# df = pd.read_csv("second.csv")
# st.line_chart(df)

# Using columns to create a two-column layout
col1, col2 = st.columns(2)
with col1:
    st.write("Column 1")
    st.markdown("# <span style='color: blue;'>Hello *world!* </span>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
    
    
with col2:
    st.write("Column 2")
    age = st.slider('How old are you?', 0, 130, 25)
    st.write("I'm ", age, 'years old')
d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)
# Using sidebar for a side panel
with st.sidebar:
    st.write("Welcome")
    st.write("Home")
    st.write("FAQ")
    st.write("Support")

# Using expander to collapse/expand content
with st.expander("Click to expand"):
    st.write("This is for test")
    st.write("Hey")
    st.write("Hi There!")