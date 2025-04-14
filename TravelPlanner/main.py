from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

from langchain_core.messages import HumanMessage, AIMessage
from agent.graph import TravelPlannerGraph
from agent.state import AgentState

def main():
    # Verify API key is loaded
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY not found in environment variables")
    
    # Initialize the travel planner graph
    travel_planner = TravelPlannerGraph()
    
    # Example conversation
    user_input = "I want to plan a 5-day trip with a budget of $2000. I'm interested in historical sites and local cuisine."
    
    # Create initial state
    initial_state = AgentState(
        messages=[HumanMessage(content=user_input)],
        current_step="understand_preferences"
    )
    
    # Run the agent
    final_state = travel_planner.invoke(initial_state)
    
    # Print the final response
    print(final_state.messages[-1].content)

if __name__ == "__main__":
    main()