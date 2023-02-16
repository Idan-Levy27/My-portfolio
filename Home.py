import streamlit as st
import pandas

st.set_page_config(layout="wide")
apps_info = "Below you can find some of the apps I have built in Python. " \
            "Feel free to contact me!"

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpeg")

with col2:
    st.title("Idan Levy")
    content = """Hi, I am Idan Levy! Highly motivated software developer with experience developing and optimizing 
              algorithms through large code bases in C, C#, Python, and Java. Skilled in source code control tools 
              and proficient in data analysis and machine learning concepts. Demonstrated ability to work well in a team 
              environment and quickly learn new technologies"""
    st.subheader(content)

empty_1, center_col, empty_2 = st.columns([1, 4, 1])

with empty_1:
    st.write(' ')

with center_col:
    st.subheader(apps_info)

with empty_2:
    st.write(' ')

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
        if row["title"] == "Todo App":
            st.write("Check out this [link](https://idan-levy27-my-todolist-web-todo-webapp-qfl4zp.streamlit.app/)")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
