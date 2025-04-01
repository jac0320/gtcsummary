from agents import Agent, Runner, WebSearchTool
import streamlit as st
from dotenv import load_dotenv
import argparse
import asyncio

# Initialize the OpenAI client
web_search = WebSearchTool()

web_search_gtc_agent = Agent(
    name="web_search_gtc_agent",
    instructions="""
    You are a specialized search agent focused on NVIDIA's GTC 2025 conference.
    Your primary tasks are to:
    1. Search for and analyze news, announcements, and products related to GTC 2025
    2. Track emerging trends and developments from the conference
    3. Focus on key areas including:
       - New GPU and AI hardware announcements
       - Software and framework updates
       - Industry partnerships and collaborations
       - AI and ML innovations
       - Gaming and graphics technology
       - Automotive and robotics developments
    
    When searching:
    - Prioritize official NVIDIA sources and reputable tech news outlets
    - Focus on recent and upcoming GTC 2025 related content
    - Provide concise, relevant summaries of findings
    - Include dates and sources in your responses
    """,
    tools=[web_search]
)

def search_gtc(query: str) -> str:
    """
    Wrapper function to search GTC 2025 related content.
    
    Args:
        query (str): The search query related to GTC 2025
        
    Returns:
        str: The search results and analysis
    """
    try:
        result = asyncio.run(Runner.run(web_search_gtc_agent, query))
        st.session_state.chat_messages.append({"role": "assistant", "content": result.final_output})
        return result.final_output
    except Exception as e:
        return f"An error occurred while searching: {str(e)}"