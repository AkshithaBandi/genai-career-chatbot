# 🎓 AI Career Advisor Chatbot

A production-ready domain-specific chatbot built using Google Gemini 2.5 Flash API and Streamlit.

## 🚀 Features
- Multi-turn conversation memory
- Modular backend architecture
- Secure environment variable handling
- Gemini 2.5 Flash integration
- Dark/Light mode UI
- Export chat to PDF
- Retry handling for API load

## 🏗 Architecture

User  
→ Streamlit UI  
→ Backend Layer  
→ Prompt Module  
→ Gemini API  
→ Response Processing  
→ UI Rendering  

## 📦 Installation

1. Clone repository
2. Create virtual environment
3. Install dependencies:

pip install -r requirements.txt

4. Create `.env` file:

GEMINI_API_KEY=your_api_key_here

5. Run:

streamlit run app.py

## 📌 Tech Stack
- Python
- Streamlit
- Google Gemini API (gemini-2.5-flash)
- Clean modular architecture

## 🌍 Deployment
Designed for AWS EC2 deployment.
