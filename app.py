import streamlit as st
import time
import os
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

from memory.session_memory import (
    initialize_memory,
    add_to_memory,
    get_memory
)
from services.llm_service import generate_response


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Career Advisor",
    page_icon="🎓",
    layout="wide"
)

initialize_memory()

# ---------------- DARK MODE SESSION STATE ----------------
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

# ---------------- SIDEBAR ----------------
with st.sidebar:

    st.image(os.path.join("assets", "logo.png"), width=120)
    st.title("AI Career Advisor")

    st.session_state.dark_mode = st.toggle(
        "🌙 Dark Mode",
        value=st.session_state.dark_mode
    )

    st.markdown("### 🚀 Features")
    st.markdown("""
    - 🎯 Placement Roadmaps  
    - 📊 AI/ML Career Planning  
    - 📄 Resume Guidance  
    - 🧠 Skill Recommendations  
    """)

    if st.button("🗑 Clear Chat"):
        st.session_state.chat_history = []

    st.markdown("---")
    st.markdown("### 📊 Usage Stats")
    st.write("Total Messages:", len(get_memory()))

    # Export Chat
    if st.button("📄 Export Chat as PDF"):
        def export_chat(chat_history):
            buffer = BytesIO()
            doc = SimpleDocTemplate(buffer)
            elements = []
            styles = getSampleStyleSheet()
            style = styles["Normal"]

            for msg in chat_history:
                text = f"{msg['role'].capitalize()}: {msg['content']}"
                elements.append(Paragraph(text, style))
                elements.append(Spacer(1, 0.3 * inch))

            doc.build(elements)
            buffer.seek(0)
            return buffer

        pdf = export_chat(get_memory())
        st.download_button(
            label="Download PDF",
            data=pdf,
            file_name="chat_history.pdf",
            mime="application/pdf"
        )

# ---------------- THEME STYLING ----------------
if st.session_state.dark_mode:
    background = "#0e1117"
    text_color = "#ffffff"
    card = "#1c1f26"
else:
    background = "#f4f6f9"
    text_color = "#000000"
    card = "#ffffff"

st.markdown(f"""
<style>
    .stApp {{
        background: linear-gradient(135deg, {background}, #1f4e79);
        color: {text_color};
    }}

    section[data-testid="stSidebar"] {{
        background-color: {card};
    }}

    .stChatMessage {{
        background-color: {card};
        border-radius: 12px;
        padding: 10px;
    }}

    h1, h2, h3, h4, h5, h6, p, div {{
        color: {text_color};
    }}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown(
    "<h1 style='text-align: center;'>🎓 AI Career Advisor</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center;'>Your intelligent mentor for placements & AI career growth.</p>",
    unsafe_allow_html=True
)

# ---------------- CHAT DISPLAY ----------------
for message in get_memory():
    if message["role"] == "assistant":
        with st.chat_message("assistant", avatar=os.path.join("assets", "bot.png")):
            st.markdown(message["content"])
    else:
        with st.chat_message("user", avatar=os.path.join("assets", "user.png")):
            st.markdown(message["content"])

# ---------------- USER INPUT ----------------
if prompt := st.chat_input("Ask your career question..."):

    add_to_memory("user", prompt)

    with st.chat_message("user", avatar=os.path.join("assets", "user.png")):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar=os.path.join("assets", "bot.png")):
        with st.spinner("Analyzing your profile..."):
            response = generate_response(get_memory())

            # Typing animation
            placeholder = st.empty()
            typed = ""
            for char in response:
                typed += char
                placeholder.markdown(typed)
                time.sleep(0.01)

    add_to_memory("assistant", response)