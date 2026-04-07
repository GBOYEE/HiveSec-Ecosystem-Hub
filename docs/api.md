# HiveSec Ecosystem Hub API

The dashboard is primarily a Streamlit UI, but you can query findings programmatically:

```python
from hivehub.db import get_findings

findings = get_findings(severity="high", days=7)
```

Database schema is in `db/models.py`.

## Endpoints (if running in API mode)

No public API yet. The dashboard reads directly from the findings store.

To add an API, extend `app/api/` (FastAPI) and protect with authentication.
