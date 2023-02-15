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
    content = """Hi, I am Idan Levy! I am experienced developer with a background in developing and optimizing algorithms 
    using C#, Python, and Java. Also skilled in data analysis and statistical modeling to predict outcomes. 
    I have an excellent interpersonal skills, a fast self-learning ability, and are highly ambitious to thrive in a team environment.
    Always ready to learn and take on new challenges."""
    st.info(content)

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
