import streamlit as st
from agent import ask_ai
from canvas_utils import get_canvas_courses

st.set_page_config(page_title="GMU IST AI Student Assistant", layout="wide")
st.title("🎓 GMU IST Agentic AI Assistant")

# Sidebar login (mock)
st.sidebar.header("Login")
st.session_state["student_id"] = st.sidebar.text_input("GMU G Number", "G01234567")

# Navigation options
page = st.sidebar.radio("Navigation", ["Ask AI", "Course Planner", "Canvas Dashboard"])

if page == "Ask AI":
    st.subheader("💬 Ask a Question")
    user_query = st.text_input("Enter your question:")
    if st.button("Ask") and user_query:
        response = ask_ai(user_query)
        st.success(response)

elif page == "Course Planner":
    st.subheader("📘 Recommended Courses")
    st.info("(To be implemented) Based on IST major and course history at GMU.")

elif page == "Canvas Dashboard":
    st.subheader("📚 Your Canvas Courses")
    courses = get_canvas_courses(st.session_state["student_id"])
    if courses:
        for course in courses:
            st.markdown(f"**{course['name']}** – {course['term']}")
    else:
        st.warning("No courses found or Canvas not configured.")
