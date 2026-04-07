# HiveSec Ecosystem Hub — AI Security Dashboard

Centralized dashboard for monitoring and securing multi-agent systems.

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI](https://github.com/GBOYEE/HiveSec-Ecosystem-Hub/actions/workflows/ci.yml/badge.svg)](.github/workflows/ci.yml)
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](docker-compose.yml)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://gboyee.streamlit.app/HiveSec-Ecosystem-Hub)

## 🚀 What Problem This Solves

When running multiple AI agents or autonomous systems, you need visibility: which agents are active, what vulnerabilities or misalignments have been detected, and the ability to intervene quickly. Existing monitoring tools don't understand AI-specific risks. HiveSec provides a security-focused control plane for agent fleets.

## ⚙️ How It Works

- **Agent registry** auto-discovers agents from `agents/` folder
- **Real-time dashboard** shows alerts, agent status, and trends
- **Unified findings store** (SQLite/Postgres) aggregates scan results
- **Launch & monitor** — trigger scans and watch progress
- **Audit trails** — every action logged with timestamps

The system is built on Streamlit for rapid UI, with a plugin architecture for adding new security agents. Each agent implements a `scan()` function and returns standardized Finding objects.

## 📈 Why It Matters

- **Centralized visibility**: One pane for all your AI security agents
- **Rapid response**: Spot suspicious activity or failures instantly
- **Extensible**: Drop in new agents without touching the core
- **Production-ready**: Docker, health checks, CI, structured logging
- **Auditability**: Full logs for compliance and forensics

Result: You can operate AI agent fleets with confidence and oversight.

---

## ✨ Features

- **Agent registry** — Auto-discovers agents in `agents/` folder
- **Real-time KPI dashboard** — Alerts, agents status, trends
- **Unified findings store** — SQLite + optional Postgres
- **Launch & monitor** — Trigger scans and watch progress
- **Production ready** — Docker, health checks, CI, structured logging

---

## 🚀 Quick Start

```bash
# Clone and install
git clone https://github.com/GBOYEE/HiveSec-Ecosystem-Hub.git
cd HiveSec-Ecosystem-Hub
pip install -r requirements.txt

# Run the dashboard
streamlit run Home.py

# Open http://localhost:8501
```

---

## 🐳 Deployment

### Docker Compose (recommended)

```bash
docker-compose up -d
# Open http://localhost:8501
```

Includes optional PostgreSQL service (uncomment profile).

### Streamlit Cloud

Push to GitHub and deploy via Streamlit Community Cloud. Set secrets in the dashboard settings.

---

## 🔐 Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `DATABASE_URL` | `sqlite:///data/hub.db` | Database connection (SQLite or Postgres) |
| `STREAMLIT_SERVER_HEADLESS` | `true` | Run in headless mode (Docker) |

---

## 📡 Health Check

- Endpoint: `GET /healthz` returns "ok"
- Docker healthcheck enabled by default

---

## 🏗️ Architecture

```mermaid
flowchart TD
    UI[Streamlit Dashboard]
    REG[Agent Registry]
    DB[(Database)]
    AG1[Agent 1]
    AG2[Agent 2]
    AGN[Agent N]

    UI --> REG
    REG --> AG1 & AG2 & AGN
    AG1 & AG2 & AGN --> DB
    UI --> DB

    subgraph "Agents"
        AG1
        AG2
        AGN
    end
```

Agents auto-discovered from `agents/` folder. Each agent implements a common interface (`scan()`) and returns findings to the central store.

Detailed production architecture: [README-PRODUCTION.md](README-PRODUCTION.md#architecture)

---

## 🧩 Adding Agents

1. Create `agents/my_agent.py` implementing:
   - `name() -> str`
   - `scan(target: str) -> List[Finding]`
   - `metadata() -> dict`
2. Restart dashboard — auto-registered.
3. Optional: add icon to `assets/icons/`.

Template: `agents/EXAMPLE_AGENT.py`

---

## 🛠️ Development

```bash
# Hot reload
streamlit run Home.py --server.runOnSave true

# Lint
black .
flake8 .

# Type check
mypy . --ignore-missing-imports
```

Pre-commit hooks:
```bash
pre-commit install
```

CI runs on push.

---

## 🚢 Production

- Use Docker Compose for easy deployment
- For multi-user, switch to Postgres via `DATABASE_URL`
- Enable authentication via Streamlit secrets if needed
- Set `STREAMLIT_SERVER_PORT=8501` and reverse proxy with Nginx if desired

Full guide: [README-PRODUCTION.md](README-PRODUCTION.md)

---

## 📄 License

MIT — see [LICENSE](LICENSE).
