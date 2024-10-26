import os
import logging
import pandas as pd
from dotenv import load_dotenv
from app.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
from app.plugins import PluginManager

# Load environment variables
load_dotenv()
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Set up logging configuration
logging.basicConfig(level=LOG_LEVEL)
logger = logging.getLogger(__name__)

class CalculatorREPL:
    def __init__(self):
        self.history = pd.DataFrame(columns=["operation", "result"])
        self.commands = {
            "add": AddCommand(),
            "subtract": SubtractCommand(),
            "multiply": MultiplyCommand(),
            "divide": DivideCommand()
        }
        self.plugin_manager = PluginManager(self.commands)
        
    def start(self):
        print("Advanced Calculator. Type 'exit' to quit.")
        while True:
            command = input("> ").strip().lower()
            if command == "exit":
                break
            elif command == "history":
                print(self.history)
            elif command in self.commands:
                try:
                    result = self.commands[command].execute()
                    self.history = pd.concat([self.history, pd.DataFrame([[command, result]], columns=self.history.columns)])
                    logger.info(f"Executed {command} with result: {result}")
                    print(f"Result: {result}")
                except Exception as e:
                    logger.error(f"Error executing {command}: {e}")
                    print("Error: ", e)
            elif command == "menu":
                print("Available commands:", ", ".join(self.commands.keys()))
            else:
                print("Unknown command.")

if __name__ == "__main__":
    CalculatorREPL().start()
