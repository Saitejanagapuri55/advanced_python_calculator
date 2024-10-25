# tests/test_plugin_manager.py
import pytest
from app.plugin_manager import PluginManager  # Ensure this is the correct class

def test_load_plugin():
    plugin_manager = PluginManager()
    plugin_manager.load_plugin("example_plugin")  # Adjust as per your plugin implementation
    assert plugin_manager.is_plugin_loaded("example_plugin") is True

def test_unload_plugin():
    plugin_manager = PluginManager()
    plugin_manager.load_plugin("example_plugin")
    plugin_manager.unload_plugin("example_plugin")
    assert plugin_manager.is_plugin_loaded("example_plugin") is False
