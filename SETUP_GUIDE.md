# Smart Factory Floor Assistant - Setup Guide

## ✅ STEP 1 — Get Your Free API Key

1. Visit: https://aistudio.google.com/apikey
2. Click "Create API Key"
3. Copy your key

**No credit card needed!** This is 100% free using Google AI Studio.

---

## ✅ STEP 2 — Configure Environment

Edit the `.env` file and replace `PASTE_YOUR_KEY_HERE` with your actual API key:

```bash
GOOGLE_API_KEY=AIza...your_actual_key_here
GOOGLE_GENAI_USE_VERTEXAI=FALSE
```

---

## ✅ STEP 3 — Install Dependencies

```bash
pip install google-adk>=0.5.0
```

---

## ✅ STEP 4 — Verify Installation

Test that the agent loads correctly:

```bash
python3 -c "from factory_agent.agent import root_agent; print('✅ Agent loaded:', root_agent.name)"
```

You should see: `✅ Agent loaded: factory_floor_agent`

---

## ✅ STEP 5 — Launch the ADK Web UI

```bash
adk web
```

This will start the development server at: **http://localhost:8000**

---

## ✅ STEP 6 — Run the 5 Demo Queries

Open http://localhost:8000 in your browser, select **factory_floor_agent** from the dropdown, and run these queries in order:

### Query 1 (Warm-up):
```
Which production lines are currently running and which are down?
```

### Query 2 (Fault Diagnosis):
```
Line 3 is down with error code E-412. What's wrong and what does the maintenance team need to do?
```

### Query 3 (Quality Decision):
```
Should we release Batch B-2041? Give me your recommendation.
```

### Query 4 (Analysis):
```
Line 4 has an OEE of 67%. Walk me through what that means and what we should investigate.
```

### Query 5 (THE SHOWSTOPPER — runs all 3 agents):
```
Give me a complete shift status report — production performance, any active faults, and quality summary. What are the top 3 things I need to act on right now?
```

---

## 🎯 What to Show Clients

1. **Run Query 5 first** — it's the most impressive
2. **Click 'Trace' in the UI** after it runs to show multi-agent coordination
3. **Point out** how one question triggered 3 specialist agents automatically

---

## 📊 Architecture Overview

### 3 Specialist Agents:
- **Production Monitor Agent**: Line status, OEE metrics, shift attainment
- **Maintenance Agent**: Fault diagnosis, error codes, maintenance history
- **Quality Agent**: Defect analysis, batch disposition, quality trends

### 1 Root Orchestrator Agent:
- **Factory Floor Agent**: Routes questions to specialists, synthesizes responses

### 6 Tools (Mock Data):
- `get_production_status()` - Production line metrics
- `get_active_alarms()` - Current alarms and down lines
- `get_fault_details()` - Error code lookup
- `get_maintenance_history()` - Machine maintenance records
- `get_quality_summary()` - Batch quality data
- `get_shift_performance_report()` - Comprehensive shift report

---

## 🚀 Next Steps to Productionize

1. Replace JSON file reads in `factory_agent/tools.py` with real MES/ERP API calls
2. Add `GOOGLE_GENAI_USE_VERTEXAI=TRUE` in `.env`
3. Deploy to Vertex AI Agent Engine
4. Same agents, same tools, real data!

---

## 🛠️ Troubleshooting

**Problem:** "Module not found: google.adk"  
**Fix:** `pip install google-adk`

**Problem:** "API key invalid or quota exceeded"  
**Fix:** Get a fresh key from https://aistudio.google.com/apikey — ensure `GOOGLE_GENAI_USE_VERTEXAI=FALSE` in `.env`

**Problem:** "root_agent not found"  
**Fix:** Ensure `factory_agent/__init__.py` contains `from . import agent` and `root_agent` is defined in `agent.py`

**Problem:** "Agent not routing to sub-agents"  
**Fix:** Check that `sub_agents=[production_monitor_agent, maintenance_agent, quality_agent]` is set on `root_agent`

**Problem:** "Tool returns empty data"  
**Fix:** Verify all 4 JSON files exist in the `data/` folder with correct names

**Problem:** Architecture mismatch error  
**Fix:** `pip install --upgrade --force-reinstall cryptography`

---

## 💰 Cost

**Zero cost!** Using Gemini 2.5 Flash free tier via Google AI Studio.

---

## 📁 Project Structure

```
smart_factory_poc/
├── .env                          # API key configuration
├── requirements.txt              # Dependencies
├── SETUP_GUIDE.md               # This file
├── data/                        # Mock manufacturing data
│   ├── production_lines.json   # 4 production lines
│   ├── machine_faults.json     # 8 error codes
│   ├── maintenance_history.json # 6 machines, 5 events each
│   └── quality_logs.json       # Shift summary + 6 batches
└── factory_agent/              # Agent system
    ├── __init__.py
    ├── tools.py                # 6 tool functions
    └── agent.py                # 4 agents (3 specialists + 1 root)
```
