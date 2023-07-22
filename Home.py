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
    content = """* Data Analyst proficient with Python (including libraries: Pandas, Numpy).
                 * Proficiency with Exploratory Data Analysis, Data Visualization, Statistics, Data Science and Machine Learning with Python.
                 * Experience with BI tools such as Tableau and Qlik Sense, and databases (SQL, MongoDB) including writing complex queries.
                 * I developed 8 projects using technologies such as Python (Pandas, Numpy), Tableau, and Qlick Sense.
                 * Ability to collect, organize, and analyze significant information with attention to detail and accuracy.
                 * Self-learner, multi-tasker, and Independent with excellent analytical and research skills.
                 * Problem solver combined with strong communication and interpersonal skills.
                 * B.Sc. in Computer and Information Science (specialization in Big Data)
                 * English – fluent."""
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
