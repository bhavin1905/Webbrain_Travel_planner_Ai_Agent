from typing import List, Optional
from dataclasses import dataclass
from langchain_core.messages import BaseMessage

@dataclass
class AgentState:
    messages: List[BaseMessage]
    current_step: str
    preferences: Optional[dict] = None
    selected_destination: Optional[str] = None
    itinerary: Optional[List[dict]] = None