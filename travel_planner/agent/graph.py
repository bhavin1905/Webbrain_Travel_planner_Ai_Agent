from langgraph.graph import StateGraph, END
from agent.state import PlannerState
from agent.nodes.extract_preferences import extract_preferences
from agent.nodes.find_destinations import find_destinations
from agent.nodes.create_itinerary import create_itinerary
from agent.nodes.handle_followup import handle_followup

def build_travel_planner_graph():
    graph = StateGraph(PlannerState)

    graph.add_node("extract_preferences", extract_preferences)
    graph.add_node("find_destinations", find_destinations)
    graph.add_node("create_itinerary", create_itinerary)
    graph.add_node("handle_followup", handle_followup)

    graph.set_entry_point("extract_preferences")
    graph.add_edge("extract_preferences", "find_destinations")
    graph.add_edge("find_destinations", "create_itinerary")

    graph.add_conditional_edges(
        "create_itinerary",
        lambda state: "handle_followup" if state.get("is_followup") else END
    )
    graph.add_edge("handle_followup", END)

    return graph.compile()