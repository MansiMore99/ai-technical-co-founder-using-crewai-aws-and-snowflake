
from crewai import Agent, Crew
from backend.crew.llm import bedrock_llm
from backend.crew.tasks import summarize_notes_task, stock_outlook_task, investor_scan_task
from backend.crew.tools.snowflake_tool import get_latest_meeting_notes, query_snowflake
from backend.crew.tools.market_tool import get_stock_price, get_market_headline

# Create a single "AI Co‑Founder" agent with attached tools
def build_crew():
    agent = Agent(
        role='AI Co‑Founder',
        goal='Help founders by reading business data and giving advice',
        backstory='A reliable co‑founder who reads your docs, tracks meetings, and knows markets.',
        tools=[get_latest_meeting_notes, query_snowflake, get_stock_price, get_market_headline],
        llm=bedrock_llm(),
        verbose=True
    )
    return Crew(agents=[agent], tasks=[]), agent

def run_summarize_notes():
    crew, agent = build_crew()
    task = summarize_notes_task()
    crew.tasks = [task]
    result = crew.kickoff()
    return str(result)

def run_stock_outlook(ticker: str):
    crew, agent = build_crew()
    task = stock_outlook_task(ticker)
    crew.tasks = [task]
    result = crew.kickoff()
    return str(result)

def run_investor_scan(keyword: str):
    crew, agent = build_crew()
    task = investor_scan_task(keyword)
    crew.tasks = [task]
    result = crew.kickoff()
    return str(result)
