from dotenv import load_dotenv
import os
load_dotenv()  # ✅ Load .env into environment

from agent.graph import build_travel_planner_graph


def run_planner(user_input: str, is_followup=False):
    workflow = build_travel_planner_graph()
    state = {
        "user_input": user_input,
        "is_followup": is_followup,
        "history": []
    }
    result = workflow.invoke(state)
    return result


if __name__ == "__main__":
    user_input = input("Describe your ideal trip: ")
    final_state = run_planner(user_input)
    print("\n🌍 --- Trip Plan ---")
itinerary = final_state.get("itinerary", {})

if "message" in itinerary:
    print(f"⚠️ {itinerary['message']}")
else:
    print(f"\n📍 Destination: {itinerary.get('destination', 'Unknown')}")
    print(f"🌤️ Weather Forecast: {itinerary.get('weather', 'N/A')}")

    print("\n🗓️ Day-by-Day Itinerary:")
    for day_plan in itinerary.get("days", []):
        day = day_plan.get("day", "N/A")
        plan = day_plan.get("plan", "No plan provided.")
        print(f"  \n🗓️ Day {day}: {plan}")

