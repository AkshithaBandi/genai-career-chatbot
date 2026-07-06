# 🎓 GenAI Career Advisor Chatbot

A Production-Ready AI Career Guidance Chatbot built using **Google Gemini API**, **Streamlit**, and **Prompt Engineering**. The chatbot provides personalized career guidance, skill recommendations, placement preparation tips, resume advice, and AI/ML learning roadmaps through an interactive conversational interface.

# 📌 Project Overview

Choosing the right career path can be challenging for students and professionals. Traditional career counseling is often expensive, time-consuming, and not always accessible.

The **GenAI Career Advisor Chatbot** solves this problem by leveraging the power of **Generative AI** to provide personalized and context-aware career guidance.

The chatbot can:

- Suggest career paths based on user interests
- Recommend technical and non-technical skills
- Provide placement preparation strategies
- Offer resume improvement suggestions
- Generate AI/ML learning roadmaps
- Maintain conversation context using chat memory
- Export chat history as PDF

---

# 🚀 Features

### 🤖 AI-Powered Career Guidance
- Personalized career recommendations
- AI/ML roadmap generation
- Placement preparation advice
- Skill gap analysis

### 🧠 Context-Aware Conversations
- Multi-turn conversation memory
- Maintains context throughout chat

### 🔥 Prompt Engineering
- Structured system prompts
- Domain-specific career guidance responses

### 📄 PDF Export
- Download complete chat history as PDF

### 🌙 Dark Mode
- Toggle between light and dark themes

### ⚡ Production-Ready Features
- Secure API key handling
- Retry mechanism
- Fallback model support
- Error handling & logging

---

# 🏗️ System Architecture

```text
User
  │
  ▼
Streamlit Frontend
  │
  ▼
Prompt Builder
  │
  ▼
Chat Memory Module
  │
  ▼
Gemini API Integration
  │
  ▼
Response Generation
  │
  ▼
Streamlit UI
```

---

# 🧠 AI Models Used

### Primary Model
```python
gemini-2.5-flash
```

### Fallback Models
```python
gemini-flash-latest
gemini-2.0-flash
```

### Why Multiple Models?

To ensure uninterrupted service:

1. Try Gemini 2.5 Flash
2. If unavailable → Gemini Flash Latest
3. If unavailable → Gemini 2.0 Flash

This improves reliability during API overload situations.

---

# 🛠️ Tech Stack

## Frontend
- Streamlit

## Backend
- Python

## AI / LLM
- Google Gemini API
- Google GenAI SDK

## Libraries
- streamlit
- google-genai
- python-dotenv
- reportlab

## Deployment
- Streamlit Cloud

## Version Control
- Git
- GitHub

---

# 📂 Project Structure

```text
genai-career-chatbot/
│
├── assets/
│   ├── logo.png
│   ├── bot.png
│   └── user.png
│
├── config/
│   └── settings.py
│
├── memory/
│   └── session_memory.py
│
├── prompts/
│   └── system_prompt.py
│
├── services/
│   └── llm_service.py
│
├── utils/
│   └── logger.py
│
├── app.py
├── requirements.txt
├── README.md
├── .env
└── .gitignore
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/AkshithaBandi/genai-career-chatbot.git

cd genai-career-chatbot
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux / Mac

```bash
python -m venv .venv

source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

# ▶️ Run Locally

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

# ☁️ Deployment

## Streamlit Cloud

1. Push project to GitHub
2. Login to Streamlit Cloud
3. Create New App
4. Select repository
5. Add Secrets:

```toml
GEMINI_API_KEY = "YOUR_API_KEY"
```

6. Deploy

---

# 📸 Screenshots

## Home Page

<img width="1902" height="945" alt="Screenshot 2026-02-22 185339" src="https://github.com/user-attachments/assets/c76799e2-941d-4a25-9ebf-7284ec5c1cf7" />

## Career Guidance Chat

<img width="956" height="430" alt="Screenshot 2026-07-06 153513" src="https://github.com/user-attachments/assets/231c65f2-e630-4afa-bc0c-bf22bb9239d8" />


## Dark Mode

<img width="959" height="431" alt="Screenshot 2026-07-06 154208" src="https://github.com/user-attachments/assets/60849a70-d990-49e6-9153-009430780398" />

---

## PDF Export
<img width="301" height="383" alt="Screenshot 2026-07-06 153541" src="https://github.com/user-attachments/assets/67ceb94a-08f9-4161-b59d-9003dc8936b8" />


---

# 📊 Sample Questions

Try asking:

```text
How do I become an AI Engineer?

What skills are required for Data Science?

Create a roadmap for Machine Learning.

How should I prepare for placements?

Review my career options after BTech AIML.
```

---

# 🔥 Challenges Faced

### API Rate Limits

Gemini API occasionally returned:

```text
503 UNAVAILABLE
```

Solution:
- Implemented retry logic
- Added fallback models

---

### Deployment Challenges

AWS EC2 deployment faced:

- Environment variable issues
- API endpoint configuration conflicts

Final deployment completed successfully on Streamlit Cloud.

---

# 🚀 Future Enhancements

- Resume Analyzer
- Voice-Based Career Assistant
- User Authentication
- Personalized Career Dashboard
- Job Recommendation System
- Multi-Language Support
- Interview Preparation Module

---

# 📈 Learning Outcomes

Through this project I learned:

- Generative AI Application Development
- Prompt Engineering
- Multi-turn Conversation Design
- Cloud Deployment
- Secure API Management
- Error Handling Strategies
- Production-Ready AI Architecture

---

# 👨‍💻 Author

### Akshitha Dhakshayani

B.Tech – Artificial Intelligence & Machine Learning  

🔗 LinkedIn  
https://www.linkedin.com/in/akshitha-dhakshayani-57b0892bb/

🔗 GitHub  
https://github.com/AkshithaBandi

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---
