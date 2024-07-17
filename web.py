import streamlit as st
import func

st.set_page_config(layout="wide")
todos = func.get_todos()
st.title("TO-Do App")
st.subheader("Get started..")
st.write("<b>*Your List:*</b>", unsafe_allow_html=True)


def add_todo():
    todo_ = st.session_state["new"] + "\n"
    todos.append(todo_)
    func.write_todos(todos)


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        func.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add a new todo", key="new", on_change=add_todo)
