from agent.tools.destination_db import load_destinations, filter_destinations

def find_destinations(state):
    all_destinations = load_destinations()
    preferences = state.get("preferences", {})
    matched = filter_destinations(preferences, all_destinations)
    state["destinations"] = matched
    return state