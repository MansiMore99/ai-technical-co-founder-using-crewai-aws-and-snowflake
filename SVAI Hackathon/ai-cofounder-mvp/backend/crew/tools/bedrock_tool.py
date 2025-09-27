
# Optional placeholder illustrating how you'd wrap a Bedrock Agent invoke as a CrewAI tool.
# For this MVP we route through CrewAI's LLM directly in agent prompts, so this is not strictly required.
from crewai_tools import tool

@tool("ping-bedrock")
def ping_bedrock_tool(prompt: str) -> str:
    """Echo tool to demonstrate wiring."""
    return f"(bedrock echo) {prompt}"
