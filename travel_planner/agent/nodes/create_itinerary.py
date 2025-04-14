from agent.tools.weather_api import get_mock_weather
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
import json
import re

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

def create_itinerary(state):
    destinations = state.get("destinations", [])
    preferences = state.get("preferences", {})
    user_input = state.get("user_input", "")

    # ✅ Extract number of days from user input
    match = re.search(r"(\d+)\s*(day|days)", user_input.lower())
    num_days = int(match.group(1)) if match else 3

    # ✅ Extract city from input (simple heuristic)
    city_match = re.search(r"(?:travel|trip|visit|go to|in|to|for)\s+(?:to\s+)?([a-z\s]+)", user_input.lower())
    city = city_match.group(1).strip().title() if city_match else None


    # ✅ If matched destinations exist
    if destinations:
        chosen = destinations[0]
        weather = get_mock_weather(chosen["name"])

        itinerary = {
            "destination": chosen["name"],
            "days": [
                {"day": 1, "plan": f"Arrive in {chosen['name']} and explore local areas."},
                {"day": 2, "plan": f"Enjoy activities related to: {', '.join(chosen['tags'])}."}
            ],
            "weather": weather
        }

    else:
        # ✅ No match — ask OpenAI to generate plan based on extracted city and preferences
        prompt = f"""
You are a helpful travel assistant.

Your task is to generate a personalized {num_days}-day travel itinerary for the destination: **{city if city else 'any suitable place'}**.

🛑 Rules:
- If the user mentions a destination like "{city if city else 'unknown'}", you MUST use that exact city. Do not suggest or switch to another.
- If no city is mentioned, suggest a city based on the user's interests and budget.

✅ Itinerary Instructions:
- Each day should have a full "plan" (2–3 sentences).
- Include local experiences: sightseeing, food, culture, shopping, etc.
- No repetitive activities.
- The destination must match what the user asked (if provided).
- Return exactly {num_days} days.

🎯 User Input:
\"{user_input}\"

🔎 Extracted Preferences:
- Budget: {preferences.get("budget", "medium")}
- Interests: {', '.join(preferences.get("interests", []))}
- Destination: {city if city else "Not specified"}

📤 Return JSON ONLY like:
{{
  "destination": "{city if city else 'City Name'}",
  "days": [
    {{ "day": 1, "plan": "..." }},
    ...
    {{ "day": {num_days}, "plan": "..." }}
  ],
  "weather": "..."
}}
"""

        response = llm.invoke([HumanMessage(content=prompt)])
        try:
            content = response.content.strip().strip("```json").strip("```").strip()
            itinerary = json.loads(content)
            if city:
                itinerary["destination"] = city
        except Exception as e:
            itinerary = {"message": "We couldn't generate a custom itinerary. Try again."}

    state["itinerary"] = itinerary
    return state
