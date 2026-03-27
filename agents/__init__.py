import importlib
import pkgutil
from pathlib import Path
from typing import List

class AgentInfo:
    def __init__(self, module):
        self._module = module
    def name(self):
        return getattr(self._module, "AGENT_NAME", self._module.__name__)
    def metadata(self):
        return getattr(self._module, "AGENT_METADATA", {})
    def scan(self, target: str):
        return self._module.scan(target)

def _iter_agent_modules():
    agents_dir = Path(__file__).parent
    for _, name, _ in pkgutil.iter_modules([str(agents_dir)]):
        if name.startswith("_"):
            continue
        yield importlib.import_module(f"agents.{name}")

def list_agents() -> List[AgentInfo]:
    return [AgentInfo(mod) for mod in _iter_agent_modules()]
