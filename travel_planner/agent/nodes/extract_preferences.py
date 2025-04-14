from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
import json

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

def extract_preferences(state):
    user_input = state["user_input"]

    messages = [
    SystemMessage(content="You are a helpful travel assistant."),
    HumanMessage(content=f"""
Extract travel preferences from the message below.

Return a JSON object with:
- "budget": one of "low", "medium", or "high"
- "interests": an array like ["beach", "culture", "history", "food", "shopping", "relaxation", "adventure", "romantic"]

User message:
\"{user_input}\"

Only return valid JSON. No explanation or markdown.
    """)
]


    response = llm.invoke(messages)

    try:
        # Sometimes model may wrap the response in markdown
        content = response.content.strip().strip("```json").strip("```").strip()
        preferences = json.loads(content)
    except json.JSONDecodeError:
        preferences = {"budget": "medium", "interests": []}

    state["preferences"] = preferences
    return state
