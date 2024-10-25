import importlib
import os

class PluginManager:
    def __init__(self):
        self.plugins = {}

    def load_plugins(self):
        for filename in os.listdir("plugins"):
            if filename.endswith("_plugin.py"):
                plugin_name = filename[:-3]
                module = importlib.import_module(f"plugins.{plugin_name}")
                self.plugins[plugin_name] = module.Plugin()

    def get_plugin_commands(self):
        return {name: plugin for name, plugin in self.plugins.items()}

    def execute_plugin_command(self, command_name, *args):
        plugin = self.plugins.get(command_name)
        if plugin:
            return plugin.execute(*args)
        return None
