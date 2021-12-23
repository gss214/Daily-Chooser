from datetime import datetime

date = datetime.now()


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
    ___      _ _           ___ _                                 ____    ___  
   /   \__ _(_) |_   _    / __\ |__   ___   ___  ___  ___ _ __  |___ \  / _ \ 
  / /\ / _` | | | | | |  / /  | '_ \ / _ \ / _ \/ __|/ _ \ '__|   __) || | | |
 / /_// (_| | | | |_| | / /___| | | | (_) | (_) \__ \  __/ |     / __/ | |_| |
/___,' \__,_|_|_|\__, | \____/|_| |_|\___/ \___/|___/\___|_|    |_____(_)___/ 
                 |___/                   {bcolors.OKBLUE}{date.day}/{date.month}/{date.year}{bcolors.ENDC}                                     
    """
}
