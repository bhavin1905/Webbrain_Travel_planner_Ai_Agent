from typing import Tuple
from langchain_core.messages import AIMessage
from agent.state import AgentState
from langchain_openai import ChatOpenAI

# Initialize the language model
llm = ChatOpenAI(temperature=0.7)

def understand_preferences(state: AgentState) -> AgentState:
    # Extract preferences from user input
    response = llm.invoke(state.messages[-1].content)
    state.preferences = {
        "parsed_preferences": response
    }
    state.messages.append(AIMessage(content=response))
    return state

def suggest_destinations(state: AgentState) -> AgentState:
    # Suggest destinations based on preferences
    prompt = f"Based on these preferences: {state.preferences}, suggest suitable destinations."
    response = llm.invoke(prompt)
    state.selected_destination = response
    state.messages.append(AIMessage(content=response))
    return state

def create_itinerary(state: AgentState) -> AgentState:
    # Create detailed itinerary
    prompt = f"Create a detailed itinerary for {state.selected_destination}"
    response = llm.invoke(prompt)
    state.itinerary = response
    state.messages.append(AIMessage(content=response))
    return state

def answer_questions(state: AgentState) -> AgentState:
    # Handle follow-up questions
    if len(state.messages) > 0 and "question" in state.messages[-1].content.lower():
        response = llm.invoke(state.messages[-1].content)
        state.messages.append(AIMessage(content=response))
    return state