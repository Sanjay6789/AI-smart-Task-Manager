import streamlit as st
# Humne import ka tareeka badal diya taaki error na aaye
import database.db_manager as db
from services.ai_service import extract_task_details

# Database initialize karein
db.init_db()

# Page UI Setup``
st.set_page_config(page_title="AI Smart Task Manager", page_icon="📝", layout="centered")
st.title("📝 AI-Powered Smart Task Manager")
st.write("Professional Modular Architecture Version")

# Input Form
with st.form("task_form", clear_on_submit=True):
    user_input = st.text_input("Naya task likhein (e.g., 'Kal shaam 5 baje client call hai')", 
                              placeholder="Type your task here...")
    submit_button = st.form_submit_button("AI se Add Karein")

# Form Submission Logic
if submit_button and user_input:
    with st.spinner("AI task process kar raha hai..."):
        task_name, due_date = extract_task_details(user_input)
        db.add_task(task_name, due_date)
        st.success(f"📌 Task Added: *{task_name}* | 📅 Date: *{due_date}*")

# Saved Tasks Section
st.subheader("📋 Aapke Saved Tasks")
all_tasks = db.get_all_tasks()

if not all_tasks:
    st.info("Abhi tak koi task nahi hai.")
else:
    for task_id, task_text, due_date in all_tasks:
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"🔹 *{task_text}* (Due: {due_date} )")
        with col2:
            if st.button("Done ✅", key=f"del_{task_id}"):
                db.delete_task(task_id)
                st.rerun()