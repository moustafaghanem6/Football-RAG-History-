import os
import requests
import streamlit as st
from dotenv import load_dotenv

def generate_rag_answer(query, retrieved_contexts):
    # محاولة جلب المفتاح من إعدادات Streamlit Cloud الآمنة أولاً، ثم ملف .env محلياً
    api_key = ""
    try:
        api_key = st.secrets["OPENROUTER_API_KEY"]
    except Exception:
        load_dotenv(override=True)
        api_key = os.getenv("OPENROUTER_API_KEY", "").strip()
        
    model_name = os.getenv("OPENROUTER_MODEL", "openai/gpt-4o-mini").strip()

    if not api_key:
        return "خطأ: لم يتم العثور على مفتاح OPENROUTER_API_KEY في إعدادات المنصة أو ملف .env"

    context_text = ""
    sources = set()
    
    for c in retrieved_contexts:
        context_text += f"- {c['content']}\n"
        sources.add(c['source'])
        
    prompt = f"""You are an expert Football AI Assistant. 
CRITICAL RULE: You are ONLY allowed to answer questions related to football (soccer), history of matches, players, teams, tournaments, and data provided in the context. 
If the user asks about any topic outside of football, you MUST politely refuse to answer.

Use the provided database context to answer accurately, and you can also use your general expert knowledge about football. Always cite your sources from the context if used. Support both Arabic and English seamlessly.

Context:
{context_text}

Question: {query}
"""

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": model_name,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload
        )
        res_json = response.json()
        if "choices" in res_json:
            answer = res_json["choices"][0]["message"]["content"]
            sources_str = ", ".join(sources) if sources else "General Football Knowledge"
            return f"{answer}\n\n**Sources:** {sources_str}"
        else:
            return f"Error from API: {res_json}"
    except Exception as e:
        return f"Error connecting to OpenRouter: {e}"
