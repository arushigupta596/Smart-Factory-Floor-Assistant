# 🏭 Smart Factory Floor Assistant

A multi-agent manufacturing POC built with Google ADK (Agent Development Kit). Features 3 specialist agents orchestrated by a root agent, running completely free using Gemini's free tier.

## 🎯 Overview

This system simulates a smart factory monitoring assistant with:
- **Production Specialist Agent**: Monitors production lines, efficiency, and operations
- **Maintenance Specialist Agent**: Tracks machine faults and maintenance schedules
- **Quality Specialist Agent**: Analyzes quality inspections and defect trends
- **Root Orchestrator Agent**: Coordinates specialists and provides unified intelligence

## 📁 Project Structure

```
smart_factory_poc/
├── .env                          # API key configuration
├── requirements.txt              # Python dependencies
├── README.md                     # This file
├── data/                         # Mock factory data (simulates MES/ERP)
│   ├── production_lines.json    # Production line status & metrics
│   ├── machine_faults.json      # Machine fault records
│   ├── maintenance_history.json # Maintenance schedules & history
│   └── quality_logs.json        # Quality inspection data
└── factory_agent/
    ├── __init__.py
    ├── agent.py                 # Multi-agent system definition
    └── tools.py                 # Factory data access tools
```

## 🚀 Quick Start

### 1. Get a Free Google API Key

1. Visit [Google AI Studio](https://aistudio.google.com/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the key

### 2. Install Dependencies

```bash
cd smart_factory_poc
pip install -r requirements.txt
```

### 3. Configure API Key

Edit `.env` file and add your API key:

```bash
GOOGLE_API_KEY=your_actual_api_key_here
```

### 4. Run the Assistant

```bash
python -m factory_agent.agent
```

## 💬 Example Queries

Once running, try these questions:

**General Status:**
- "What's the factory status?"
- "Give me an overview of all production lines"
- "What's the overall efficiency?"

**Production Questions:**
- "What's the status of LINE-A2?"
- "Which production line is most efficient?"
- "Why is LINE-A2 running slower than target?"

**Maintenance Questions:**
- "Show me all open machine faults"
- "Any critical issues I should know about?"
- "What maintenance is scheduled this week?"
- "What's wrong with machine M005?"

**Quality Questions:**
- "Show me recent quality inspections"
- "Are there any failed inspections?"
- "What's the defect rate for LINE-A2?"
- "Which line has quality issues?"

**Cross-Functional Analysis:**
- "Why is LINE-A2 underperforming?" (triggers Production + Maintenance + Quality analysis)
- "What's affecting our efficiency today?"
- "Investigate the issues on LINE-B1"

## 🧠 How It Works

### Multi-Agent Architecture

```
┌─────────────────────────────────────────┐
│   Root Agent (Orchestrator)             │
│   - Routes queries to specialists       │
│   - Synthesizes multi-agent responses   │
│   - Provides factory overview           │
└─────────────────┬───────────────────────┘
                  │
        ┌─────────┼─────────┐
        │         │         │
        ▼         ▼         ▼
┌──────────┐ ┌──────────┐ ┌──────────┐
│Production│ │Maintenance│ │Quality   │
│Specialist│ │Specialist │ │Specialist│
└────┬─────┘ └────┬──────┘ └────┬─────┘
     │            │             │
     └────────────┴─────────────┘
                  │
          ┌───────▼────────┐
          │  Factory Tools  │
          │  (JSON Data)    │
          └────────────────┘
```

### Agent Responsibilities

**Root Agent:**
- Understands user intent
- Routes to appropriate specialist(s)
- Coordinates multi-specialist queries
- Provides context and actionable insights

**Production Specialist:**
- Production line monitoring
- Efficiency analysis
- Throughput tracking
- Operator information

**Maintenance Specialist:**
- Fault diagnosis
- Maintenance scheduling
- Equipment health
- Preventive maintenance

**Quality Specialist:**
- Inspection analysis
- Defect tracking
- Standards compliance
- Quality trends

### Data Tools

All agents access factory data through structured tools that simulate real MES/ERP system queries:

- `get_production_line_status()` - Line operations
- `get_line_efficiency()` - Performance metrics
- `get_machine_faults()` - Equipment issues
- `get_maintenance_history()` - Service records
- `get_quality_inspections()` - QA data
- `get_factory_overview()` - Overall status

## 🎨 Customization

### Add More Mock Data

Edit JSON files in `data/` directory to simulate different scenarios:
- Add more production lines
- Create new fault conditions
- Add inspection failures
- Schedule maintenance

### Add New Tools

In `factory_agent/tools.py`, create new functions and add them to specialist agents.

### Add New Specialist Agents

In `factory_agent/agent.py`, create a new specialist using `genai.Agent()` and add it to the root agent's `agents=[]` list.

### Modify Agent Personalities

Edit the `instructions` parameter in each agent's creation to change expertise and behavior.

## 📊 Mock Data Scenarios

The included data simulates a realistic factory scenario:

**Production Lines:**
- LINE-A1: Running at 95.8% efficiency
- LINE-A2: Running at 90% efficiency (sensor issue on M005)
- LINE-B1: Warning status (material feed issues)
- LINE-C1: Stopped for scheduled maintenance

**Active Issues:**
- M005: Temperature sensor malfunction (medium severity)
- M008: Material feed jamming (low severity)

**Quality Alerts:**
- LINE-A2: Failed inspection with 8% defect rate (above 5% threshold)

## 🔧 Troubleshooting

**"API Key not set" error:**
- Make sure `.env` file exists and contains your API key
- Check that the key is not "your_api_key_here"

**Import errors:**
- Run `pip install -r requirements.txt`
- Make sure you're in the project directory

**Agent not responding:**
- Check your internet connection (needs to reach Google's API)
- Verify API key is valid at [Google AI Studio](https://aistudio.google.com/apikey)

**"Model not found" error:**
- The free tier uses `gemini-2.0-flash-exp`
- Check [Google's model documentation](https://ai.google.dev/gemini-api/docs/models) for current available models

## 💡 Next Steps

**Enhance the POC:**
1. Add more data sources (inventory, supply chain, energy usage)
2. Create visualization dashboard
3. Add predictive analytics (predict failures, optimize schedules)
4. Implement write operations (create work orders, update schedules)
5. Add real-time data streaming simulation
6. Connect to actual MES/ERP systems

**Deploy for Real Use:**
1. Replace JSON files with database connections
2. Add authentication and authorization
3. Create web interface or Slack/Teams integration
4. Add audit logging and compliance tracking
5. Implement alerts and notifications

## 📝 License

This is a proof-of-concept demonstration. Modify and use as needed for your projects.

## 🤝 Contributing

This is a demo project, but feel free to fork and extend it! Ideas:
- Add more specialist agents (logistics, energy, safety)
- Create web UI with real-time updates
- Add data visualization charts
- Implement voice interface
- Create mobile app integration

---

**Built with:**
- [Google ADK](https://github.com/google/genai-sdk-python) - Agent Development Kit
- [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-v2) - Google's latest AI model
- Python 3.8+

**Zero Cost:** Runs entirely on Gemini's free tier! 🎉
