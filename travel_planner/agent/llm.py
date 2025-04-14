import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage, SystemMessage

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROK_API"),
    model_name="gemma2-9b-it",
    temperature=0.7,
    max_tokens=4096
)

def get_llm_response(prompt, system_prompt=None):
    messages = []
    if system_prompt:
        messages.append(SystemMessage(content=system_prompt))
    messages.append(HumanMessage(content=prompt))
    
    try:
        response = llm.invoke(messages)
        return response.content
    except Exception as e:
        print(f"Error with LLM: {str(e)}")
        return "I apologize, but I encountered an error. Please try again."