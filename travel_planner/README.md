# Travel Planner AI Agent

A sophisticated AI-powered travel planning assistant built with LangGraph and Grok LLM.

## Overview

This Travel Planner AI agent helps users plan trips by understanding their preferences, suggesting destinations, creating itineraries, and answering follow-up questions. It demonstrates the implementation of a multi-step reasoning workflow using the LangGraph library.

## Features

- **Preference Extraction**: Analyzes user input to understand travel preferences (budget, duration, interests, etc.)
- **Destination Recommendations**: Suggests appropriate destinations based on user preferences
- **Itinerary Creation**: Generates detailed day-by-day travel plans
- **Follow-up Question Handling**: Responds intelligently to questions about the suggested plans
- **Weather Information**: Provides weather forecasts for destinations (mock implementation)

## Project Structure

```
travel_planner/
├── main.py                  # Entry point for the application
├── agent/
│   ├── graph.py             # LangGraph implementation
│   ├── nodes/               # Node implementations for each step
│   ├── tools/               # External tool connections
│   └── state.py             # State management
├── data/
│   └── destinations.json    # Mock destination database
├── tests/
│   └── test_agent.py        # Test cases
└── README.md                # Documentation
```

## Technical Implementation

### LangGraph Framework

The agent is built as a directed graph using LangGraph with the following nodes:

1. **PreferenceExtractor**: Extracts travel preferences from user input
2. **DestinationFinder**: Finds suitable destinations based on preferences
3. **ItineraryCreator**: Creates a detailed itinerary for the selected destination
4. **FollowUpHandler**: Handles follow-up questions about the plan

### State Management

The agent uses a Pydantic-based state object to track:
- User preferences
- Selected destinations
- Current itinerary
- Conversation history
- Weather information

### External Tools

The agent integrates with:
- **Destination Database**: A JSON-based database of travel destinations
- **Weather API**: A mock weather service providing forecasts for destinations

### Grok LLM Integration

The agent uses the Grok LLM model (mixtral-8x7b) for natural language understanding and generation across all nodes.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Required packages: langgraph, langchain, langchain_community, pydantic

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/travel-planner.git
cd travel-planner
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

To start the travel planner:

```bash
python main.py
```

### Running Tests

To run the test suite:

```bash
python -m unittest discover tests
```

## Example Conversation

```
🌍 Welcome to the Travel Planner AI Assistant! 🌍
Tell me about your travel preferences, and I'll help you plan the perfect trip.

You: I want to go on a beach vacation for 1 week in the summer with my partner. We enjoy food, swimming, and relaxing. Our budget is medium.

Travel Assistant: Based on your preferences for a 1-week beach vacation in summer with a medium budget, I recommend these destinations:

1. Bali, Indonesia
   Bali offers beautiful beaches, vibrant culture, and excellent value for money. Summer temperatures range from 23°C-31°C with relatively dry conditions. You can enjoy beach relaxation at Kuta or Seminyak, explore sacred temples like Tanah Lot, and indulge in affordable yet delicious Indonesian cuisine. The island has plenty of mid-range accommodations perfect for couples.

2. Barcelona, Spain
   Barcelona combines urban excitement with fantastic Mediterranean beaches. Summer is hot and sunny (20°C-28°C), perfect for enjoying Barceloneta Beach. You and your partner can explore Gothic Quarter, marvel at Gaudi's architecture, and enjoy amazing tapas and seafood. The city offers excellent public transportation and good value accommodations.

3. Bangkok, Thailand
   While not directly on the beach, Bangkok is a budget-friendly gateway to Thailand's stunning islands. Even during the summer monsoon season, you'll find plenty of sunny days with warm temperatures (25°C-33°C). The city offers incredible street food, vibrant markets, and easy connections to beach destinations like Pattaya or Hua Hin for day trips.

Would you like me to create a detailed itinerary for any of these destinations?

You: Let's go with Bali. Can you create an itinerary?

Travel Assistant: [Detailed Bali itinerary with day-by-day activities]

You: What's the best way to get around in Bali?

Travel Assistant: [Information about transportation options in Bali]
```

## Extending the Agent

To extend this agent, you might consider:

1. Integrating with real weather APIs and destination databases
2. Adding flight and accommodation booking recommendations
3. Implementing user preference learning across sessions
4. Adding multi-destination trip planning capabilities
5. Integrating with maps and travel time estimation services

## License

This project is licensed under the MIT License - see the LICENSE file for details.