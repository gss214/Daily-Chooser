from pathlib import Path
from random import choice, choices
from rich.console import Console
from rich.table import Table
from time import sleep
import init
import os
import settngs
import utils

art = utils.Art()

def choose_one(data, odds):
    member_list = list(data["members"].keys())
    chosen = choices(member_list, weights=odds, k=1)[0]
    return chosen, odds[member_list.index(chosen)]

def display_table(title, rows, columns):
    table = Table(title=title)
    for column in columns:
        table.add_column(column)
    for row in rows:
        table.add_row(*row[:-1], style=row[-1])
    console = Console()
    console.print(table)

def show_animation(data, odds, excluded):
    utils.clear_screen()
    for _ in range(10):
        print(art.daily)
        random_person = choice(list(data["members"].keys()))
        title = "Odds of the day"
        columns = ["Person", "Odds"]
        rows = []
        for person, odd in zip(data["members"], odds):
            selected = "➡️" if person == random_person else ""
            color = "yellow" if person in excluded else "bright_green"
            rows.append([f"{selected} {person}", f"{odd:.2f}%", color])
        display_table(title, rows, columns)
        sleep(0.2)
        utils.clear_screen()

def validate_draw():
    response = input("Do you want to validate the result? (y/n)\n")
    while response != "y" and response != "n":
        response = input("Invalid option. Please enter 'y' or 'n'.\n")
    return response == "y"

def update_odds_and_stats_after_draw(data, chosen_member):
    retroactive_odd = data["members"][chosen_member]["odds"] / (len([member for member in data["members"] if (not data["members"][member]["on_vacation"] and chosen_member != member)]))
    for member in data["members"]:
        if member != chosen_member and not data["members"][member]["on_vacation"]:
            data["members"][member]["odds"] += retroactive_odd
    data["members"][chosen_member]["odds"] = 0
    data["members"][chosen_member]["daily_chosen"] += 1
    return data


def display_stats(data):
    title = f"Stats: Daily Number - {data['quantity_dailys']}"
    columns = ["Person", "Stats"]
    rows = []
    for person in data["members"]:
        rows.append([person, f"{data['members'][person]['daily_chosen']}/{data['quantity_dailys']}", "bright_green"])
    display_table(title, rows, columns)
    
def update_odds_before_draw(data):
    excluded_members = input("Do you want to take someone out of the draw? (separate the names by ', ')\n").split(', ')
    total_redistribution = sum(data['members'][member]['odds'] for member in excluded_members if (member in data['members']))
    active_members = [member for member in data['members'] if (not data['members'][member]['on_vacation'] and member not in excluded_members)]
    redistribution = total_redistribution / len(active_members)
    odds = []
    if not active_members:
        print("Não há membros suficientes para o sorteio.")
        return False, False
    for member in data['members']:
        if member in active_members:
            odds.append(data['members'][member]['odds'] + redistribution)
        else: 
            odds.append(0)
    rows = [[person, '0.00%' if person in excluded_members else (f'{data["members"][person]["odds"] + redistribution:.2f}%' if not data["members"][person]['on_vacation'] else 'is on vacation'), 'blue' if data["members"][person]['on_vacation'] else ('yellow' if (data["members"][person]["odds"] + redistribution == 0 or person in excluded_members) else 'bright_green')] for person in data['members']]
    display_table(f"Daily {data['team_name']}\n Odds of the day", rows, ["Person", "Odds"])
    return odds, excluded_members
    
def draw():
    utils.clear_screen()
    print(art.daily)
    data = utils.load_json('data.json')
    odds, excluded_members = update_odds_before_draw(data)
    if excluded_members and odds:
        input("\nPress enter to start the draw\n")
        chosen, odd = choose_one(data, odds)
        show_animation(data, odds, excluded_members)
        print(f"{utils.bcolors.OKGREEN}\t\t{chosen} have been chosen!")
        print(f"\t\t{chosen} was chosen with a {odd:.2f}% chance{utils.bcolors.ENDC}")
        if validate_draw():
            print(f'{utils.bcolors.OKGREEN}Daily validated{utils.bcolors.ENDC}\n')
            data = update_odds_and_stats_after_draw(data, chosen)
            display_stats(data)
            data['quantity_dailys'] += 1
            utils.save_json(data, 'data.json')
        else:
            print('Restarting...')
            sleep(1)
            draw()
    else:
        sleep(1)
        menu()
def menu():
    utils.clear_screen()
    print(art.daily)
    print('Select a option\n\n1 - Start the draw\n2 - Settings')
    op = None
    while op not in [1, 2]:
        try:
            op = int(input())
        except ValueError:
            op = None
        print("Invalid option. Please enter a valid number.")
    if op == 1:
        draw()
    elif op == 2:
        settngs.settings()
        menu()

def main():
    file_name = 'data/data.json'
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), file_name))
    path = Path(file_path)
    if not path.is_file():
        init.main()
    menu()

if __name__ == '__main__':
    main()
