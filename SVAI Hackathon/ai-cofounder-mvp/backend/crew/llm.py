
from crewai import LLM
from backend.config import settings

def bedrock_llm() -> LLM:
    # CrewAI will read AWS creds from environment.
    return LLM(
        model=settings.BEDROCK_MODEL,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        aws_region_name=settings.AWS_REGION,
        aws_session_token=settings.AWS_SESSION_TOKEN
    )
