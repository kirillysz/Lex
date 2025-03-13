import json
import os

class Config:
    def __init__(self):
        self.config_path = self.find_config_file("configs")
        self.commands = self.load_commands()

    def find_config_file(self, search_dir):
        for root, dirs, files in os.walk(search_dir):
            if "config.json" in files:
                return os.path.join(root, "config.json")
        raise FileNotFoundError("config.json file not found")

    def load_commands(self):
        with open(self.config_path, 'r', encoding='utf-8') as file:
            config = json.load(file)

            return config.get("commands", {})