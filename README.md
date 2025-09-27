# secondBrain: AI Co-Founder — MVP (Snowflake + AWS Bedrock + FastAPI + Streamlit)
Build your own always-on AI co-founder—powered by **AWS**, **CrewAI**, and **Snowflake**—that reads your business documents, tracks meetings, analyzes investor and market data, and gives you smart, actionable advice for founders, CEOs, HR managers, and busy professionals—all in one place.

#### 🔧 Tech stack

* Frontend: Streamlit (simple chat UI)
* Backend: FastAPI (/chat endpoint)
* Orchestration: CrewAI Agent (single agent, single task)
* LLM: AWS Bedrock (Claude 3.5 Sonnet)
* Data: Snowflake (read-only queries)
* Infra Auth: Env variables (.env / shell exports)

#### Architecture:

```
Streamlit UI
    │  user message
    ▼
FastAPI /chat
    │  routes intent → targeted SQL (no free-form DB access)
    ▼
Snowflake (read)
    │  rows → compact JSON context
    ▼
CrewAI Agent (Claude via Bedrock)
    │  grounded reasoning on JSON snapshot
    ▼
Answer (bullets + next steps) → back to UI
```

#### 📊 Data model (demo tables)

BUSINESS_STRATEGY: COMPANY, MISSION, GOALS, RISKS
MEETING_NOTES: DATE, MEETING, NOTES, ACTION_ITEMS
INVESTORS: NAME, FIRM, STAGE_FOCUS, LAST_INVESTMENT, NOTES
MARKET_TRENDS: CATEGORY, YEAR, VALUATION, GROWTH_RATE
COMPETITORS: NAME, STATUS, VALUATION
STOCK_UPDATES: COMPANY, SYMBOL, PRICE, CHANGE
CALENDAR_EVENTS: DATE, TIME, EVENT, PARTICIPANTS, NOTES
CUSTOMER_FEEDBACK: CUSTOMER, FEEDBACK

The router only pulls the minimum needed rows per question to keep responses fast, cheap, and grounded.

#### ✅ Prerequisites

Python 3.10+
Snowflake access
Account: 
Warehouse: 
Database: 
Schema: 

AWS Bedrock permissions in us-west-2 (InvokeModel for Anthropic Claude)

### ⚙️ Setup

Install
```
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then edit values
```

#### ▶️ Run

**Backend (FastAPI)**
```
uvicorn app.server:app --reload --port 8000
```

**Frontend (Streamlit)**
```
export BACKEND_URL=http://127.0.0.1:8000/chat
streamlit run streamlit_app.py
```

#### 🔌 API (if you call it directly)

POST /chat
```
// Request
{ "message": "Who should we pitch next week?" }

// Response
{ "reply": "• Pitch Priya (Accel)…\n• Pitch Alex (Lightspeed)…\n\nNext 3 actions:\n1) Email intro…\n2) Update deck…\n3) Schedule demo…" }
```

#### 🧠 How it works (internals)

Streamlit sends your question to FastAPI /chat.
router.py does intent-based SQL (no free-form DB access).
Results become a compact JSON context.
agent.py (CrewAI + Bedrock) asks Claude to answer using only that context, returning bullets + next steps.


