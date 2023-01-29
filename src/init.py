import utils
from rich.console import Console
from rich.table import Table

def input_team_name():
    team_name = input('First what is the name of the team?\n')
    return team_name

def input_member_count():
    n_members = int(input('How many members are there in the team?\n'))
    return n_members

def input_member_names(n_members):
    members = {}
    print('Enter the names of each team member:')
    for i in range(n_members):
        member = input(f'Enter name of member {i+1}: ')
        members[member] = {'odds': 0, 'daily_chosen': 0, 'on_vacation': False}
    return members

def display_team_summary(team_name, members):
    table = Table(title=team_name)
    table.add_column('Persons')
    for person in members:
        table.add_row(person, style='bright_green')
    console = Console()
    console.print(table)

def confirm_team_summary():
    confirmation = input('Is the information above correct? (y/n)\n')
    return confirmation.lower() == 'y'

def initialise_odds(members):
    initial_odds = 100 / len(members)
    for person in members:
        members[person]['odds'] = initial_odds
    return members

def main():
    utils.clear_screen()
    art = utils.Art()
    print(art.daily)
    print('Welcome to DailyChooser. The daily chooser is a script to select who from the team will command the daily on the day.')
    team_name = input_team_name()
    n_members = input_member_count()
    members = input_member_names(n_members)
    display_team_summary(team_name, members)
    confirmed = confirm_team_summary()
    if confirmed:
        members = initialise_odds(members)
        data = {'team_name': team_name, 'quantity_dailys': 1, 'members': members}
        utils.save_json(data, 'data.json')
        print('Daily Chooser successfully configured.')
    else:
        print('Restarting...')
        main()

if __name__ == '__main__':
    main()
