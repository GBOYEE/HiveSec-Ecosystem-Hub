# HiveSec Ecosystem Hub Architecture

## Structure

- **Hub (Streamlit app)**: central dashboard
- **Agent registry**: auto-discovers agents from `agents/` folder
- **Findings store**: SQLite (dev) or Postgres (prod) for scan results
- **Agents**: individual security scanners implementing `scan(target) -> List[Finding]`

## Agent Interface

```python
class Agent:
    def name(self) -> str: ...
    def scan(self, target: str) -> List[Finding]: ...
    def metadata(self) -> dict: ...
```

Add a new agent by dropping a file in `agents/` and restarting the dashboard.

## Data Model

Finding fields:
- `title`, `severity` (low/medium/high/critical)
- `description`, `evidence`, `agent_name`
- `timestamp`, `target`

## Deployment

Docker Compose includes optional Postgres profile:

```bash
docker compose --profile postgres up -d
```

## Scaling

For large fleets, use Postgres and enable Redis caching in Streamlit config.
