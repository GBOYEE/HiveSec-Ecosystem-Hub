import streamlit as st
import sqlite3
import logging
from pathlib import Path
from agents import list_agents

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("hivesec_hub")

# Page config
st.set_page_config(page_title="HiveSec Hub", layout="wide")
st.title("🛡️ HiveSec Ecosystem Hub")

# Health check endpoint (for /healthz)
if st.query_params.get("healthz"):
    st.write("ok")
    st.stop()

DB_PATH = Path("data/hub.db")
DB_PATH.parent.mkdir(exist_ok=True)

# Initialize DB if not exists
try:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS findings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        agent TEXT,
        severity TEXT,
        title TEXT,
        description TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()
    logger.info("Database initialized")
except Exception as e:
    logger.error("Database init failed: %s", e)

st.header("Agents")
try:
    agents = list_agents()
    if not agents:
        st.info("No agents found in agents/ folder.")
    for agent in agents:
        st.subheader(agent.name())
        st.write(f"**Capabilities:** {', '.join(agent.metadata().get('capabilities', []))}")
        if st.button(f"Launch {agent.name()}", key=f"launch_{agent.name()}"):
            logger.info("Launch requested: %s", agent.name())
            st.success(f"Launched {agent.name()}! (demo)")
except Exception as e:
    logger.error("Agent listing failed: %s", e)
    st.error("Failed to load agents.")

st.header("Recent Findings")
try:
    conn = sqlite3.connect(DB_PATH)
    import pandas as pd
    df = pd.read_sql("SELECT * FROM findings ORDER BY timestamp DESC LIMIT 10", conn)
    conn.close()
    st.dataframe(df, use_container_width=True)
except Exception as e:
    logger.error("Failed to load findings: %s", e)
    st.error("Could not load findings.")

st.markdown("---")
st.caption("Powered by Streamlit & Xander Hive")
