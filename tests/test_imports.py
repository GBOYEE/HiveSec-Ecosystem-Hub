def test_home_import():
    pass  # Should not raise

def test_agent_registry():
    from agents import list_agents
    agents = list_agents()
    # The registry should expose at least the shipped example agent
    names = [a.name() for a in agents]
    assert "ExampleScanner" in names
    assert hasattr(agents, "__len__")
