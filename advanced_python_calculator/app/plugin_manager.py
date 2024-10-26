# app/plugin_manager.py

class PluginManager:
    """Class to manage plugins."""
    
    def __init__(self):
        self.plugins = []

    def load_plugins(self):
        """Load plugins (dummy implementation)."""
        # For demonstration, we just append a mock plugin.
        self.plugins.append("MockPlugin")
