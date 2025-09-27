# AI Technical Co‑Founder using CrewAI, AWS, and Snowflake

Build your own always-on AI co-founder—powered by AWS, CrewAI, and Snowflake—that reads your business documents, tracks meetings, analyzes investor and market data, and gives you smart, actionable advice for founders, CEOs, HR managers, and busy professionals—all in one place.

## Overview

This is a minimal, runnable MVP that includes:
- **FastAPI backend** that wraps a **CrewAI agent** powered by **Amazon Bedrock** and
  two tools: **Snowflake query tool** and a **Stocks/News tool**.
- **Simple web UI** (plain HTML/JS) to chat with your AI co‑founder.
- **Sample Snowflake table + loader** so the agent can summarize "meeting notes".

> **No secrets are included.** Configure via `.env` using the provided `.env.example` file.

## Quick Start

### 1) Python env & deps
```bash
cd backend
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # and fill values
```

### 2) (Optional) Load sample data into Snowflake
```bash
python scripts/load_sample_data.py
```

### 3) Run the backend
```bash
uvicorn app:app --host 0.0.0.0 --port 8080 --reload
```

### 4) Open the UI
Open `frontend/index.html` in your browser (or serve it with any static server).
By default it posts to `http://localhost:8080/chat`.

---

## What’s inside

```
ai-cofounder-mvp/
├─ backend/
│  ├─ app.py                     # FastAPI app with /chat endpoint
│  ├─ config.py                  # Env settings
│  ├─ requirements.txt
│  ├─ .env.example               # Copy to .env and fill
│  ├─ models/
│  │  └─ schemas.py              # Pydantic request/response schemas
│  ├─ crew/
│  │  ├─ llm.py                  # Bedrock LLM config for CrewAI
│  │  ├─ agent.py                # CrewAI agent + crew wiring
│  │  ├─ tasks.py                # Task templates used by the agent
│  │  └─ tools/
│  │     ├─ bedrock_tool.py      # BedrockInvokeAgentTool wrapper (optional helper)
│  │     ├─ snowflake_tool.py    # Query Snowflake (meeting notes, investor data)
│  │     └─ market_tool.py       # Latest stock price & headlines (demo)
│  └─ scripts/
│     ├─ load_sample_data.py     # Creates table + loads sample notes
│     └─ init_snowflake.sql      # DDL for demo table
└─ frontend/
   ├─ index.html                 # Minimal chat UI
   ├─ app.js                     # Calls backend /chat
   └─ styles.css
```

---

## Demo Prompts to Try

- *"Summarize my latest meeting notes."*  
- *"List top 3 risks from last week’s notes."*  
- *"What’s the current price and 1‑sentence outlook for AAPL?"*  
- *"Find investors in my Snowflake table mentioning 'climate' and summarize."*

> If Snowflake isn’t configured, the agent will still answer but will note missing credentials.

---

## Notes

- This MVP uses **CrewAI** orchestration with Bedrock as the LLM provider (via `crewai.LLM`).
- The **Snowflake tool** runs parameterized SQL to avoid injection.
- The **Market tool** demonstrates simple retrieval (price + headlines) using public libs.
- Replace or extend tools as needed (CRM lookups, email, calendars, etc.).

---

## Notes

- This MVP uses **CrewAI** orchestration with Bedrock as the LLM provider (via `crewai.LLM`).
- The **Snowflake tool** runs parameterized SQL to avoid injection.
- The **Market tool** demonstrates simple retrieval (price + headlines) using public libs.
- Replace or extend tools as needed (CRM lookups, email, calendars, etc.).
