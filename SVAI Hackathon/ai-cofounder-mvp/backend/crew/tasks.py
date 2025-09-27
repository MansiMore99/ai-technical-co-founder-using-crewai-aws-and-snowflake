
from crewai import Task

def summarize_notes_task():
    return Task(
        description=(
            "Summarize the latest meeting notes from the Snowflake 'MEETING_NOTES' table. "
            "Provide key decisions, action items, and risks. If Snowflake is not available, "
            "explain that credentials are missing."
        ),
        expected_output="A concise, bulleted summary with 3-5 bullets."
    )

def stock_outlook_task(ticker: str):
    return Task(
        description=(
            f"Fetch the current price and 1-sentence outlook for {ticker}. "
            "Use the Market tool to get a current price and a headline."
        ),
        expected_output="One paragraph with the price and a succinct outlook."
    )

def investor_scan_task(keyword: str):
    return Task(
        description=(
            f"Scan Snowflake investors/documents mentioning '{keyword}' and summarize findings. "
            "If unavailable, explain missing configuration."
        ),
        expected_output="A short summary with any matching names and insights."
    )
