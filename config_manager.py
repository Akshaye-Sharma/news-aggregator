import json
import os

CONFIG_FILE = "config.json"

def is_first_run(config: dict) -> bool:
    return config.get("first_run", True)

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)

def load_config():
    if not os.path.exists(CONFIG_FILE):
        # File doesn’t exist → fresh defaults
        config = {"first_run": True, "api_key": ""}
        save_config(config)
        return config

    try:
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
    except (json.JSONDecodeError, ValueError):
        # File exists but is empty or corrupted → reset to defaults
        config = {"first_run": True, "api_key": ""}
        save_config(config)

    return config