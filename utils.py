from datetime import datetime
import json
from os import system, name

date = datetime.now()

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def loadJson(json_name):
    with open(json_name) as json_file:
        data = json.load(json_file)
    return data


def saveJson(data, json_name):
    with open(json_name, 'w') as json_file:
        json.dump(data, json_file)

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


arts = {
    'daily':
    f"""
    ___      _ _           ___ _                                  
   /   \__ _(_) |_   _    / __\ |__   ___   ___  ___  ___ _ __  
  / /\ / _` | | | | | |  / /  | '_ \ / _ \ / _ \/ __|/ _ \ '__|
 / /_// (_| | | | |_| | / /___| | | | (_) | (_) \__ \  __/ |   
/___,' \__,_|_|_|\__, | \____/|_| |_|\___/ \___/|___/\___|_|
                 |___/   {bcolors.OKBLUE}{date.day}/{date.month}/{date.year}{bcolors.ENDC}                                     
    """
}
