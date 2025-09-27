
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.models.schemas import ChatRequest, ChatResponse
from backend.crew.agent import run_summarize_notes, run_stock_outlook, run_investor_scan

app = FastAPI(title="AI Co‑Founder Agent")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat", response_model=ChatResponse)
def chat(body: ChatRequest):
    q = body.message.strip()
    # Super‑simple intent router for the MVP:
    try:
        if "summarize" in q.lower() and "note" in q.lower():
            reply = run_summarize_notes()
            return ChatResponse(reply=reply, sources=["snowflake:MEETING_NOTES"])
        if "risk" in q.lower():
            # Reuse summarize; LLM will extract risks
            reply = run_summarize_notes()
            return ChatResponse(reply=reply, sources=["snowflake:MEETING_NOTES"])
        if "price" in q.lower() or "ticker" in q.lower():
            # naive ticker extraction
            import re
            m = re.search(r'\b([A-Za-z]{1,5})\b', q)
            ticker = m.group(1).upper() if m else "AAPL"
            reply = run_stock_outlook(ticker)
            return ChatResponse(reply=reply, sources=[f"market:{ticker}"])
        if "investor" in q.lower():
            # extract keyword after 'investor' or 'investors'
            kw = q.split("investor")[-1].strip() or "climate"
            reply = run_investor_scan(kw)
            return ChatResponse(reply=reply, sources=["snowflake:INVESTORS?"])
        # default to summarize notes
        reply = run_summarize_notes()
        return ChatResponse(reply=reply, sources=["snowflake:MEETING_NOTES"])
    except Exception as e:
        return ChatResponse(reply=f"Error: {e}")
