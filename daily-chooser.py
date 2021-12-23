from random import choice, choices
from os import system, name
from time import sleep
import assets
import json


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def loadJson(json_name):
    with open(json_name) as json_file:
        data = json.load(json_file)
    return data


def save(data, json_name):
    with open(json_name, 'w') as json_file:
        json.dump(data, json_file)


def draw(data, odds):
    chosen = choices(list(data['fintech-plataform'].keys()),
                     weights=odds, k=1)
    return chosen[0]


def animation(data):
    clear()
    for _ in range(10):
        print(assets.arts['daily'])
        random_person = choice(list(data['fintech-plataform'].keys()))
        for person in data['fintech-plataform']:
            if (person == random_person):
                print(f'➡️ {person}')
            else:
                print(f'{person}')
        sleep(0.5)
        clear()
    clear()


def validateDraw():
    v = input('Do you want to validate the result?\n')
    if v == 'y':
        return True
    return False


def setOddsAndStats(data, chosen):
    for person in data['fintech-plataform']:
        if person == chosen:
            data['fintech-plataform'][person]['odds'] = 0.5
            data['fintech-plataform'][person]['daily_chosen'] += 1
        if data['fintech-plataform'][person]['odds'] == 0:
            data['fintech-plataform'][person]['odds'] = 12.5
    return data


def showStats(data):
    print('Stats:\n')
    for person in data['fintech-plataform']:
        print(
            f"{person} - {data['fintech-plataform'][person]['daily_chosen']}/{data['daily_number']}")


def checkOdds(data):
    check = True
    for person in data['fintech-plataform']:
        if data['fintech-plataform'][person]['odds'] == 12.5:
            check = False

    if check:
        for person in data['fintech-plataform']:
            data['fintech-plataform'][person]['odds'] = 12.5

    return data


def setup(data):
    odds = []
    print('Do you want to take someone out of the draw?')
    take_out = input().split()
    print('Odds of the day:\n')
    for person in data['fintech-plataform']:
        if person in take_out:
            data['fintech-plataform'][person]['odds'] = 0
        print(f"{person} - {data['fintech-plataform'][person]['odds']}%")
        odds.append(data['fintech-plataform'][person]['odds'])
    return odds


def main():
    clear()
    data = loadJson('data.json')
    data = checkOdds(data)
    print(assets.arts['daily'])
    odds = setup(data)
    print('Starting the draw in 5 seconds...')
    sleep(5)
    chosen = draw(data, odds)
    animation(data)
    print(assets.arts['daily'])
    print(f'{assets.bcolors.OKGREEN}\t\t{chosen} you have been chosen!{assets.bcolors.ENDC}')
    if validateDraw():
        print(f'{assets.bcolors.OKGREEN}Daily validated{assets.bcolors.ENDC}\n')
        print(f"Daily number {data['daily_number']} (since 02/01/2022)\n")
        data = setOddsAndStats(data, chosen)
        showStats(data)
        data['daily_number'] += 1
        save(data, 'data.json')
    else:
        print('Restarting...')
        sleep(2)
        main()


if __name__ == '__main__':
    main()
