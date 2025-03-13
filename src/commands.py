from plugins.bacis import BasicCommands
from plugins.system_utils import SystemUtils
from config import Config

class Commands:
    def __init__(self):
        self.basic_commands = BasicCommands()
        self.system_utils = SystemUtils()

        self.config = Config()
        self.commands = self.config.commands

    def handle_command(self, command: str):
        command_key = command.lower()

        if command_key in self.commands:
            command_function = eval(f"self.{self.commands[command_key]}")
            command_function()
        else:
            self.basic_commands.speak_engine.say("Команда не найдена")