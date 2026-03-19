import pandas as pd
import streamlit as st

st.title("Testing Widgets")

# Write Test
st.write("Write someting in the textbox.")

# Create Text box
name=st.text_input("Enter your name")
if name:
    st.write(f"Hello {name}, welcome to the university.")

# Create a slider for range
age=st.slider("Enter your age: ",0,100,20)
st.write(f"Your age is {age}.")

# Create drop down for option selection

options=["Python","Java","JavaScript","c++"]
choose=st.selectbox("Choose your favorite language: ", options)
st.write(f"Your selected {choose}.")

# Import a CSV file from system:
csv_file=st.file_uploader("Upload a CSV file ", type="csv")
if csv_file is not None:
    df=pd.read_csv(csv_file)
    st.write(df)

