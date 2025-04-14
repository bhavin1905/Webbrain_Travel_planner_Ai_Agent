from typing import Annotated, Sequence, TypeVar
from langgraph.graph import Graph, StateGraph
from langchain_core.messages import BaseMessage
from agent.state import AgentState
from agent.nodes import (
    understand_preferences,
    suggest_destinations,
    create_itinerary,
    answer_questions
)

def TravelPlannerGraph() -> Graph:
    # Create a new graph
    workflow = StateGraph(AgentState)
    
    # Add nodes to the graph
    workflow.add_node("understand_preferences", understand_preferences)
    workflow.add_node("suggest_destinations", suggest_destinations)
    workflow.add_node("create_itinerary", create_itinerary)
    workflow.add_node("answer_questions", answer_questions)
    
    # Define the edges
    workflow.add_edge("understand_preferences", "suggest_destinations")
    workflow.add_edge("suggest_destinations", "create_itinerary")
    workflow.add_edge("create_itinerary", "answer_questions")
    
    # Set the entry point
    workflow.set_entry_point("understand_preferences")
    
    # Compile the graph
    return workflow.compile()