
from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    AWS_REGION: str = os.getenv("AWS_REGION", "us-west-2")
    AWS_ACCESS_KEY_ID: str | None = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY: str | None = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_SESSION_TOKEN: str | None = os.getenv("AWS_SESSION_TOKEN")
    BEDROCK_MODEL: str = os.getenv("BEDROCK_MODEL", "bedrock/anthropic.claude-3-5-sonnet-20241022-v2:0")

    SNOWFLAKE_ACCOUNT: str | None = os.getenv("SNOWFLAKE_ACCOUNT")
    SNOWFLAKE_USER: str | None = os.getenv("SNOWFLAKE_USER")
    SNOWFLAKE_PASSWORD: str | None = os.getenv("SNOWFLAKE_PASSWORD")
    SNOWFLAKE_WAREHOUSE: str = os.getenv("SNOWFLAKE_WAREHOUSE", "DEFAULT_WH")
    SNOWFLAKE_DATABASE: str = os.getenv("SNOWFLAKE_DATABASE", "DATAOPS_EVENT_PROD")
    SNOWFLAKE_SCHEMA: str = os.getenv("SNOWFLAKE_SCHEMA", "DEFAULT_SCHEMA")

    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8080"))

settings = Settings()
