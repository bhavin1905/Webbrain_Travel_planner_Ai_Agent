
def handle_followup(state):
    history = state.get("history", [])
    itinerary = state.get("itinerary", {})
    followup_response = f"Sure! Here's a quick recap of your plan: {itinerary}"
    history.append(followup_response)
    state["history"] = history
    return state