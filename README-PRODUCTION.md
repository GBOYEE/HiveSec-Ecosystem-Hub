# HiveSec Ecosystem Hub — Production Guide

Deploy and operate the Streamlit security dashboard in production.

## Architecture

```mermaid
graph TD
    User --> LB[Nginx/Reverse Proxy]
    LB --> Streamlit[Streamlit App]
    Streamlit --> DB[(Database)]
    Streamlit --> Agents[Agent Modules]
    Agents --> DB

    subgraph "Docker Compose"
        Streamlit
        DB[(Postgres)]
    end
```

Components:
- **Streamlit UI** (`Home.py`) — main dashboard
- **Agent Registry** — discovers modules in `agents/`
- **Findings Store** — SQLite (default) or PostgreSQL
- **Docker** — containerized deployment

---

## Deployment Options

### Docker Compose (recommended)

```bash
# Clone and start
git clone https://github.com/GBOYEE/HiveSec-Ecosystem-Hub.git
cd HiveSec-Ecosystem-Hub
docker-compose up -d

# Open http://localhost:8501
```

To enable Postgres, edit `docker-compose.yml` and remove `profiles: ["postgres"]` from the postgres service, then run `docker-compose up -d`.

### Streamlit Community Cloud

1. Push to GitHub
2. Create new app on share.streamlit.io
3. Set main file: `Home.py`
4. Add secrets (if needed) in dashboard settings

### VPS (systemd)

Create systemd unit:

```ini
[Unit]
Description=HiveSec Hub
After=network.target

[Service]
Type=simple
User=hivesec
WorkingDirectory=/opt/hivesec
Environment="DATABASE_URL=sqlite:///data/hub.db"
ExecStart=/usr/local/bin/streamlit run Home.py --server.port 8501 --server.address 127.0.0.1
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

Then `systemctl enable --now hivesec-hub`.

---

## Configuration

### Database

Default SQLite file: `data/hub.db`

For PostgreSQL, set `DATABASE_URL`:

```
postgresql://user:pass@localhost/hivesec
```

Make sure to run migrations (the app creates tables automatically on first run).

### Secrets

Streamlit secrets (`.streamlit/secrets.toml`) for sensitive values:

```toml
# .streamlit/secrets.toml
database_url = "postgresql://..."
```

Access via `st.secrets["database_url"]`.

---

## Observability

### Health Check

`GET /healthz` returns plain text "ok". Used by Docker healthcheck.

### Logs

Streamlit logs to stdout. Capture via Docker `logs` or systemd `journalctl`.

Example:
```bash
docker-compose logs -f hub
journalctl -u hivesec-hub -f
```

---

## Upgrading

1. Pull latest code: `git pull`
2. Rebuild containers: `docker-compose build --pull`
3. Restart: `docker-compose up -d`

Backup `data/` directory regularly.

---

## Security

- Run container with non-root user (add `user: 1000:1000` in compose)
- Use strong database passwords
- Enable HTTPS via reverse proxy (Nginx) with TLS
- Restrict access via firewall or VPN if needed

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Database locked | Ensure proper file permissions on `data/` volume |
| Agents not showing | Check `agents/` folder exists and modules are importable |
| Port 8501 in use | Change `STREAMLIT_SERVER_PORT` or compose port mapping |
| Health check failing | Ensure `Home.py` handles `/healthz` query param correctly |

---

## License

MIT — see `LICENSE`.
