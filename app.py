import streamlit as st

st.set_page_config(page_title="To-Do List", page_icon="✅")

st.title("✅ To-Do List")

# Initialize session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Add a new task
with st.form("add_task_form", clear_on_submit=True):
    new_task = st.text_input("Enter a task")
    submitted = st.form_submit_button("Add Task")

    if submitted and new_task.strip():
        st.session_state.tasks.append(
            {
                "task": new_task.strip(),
                "completed": False
            }
        )

# Display tasks
if not st.session_state.tasks:
    st.info("No tasks yet. Add one above!")
else:
    for index, item in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([5, 1])

        with col1:
            completed = st.checkbox(
                item["task"],
                value=item["completed"],
                key=f"task_{index}"
            )

            st.session_state.tasks[index]["completed"] = completed

        with col2:
            if st.button("🗑️", key=f"delete_{index}"):
                st.session_state.tasks.pop(index)
                st.rerun()

# Clear completed tasks
if any(task["completed"] for task in st.session_state.tasks):
    if st.button("Clear Completed Tasks"):
        st.session_state.tasks = [
            task
            for task in st.session_state.tasks
            if not task["completed"]
        ]
        st.rerun()