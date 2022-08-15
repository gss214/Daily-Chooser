from rich.console import Console
from rich.table import Table
from time import sleep
import utils

def main():
    data = {}
    utils.clear()
    print(utils.arts['daily'])
    print('Welcome to DailyChooser. The daily chooser is a script to select who from the team will command the daily on the day.\nFirst what is the name of the team?')
    team_name = input()
    data['team_name'] = team_name
    data['quantity_dailys'] = 1
    data['members'] = {}
    print('Now put how many members your team has')
    n_members = int(input())
    print('Now put the name of each team member')
    for _ in range(n_members):
        member = input()
        data['members'][member] = {'odds':0, 'daily_chosen':0}
        print(f'Member {member} successfully added. Please put the name of the next one')
    table = Table(title=team_name)
    columns = ["Person"]
    for column in columns:
        table.add_column(column)
    for person in data['members']:
        table.add_row(person, style='bright_green')
    console = Console()
    console.print(table)
    v = input('Confirm that the information is correct (y|n)\n')
    if v == 'y':
        print('Building data json...')
        initial_odds = 100 / len(data['members'])
        for _ in data['members']:
            data['members'][_]['odds'] = initial_odds
        utils.saveJson(data,'data.json')
        print('Daily Chooser successfully configured')
        sleep(2)
    else:
        print('Restarting...')
        sleep(1)
        main()
    
if __name__ == '__main__':
    main()
