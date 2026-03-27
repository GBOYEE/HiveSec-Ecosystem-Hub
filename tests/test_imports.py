def test_home_import():
    import Home  # Should not raise

def test_agent_registry():
    from agents import registry
    assert hasattr(registry, "list_agents")
