AGENT_NAME = "ExampleScanner"
AGENT_METADATA = {
    "capabilities": ["scan:example"],
    "description": "Demo agent that finds example issues."
}

def scan(target: str):
    # In a real agent, this would perform actual scanning
    # Here we return a fake finding for demo
    return [{
        "agent": AGENT_NAME,
        "severity": "low",
        "title": "Example finding",
        "description": f"This is a demo finding for target {target}."
    }]
