def get_mock_weather(destination_name):
    return {
        "Paris": "Sunny with light showers",
        "Bali": "Tropical and warm"
    }.get(destination_name, "Weather data not available")