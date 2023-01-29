from datetime import datetime
from os import makedirs, name, path, system
import json

class Art:
    def __init__(self):
        self.date = datetime.now()
    
    @property
    def daily(self):
        return f"""
        ___      _ _           ___ _                                  
        /   \__ _(_) |_   _    / __\ |__   ___   ___  ___  ___ _ __  
        / /\ / _` | | | | | |  / /  | '_ \ / _ \ / _ \/ __|/ _ \ '__|
        / /_// (_| | | | |_| | / /___| | | | (_) | (_) \__ \  __/ |   
        /___,' \__,_|_|_|\__, | \____/|_| |_|\___/ \___/|___/\___|_|
                        |___/   {self.date.day}/{self.date.month}/{self.date.year}                                     
        """

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def load_json(json_name):
    with open(f"src/data/{json_name}") as json_file:
        data = json.load(json_file)
    return data

def save_json(data, json_name):
    if not path.exists("src/data"):
        makedirs("src/data")
    with open(f"src/data/{json_name}", 'w') as json_file:
        json.dump(data, json_file)
