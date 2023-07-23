import streamlit as st
import pandas

st.set_page_config(layout="wide")
apps_info = "Below you can find some of the apps I have built in Python. " \
            "Feel free to contact me!"

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Idan Levy")
    bullet_1 = "* Data Analyst proficient with Python (including libraries: Pandas, Numpy)."
    bullet_2 = "* Proficiency with Exploratory Data Analysis, Data Visualization, Statistics," \
               "Data Science and Machine Learning with Python."
    bullet_3 = "* Experience with BI tools such as Tableau and Qlik Sense, and databases (SQL, MongoDB)" \
               " including writing complex queries."
    bullet_4 = "* I developed 8 projects using technologies such as Python (Pandas, Numpy), Tableau, and Qlik Sense."
    bullet_5 = "* Ability to collect, organize, and analyze significant information with attention to detail and accuracy."
    bullet_6 = "* Self-learner, multi-tasker, and Independent with excellent analytical and research skills."
    bullet_7 = "* Problem solver combined with strong communication and interpersonal skills."
    bullet_8 = "* B.Sc. in Computer and Information Science (specialization in Big Data)."
    bullet_9 = "* English – fluent."

    cont = bullet_1 + "\n" + bullet_2 + "\n" + bullet_3 + "\n" + bullet_4 + "\n" + bullet_5 + "\n" + bullet_6 + "\n" + \
           bullet_7 + "\n" + bullet_8 + "\n" + bullet_9

    st.info(cont)

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
