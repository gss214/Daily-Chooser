from time import sleep
import utils

art = utils.Art()

def add_member():
    data = utils.load_json('data.json')
    print('Type the name of new member')
    name = input()
    data['members'][name] = {'odds': 0, 'daily_chosen': 0, 'on_vacation': False}
    utils.save_json(data, 'data.json')
    print(f'Member {name} added successfully')
    sleep(2)

def put_member_on_vacation():
    data = utils.load_json('data.json')
    print('Type the name of the member you want to put on vacation')
    name = input()
    data['members'][name]['on_vacation'] = True
    odd = data["members"][name]["odds"]
    members_lenght = len ([member for member in data["members"] if not data["members"][member]["on_vacation"]])
    retroactive_odd = odd / members_lenght
    for member in data["members"]:
        if member != name and not data["members"][member]["on_vacation"]:
            data["members"][member]["odds"] += retroactive_odd
    data['members'][name]['odds'] = 0
    utils.save_json(data, 'data.json')
    print('Member put on vacation successfully')
    sleep(2)
    return True

def mark_member_as_not_on_vacation():
    data = utils.load_json('data.json')
    print('Enter the name of the member who is no longer on vacation:')
    name = input()
    data['members'][name]['on_vacation'] = False
    utils.save_json(data, 'data.json')
    print('Member as not on vacation anymore')
    sleep(2)
    return True


def reset_odds():
    data = utils.load_json('data.json')
    actve_members = len([member for member in data['members'] if not data['members'][member]['on_vacation']])
    for person in data['members']:
        if not data['members'][person]['on_vacation']:
            data['members'][person]['odds'] = 100 / actve_members
    utils.save_json(data,'data.json')
    print('Odds reset successfully')
    sleep(2)
    return True

def settings():
    utils.clear_screen()
    print(art.daily)
    op = int(input("Select a option\n\n1 - Reset Odds\n2 - Put member on vacation\n3 - Mark a member as not on vacation\n4 - Add a new member\n5 - Menu\n"))
    if op == 1:
        reset_odds()
        settings()
    elif op == 2:
        put_member_on_vacation()
        settings()
    elif op == 3:
        mark_member_as_not_on_vacation()
        settings()
    elif op == 4:
        add_member()
        settings()
    elif op == 5:
        return True
