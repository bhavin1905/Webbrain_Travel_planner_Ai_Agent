import json
import os


def load_destinations():
    # Dynamically locate the data file
    filepath = os.path.join(os.path.dirname(__file__), "../../data/destinations.json")
    filepath = os.path.abspath(filepath)
    
    with open(filepath, "r") as f:
        return json.load(f)


def filter_destinations(preferences, destinations):
    matches = []
    for dest in destinations:
        if preferences.get("budget") and dest["budget_level"] != preferences["budget"]:
            continue
        if preferences.get("interests") and not any(tag in dest["tags"] for tag in preferences["interests"]):
            continue
        matches.append(dest)
    return matches
