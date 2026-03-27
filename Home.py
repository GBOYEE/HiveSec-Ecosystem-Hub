import streamlit as st
import sqlite3
from pathlib import Path
from agents import list_agents

st.set_page_config(page_title="HiveSec Hub", layout="wide")
st.title("🛡️ HiveSec Ecosystem Hub")

DB_PATH = Path("data/hub.db")
DB_PATH.parent.mkdir(exist_ok=True)

# Initialize DB if not exists
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

st.header("Agents")
agents = list_agents()
for agent in agents:
    st.subheader(agent.name())
    st.write(f"**Capabilities:** {', '.join(agent.metadata().get('capabilities', []))}")
    if st.button(f"Launch {agent.name()}", key=agent.name()):
        st.info("Launched! (demo)")

st.header("Recent Findings")
conn = sqlite3.connect(DB_PATH)
import pandas as pd
df = pd.read_sql("SELECT * FROM findings ORDER BY timestamp DESC LIMIT 10", conn)
conn.close()
st.dataframe(df, use_container_width=True)

st.markdown("---")
st.caption("Powered by Streamlit & Xander Hive")
