
import snowflake.connector
from backend.config import settings

SAMPLE_ROWS = [
    ("Weekly Sync - Product", "Decisions: Ship MVP by Friday. Actions: QA pass, pricing page. Risks: API rate limits, missing investor update."),
    ("Investor Call - Climate VC", "Notes: Interested in ARR > $10k MRR. Wants climate analytics angle. Action: send 1-pager. Risk: need Snowflake demo."),
    ("Customer Feedback - Alpha", "Users love dashboard; confused about onboarding. Action: add checklist. Risk: auth bug in SSO flow."),
]

def main():
    if not (settings.SNOWFLAKE_ACCOUNT and settings.SNOWFLAKE_USER and settings.SNOWFLAKE_PASSWORD):
        raise SystemExit("Set SNOWFLAKE_* env vars first.")
    conn = snowflake.connector.connect(
        account=settings.SNOWFLAKE_ACCOUNT,
        user=settings.SNOWFLAKE_USER,
        password=settings.SNOWFLAKE_PASSWORD,
        warehouse=settings.SNOWFLAKE_WAREHOUSE,
        database=settings.SNOWFLAKE_DATABASE,
        schema=settings.SNOWFLAKE_SCHEMA,
    )
    cur = conn.cursor()
    try:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS MEETING_NOTES (
          ID INTEGER AUTOINCREMENT,
          TITLE STRING,
          CONTENT STRING,
          CREATED_AT TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP()
        );""")
        for title, content in SAMPLE_ROWS:
            cur.execute(
                "INSERT INTO MEETING_NOTES (TITLE, CONTENT) VALUES (%s, %s)",
                (title, content)
            )
        print("Inserted sample rows.")
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    main()
