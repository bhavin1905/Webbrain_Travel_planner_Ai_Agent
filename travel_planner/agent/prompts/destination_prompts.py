def get_destination_knowledge_prompt(city, season):
    return f"""
    Provide comprehensive travel knowledge for {city}, focusing on:
    1. Cultural Background:
       - Historical significance
       - Local traditions and customs
       - Cultural etiquette tips
    
    2. Seasonal Information ({season}):
       - Weather conditions and what to pack
       - Seasonal festivals and events
       - Best times for different activities
    
    3. Travel Tips:
       - Local transportation options and costs
       - Safety considerations
       - Language essentials
       - Money-saving tips
       - Best areas to stay
    
    4. Experience Recommendations:
       - Must-try local dishes and where to find them
       - Hidden gems and local secrets
       - Photography spots
       - Shopping recommendations
    """

def get_itinerary_prompt(city, days, season, budget, interests, attractions, cuisine):
    return f"""
    Create a detailed {days}-day itinerary for {city} during {season} for a {budget}-budget traveler.
    
    Traveler Interests: {', '.join(interests)}
    Key Attractions: {', '.join(attractions)}
    Local Cuisine: {', '.join(cuisine)}
    
    For each day, provide:
    1. Morning activities and timing
    2. Afternoon exploration
    3. Evening activities
    4. Recommended restaurants and dishes
    5. Transportation between locations
    6. Estimated costs for activities
    7. Tips for the specific day
    
    Format: Use "Day X:" followed by structured timeline
    """

def get_weather_prompt(city, season):
    return f"""
    Provide detailed weather information for {city} during {season}:
    1. Temperature ranges
    2. Rainfall expectations
    3. Best outdoor activities
    4. What to pack
    5. Weather-related travel tips
    """