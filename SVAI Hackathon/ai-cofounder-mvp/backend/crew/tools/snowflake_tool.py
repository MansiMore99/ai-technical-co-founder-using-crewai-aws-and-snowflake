
import snowflake.connector
from backend.config import settings
from crewai_tools import tool

def _get_conn():
    if not (settings.SNOWFLAKE_ACCOUNT and settings.SNOWFLAKE_USER and settings.SNOWFLAKE_PASSWORD):
        raise RuntimeError("Snowflake credentials missing. Set SNOWFLAKE_* env vars.")
    return snowflake.connector.connect(
        account=settings.SNOWFLAKE_ACCOUNT,
        user=settings.SNOWFLAKE_USER,
        password=settings.SNOWFLAKE_PASSWORD,
        warehouse=settings.SNOWFLAKE_WAREHOUSE,
        database=settings.SNOWFLAKE_DATABASE,
        schema=settings.SNOWFLAKE_SCHEMA,
    )

@tool("query-snowflake")
def query_snowflake(sql: str, limit: int = 50) -> str:
    """Run a read-only SQL query against Snowflake and return first rows as TSV."""
    try:
        conn = _get_conn()
    except Exception as e:
        return f"ERROR: {e}"
    try:
        cur = conn.cursor()
        # Simple guard: forbid DML in this demo tool
        if any(k in sql.lower() for k in ["insert", "update", "delete", "merge", "create", "drop", "alter"]):
            return "ERROR: DML not allowed in demo tool."
        cur.execute(sql)
        cols = [c[0] for c in cur.description]
        rows = cur.fetchmany(limit)
        lines = ["\t".join(cols)]
        for r in rows:
            lines.append("\t".join("" if v is None else str(v) for v in r))
        return "\n".join(lines)
    finally:
        try:
            cur.close()
        except Exception:
            pass
        try:
            conn.close()
        except Exception:
            pass

@tool("get-latest-meeting-notes")
def get_latest_meeting_notes(limit: int = 1) -> str:
    """Return the latest N meeting notes from MEETING_NOTES table ordered by created_at desc."""
    sql = f"""
    SELECT id, title, content, created_at
    FROM MEETING_NOTES
    ORDER BY created_at DESC
    LIMIT {int(limit)}
    """
    return query_snowflake(sql, limit=limit)
