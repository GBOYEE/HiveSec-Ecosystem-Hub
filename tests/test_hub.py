def test_home_import():
    import Home  # should not raise

def test_agent_listing():
    from agents import list_agents
    agents = list_agents()
    # At least the example agent should be present
    names = [a.name() for a in agents]
    assert "ExampleScanner" in names
