# tests/test_plugin_manager.py

from app.plugin_manager import PluginManager

def test_plugin_loading():
    manager = PluginManager()
    manager.load_plugins()
    assert len(manager.plugins) > 0
    assert "MockPlugin" in manager.plugins
