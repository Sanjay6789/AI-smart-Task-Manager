import os
from datetime import datetime
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from config.settings import GROQ_API_KEY, MODEL_NAME

# API Key set karna
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

def extract_task_details(user_input):
    """User ki normal language se Task aur Date nikalne ka function"""
    try:
        llm = ChatGroq(model=MODEL_NAME, temperature=0)
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are an AI assistant that extracts task info. "
                       "Output strictly in this format: Task Name | YYYY-MM-DD. "
                       "If no date is mentioned, use today's date: {current_date}. "
                       "Do not write any extra text, just the format."),
            ("user", "Extract task from: {input}")
        ])
        
        current_date = datetime.today().strftime('%Y-%m-%d')
        chain = prompt | llm
        response = chain.invoke({"input": user_input, "current_date": current_date})
        
        # Output parsing logic
        task_data = response.content.strip().split("|")
        task_name = task_data[0].strip()
        due_date = task_data[1].strip() if len(task_data) > 1 else current_date
        
        return task_name, due_date
    except Exception as e:
        # Agar AI fail ho toh fallback mechanism
        return user_input, datetime.today().strftime('%Y-%m-%d')