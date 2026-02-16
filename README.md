# Smart Factory Floor Assistant

**A multi-agent AI system for intelligent manufacturing operations using Google ADK**

Built with Google Agent Development Kit (ADK) and Gemini 2.5 Flash, this POC demonstrates how multiple specialized AI agents can coordinate to provide real-time factory floor intelligence.

---

## What It Does

The Smart Factory Floor Assistant answers complex manufacturing questions by orchestrating three specialist agents:

- **Production Monitor Agent** - Line status, OEE metrics, shift attainment
- **Maintenance Agent** - Fault diagnosis, error codes, SOPs, maintenance history  
- **Quality Agent** - Defect analysis, batch disposition, quality trends

### Example Queries

```
"Give me a complete shift status report"
→ Automatically coordinates all 3 agents to provide production, maintenance, and quality insights

"Line 3 is down with error code E-412. What's wrong?"
→ Maintenance agent provides root cause, corrective action, parts list, and safety procedures

"Should we release Batch B-2041?"
→ Quality agent analyzes defect rate and recommends disposition (RELEASE/REWORK/SCRAP)
```

---

## Architecture

```
Root Agent (factory_floor_agent)
├── Tool: get_shift_performance_report()
│
├── Production Monitor Agent
│   ├── get_production_status()
│   └── get_active_alarms()
│
├── Maintenance Agent
│   ├── get_fault_details()
│   └── get_maintenance_history()
│
└── Quality Agent
    └── get_quality_summary()
```

**6 Tools** accessing mock JSON data (easily replaced with real MES/ERP APIs)

---

## Mock Data

Realistic manufacturing scenarios for demos:

- **4 Production Lines** - Line_1 through Line_4 with OEE, targets, alarms
- **8 Error Codes** - Full diagnostics (E-412: Hydraulic failure, E-201: Conveyor issue, etc.)
- **6 Machines** - 30 maintenance events (preventive, corrective, emergency)
- **6 Quality Batches** - Varying defect rates (0.4% to 12.3%)

### Critical Issues in Demo Data
- Line_3: DOWN with E-412 (hydraulic pump failure)
- Line_4: Running but OEE 67% (below 70% threshold)
- Batch B-2041: 7.5% defect rate → REWORK needed
- Batch B-2044: 12.3% defect rate → SCRAP ($6,015 loss)

---

## Quick Start

### 1. Get Free API Key
Visit https://aistudio.google.com/apikey (no credit card needed!)

### 2. Install Dependencies
```bash
pip install google-adk>=0.5.0
```

### 3. Configure API Key
```bash
cp .env.example .env
# Edit .env and add your API key
```

### 4. Run the Assistant
```bash
adk web
```

Open http://localhost:8000 and select `factory_floor_agent`

---

## 🎬 Demo Queries

Copy these into the ADK web UI:

**Query 1 (Warm-up):**
```
Which production lines are currently running and which are down?
```

**Query 2 (Fault Diagnosis):**
```
Line 3 is down with error code E-412. What's wrong and what does the maintenance team need to do?
```

**Query 3 (Quality Decision):**
```
Should we release Batch B-2041? Give me your recommendation.
```

**Query 4 (Analysis):**
```
Line 4 has an OEE of 67%. Walk me through what that means and what we should investigate.
```

**Query 5 (🌟 THE SHOWSTOPPER - Multi-Agent):**
```
Give me a complete shift status report — production performance, any active faults, and quality summary. What are the top 3 things I need to act on right now?
```

**After Query 5, click the "Trace" tab** to see how the root agent coordinated all 3 specialists!

---

## 📁 Project Structure

```
smart_factory_poc/
├── .env.example              # API key template
├── .gitignore                # Protects .env from commits
├── requirements.txt          # google-adk>=0.5.0
├── SETUP_GUIDE.md           # Detailed setup instructions
├── QUICK_START.txt          # Visual quick start guide
├── test_agent_system.py     # Verification tests
├── data/                    # Mock manufacturing data
│   ├── production_lines.json
│   ├── machine_faults.json
│   ├── maintenance_history.json
│   └── quality_logs.json
└── factory_agent/           # Multi-agent system
    ├── __init__.py
    ├── tools.py             # 6 data access functions
    └── agent.py             # 4 ADK agents
```

---

## Cost

**$0** - Uses Gemini 2.5 Flash free tier via Google AI Studio

---

## Production Deployment

### Replace Mock Data with Real APIs

Edit `factory_agent/tools.py`:
```python
def get_production_status(line_id: str = "all") -> dict:
    # Replace this:
    data = load_json_data("production_lines.json")
    
    # With this:
    response = requests.get(f"{MES_API_URL}/lines/{line_id}")
    data = response.json()
```

### Deploy Options

**Recommended: Google Cloud Run**
```bash
# See deployment guide for full instructions
gcloud run deploy factory-assistant \
  --source . \
  --platform managed \
  --region us-central1
```

**Alternatives:**
- Railway.app (most Vercel-like)
- Render.com (free tier available)
- Fly.io (global edge deployment)

See deployment cost comparison in docs.

---

## 🛠️ Tech Stack

- **Google ADK** (Agent Development Kit) - Multi-agent orchestration
- **Gemini 2.5 Flash** - Fast, cost-effective LLM
- **Python 3.11+** - Backend
- **FastAPI** (via ADK) - Web server
- **JSON** - Mock data (replace with your MES/ERP)

---

## 📖 Documentation

- **SETUP_GUIDE.md** - Complete installation guide
- **QUICK_START.txt** - Visual quick start with demo queries
- **Deployment Guide** - Production deployment options (coming soon)

---

## Use Cases

**Perfect for:**
- Manufacturing POCs and demos
- Factory digitalization pilots
- MES/ERP system integration examples
- Multi-agent AI demonstrations
- Google ADK learning projects

**Next Steps:**
- Connect to real MES/ERP systems
- Add predictive maintenance models
- Integrate with SCADA systems
- Deploy to Vertex AI Agent Engine

---

## Acknowledgments

- Built with Google Agent Development Kit (ADK)
- Powered by Gemini 2.5 Flash
- Mock data designed for realistic manufacturing scenarios

---

## 📧 Questions?

Open an issue or check the SETUP_GUIDE.md for detailed instructions.

**Get your free API key:** https://aistudio.google.com/apikey

---

