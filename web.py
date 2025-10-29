import streamlit as st
import functions as fc

todos = fc.read_list()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    fc.write_list(todos)

st.title("My Todo App")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        fc.write_list(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input("Add Todo: ", placeholder="Add new todo",
              on_change=add_todo, key="new_todo")
