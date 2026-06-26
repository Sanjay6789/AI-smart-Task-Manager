# 📝 AI-Powered Smart Task Manager

A professional Full-Stack AI application that extracts tasks and deadlines from natural language using LangChain, Groq (Llama-3.1), and Streamlit.

## 🚀 Features
- *Natural Language Processing*: Automatically extracts task names and due dates.
- *Modular Architecture*: Separate concerns for Frontend, Backend Services, Configuration, and Database.
- *Secure Configuration*: Uses environment variables (.env) for safe API management.
- *Relational Database*: Stores tasks locally using SQLite3.

## 🛠️ Tech Stack
- *Frontend*: Streamlit
- *LLM Orchestration*: LangChain Core / LangChain Groq
- *Model*: Llama-3.1-8b-instant
- *Database*: SQLite3

## 📦 Installation & Setup
1. Clone the repository and navigate to the project folder.
2. Install dependencies:
   bash
   pip install -r requirements.txt
   
3. Create a .env file in the root directory and add your key:
   text
   GROQ_API_KEY=your_groq_api_key_here
   
4. Run the application:
   bash
   streamlit run app.py
   