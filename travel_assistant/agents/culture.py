from google.adk.agents import Agent

from travel_assistant.tools.culture_tools import get_local_culture_info

LocalCultureAgent = Agent(
    name="LocalCultureAgent",
    model="gemini-2.5-flash",
    description=(
        "Provides local culture information including typical dishes, "
        "customs, and useful phrases."
    ),
    instruction="""
You are an expert in local culture and traditions worldwide.
Your job is to provide relevant information about typical dishes,
social customs, and useful phrases for a specific destination.
Always use the 'get_local_culture_info' tool to retrieve accurate information.
Answer in Spanish.
""",
    tools=[get_local_culture_info],
)