from typing import TypedDict, List, Dict, Any

class PlannerState(TypedDict, total=False):
    user_input: str
    preferences: Dict[str, Any]
    destinations: List[Dict[str, Any]]
    itinerary: Dict[str, Any]
    history: List[str]
    is_followup: bool