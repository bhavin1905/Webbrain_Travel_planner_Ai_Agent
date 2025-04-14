from .destination_prompts import *

class PromptHandler:
    @staticmethod
    def get_destination_suggestions(preferences):
        style_map = {
            "1": "cultural and heritage sites",
            "2": "nature and adventure activities",
            "3": "wellness and relaxation experiences",
            "4": "food and local experiences"
        }
        style = style_map.get(preferences.get("style", "1"))
        
        return f"""
        Suggest 3 ideal destinations for a traveler interested in {style}.
        For each destination, include:
        1. City and country name
        2. Why it's perfect for their interests
        3. Best time to visit
        4. Budget considerations
        5. Must-see attractions
        6. Unique experiences
        Format as a structured list with clear headings.
        """
    
    @staticmethod
    def get_followup_response(question, destination):
        return f"""
        Answer this question about {destination}:
        "{question}"
        
        Consider:
        1. Current season and weather
        2. Local customs and practices
        3. Practical travel tips
        4. Budget considerations
        5. Safety and health advice
        
        Provide detailed, actionable information.
        """