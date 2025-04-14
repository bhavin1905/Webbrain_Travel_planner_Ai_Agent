import unittest
from agent.graph import TravelPlannerGraph
from agent.state import AgentState
from langchain_core.messages import HumanMessage

class TestTravelPlannerAgent(unittest.TestCase):
    def setUp(self):
        self.travel_planner = TravelPlannerGraph()

    def test_basic_planning_flow(self):
        initial_state = AgentState(
            messages=[HumanMessage(content="I want to plan a 5-day trip to Rome with a $2000 budget")],
            current_step="understand_preferences"
        )
        final_state = self.travel_planner.invoke(initial_state)
        self.assertIsNotNone(final_state.preferences)
        self.assertIsNotNone(final_state.selected_destination)
        self.assertIsNotNone(final_state.itinerary)

if __name__ == '__main__':
    unittest.main()