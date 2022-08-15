import init
from pathlib import Path
from random import choice, choices
from rich.console import Console
from rich.table import Table
from time import sleep
import utils

def chosen_one(data, odds):
    chosen = choices(list(data['members'].keys()),
                     weights=odds, k=1)
    return chosen[0]

def animation(data, take_out):
    utils.clear()
    for _ in range(10):
        print(utils.arts['daily'])
        random_person = choice(list(data['members'].keys()))
        is_chosen = ''
        table = Table(title="Odds of the day")
        columns = ["Person", "Odds"]

        for column in columns:
            table.add_column(column)
        for person in data['members']:
            if person == random_person:
                is_chosen = '➡️'
            else:
                is_chosen = ''

            if person in take_out:
                table.add_row(f'{is_chosen}  {person}', '0%', style='yellow')
            else:
                table.add_row(f'{is_chosen}  {person}', f'{"%0.2f" % (data["members"][person]["odds"])}%', style='bright_green')

        console = Console()
        console.print(table)
        sleep(0.2)
        utils.clear()
    utils.clear()


def validateDraw():
    v = input('Do you want to validate the result? (y|n)\n')
    if v == 'y':
        return True
    return False


def setOddsAndStats(data, chosen):
    retro = (data['members'][chosen]['odds']) / (len(data['members']) - 1)
    sum = 0
    for person in data['members']:
        if person == chosen:
            data['members'][person]['odds'] = 0
            data['members'][person]['daily_chosen'] += 1
        else:
            data['members'][person]['odds'] += retro
        sum+=data['members'][person]['odds']
    return data


def showStats(data):
    table = Table(title=f"Stats: Daily Number - {data['quantity_dailys']}")
    columns = ["Person", "Stats"]
    for column in columns:
        table.add_column(column)
    for person in data['members']:
        table.add_row(person, str(data['members'][person]['daily_chosen']) + f"/{data['quantity_dailys']}", style='bright_green')
            
    console = Console()
    console.print(table)
    
def setup(data):
    odds = []
    print('Do you want to take someone out of the draw?')
    take_out = input().split()
    table = Table(title=f"Daily {data['team_name']}\n Odds of the day")
    columns = ["Person", "Odds"]
    for column in columns:
        table.add_column(column)
    for person in data['members']:
        if person in take_out:
            table.add_row(person, '0%', style='yellow')
            odds.append(0)
        else:
            table.add_row(person, f'{"%0.2f" % (data["members"][person]["odds"])}%', style='bright_green')
            odds.append(data['members'][person]['odds'])

    console = Console()
    console.print(table)
    return odds, take_out

def draw():
    utils.clear()
    print(utils.arts['daily'])
    data = utils.loadJson('data.json')
    odds, take_out = setup(data)
    print('\nPress enter to start the draw')
    input()
    chosen = chosen_one(data, odds)
    animation(data, take_out)
    print(utils.arts['daily'])
    print(f"{utils.bcolors.OKGREEN}\t\t{chosen} you have been chosen!")
    print(
        f"\t\t{chosen} was chosen with a {data['members'][chosen]['odds']:.2f}% chance{utils.bcolors.ENDC}")
    if validateDraw():
        print(f'{utils.bcolors.OKGREEN}Daily validated{utils.bcolors.ENDC}\n')
        data = setOddsAndStats(data, chosen)
        showStats(data)
        data['quantity_dailys'] += 1
        utils.saveJson(data, 'data.json')
    else:
        print('Restarting...')
        sleep(1)
        draw()

def reset_odds():
    data = utils.loadJson('data.json')
    initial_odds = 100 / len(data['members'])
    for _ in data['members']:
        data['members'][_]['odds'] = initial_odds
    utils.saveJson(data,'data.json')

def settings():
    utils.clear()
    print(utils.arts['daily'])
    print('Select a option\n\n1 - Reset Odds\n2 - Menu')
    op = int(input())
    if op == 1:
        reset_odds()
        print('Odds reset successfully')
        sleep(2)
        settings()
    elif op == 2:
        menu()

def menu():
    utils.clear()
    print(utils.arts['daily'])
    print('Select a option\n\n1 - Start the draw\n2 - Settings')
    op = int(input())
    if op == 1:
        draw()
    elif op == 2:
        settings()

def main():
    path_to_file = 'data.json'
    path = Path(path_to_file)   
    if not path.is_file():
        init.main()
    menu()

if __name__ == '__main__':
    main()
