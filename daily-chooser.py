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
    retro = (data['fintech-plataform'][chosen]['odds'] - 0.5) / 7
    for person in data['fintech-plataform']:
        if person == chosen:
            data['fintech-plataform'][person]['odds'] = 0.5
            data['fintech-plataform'][person]['daily_chosen'] += 1
        else:
            data['fintech-plataform'][person]['odds'] += retro

    return data


def showStats(data):
    print(f"\t\t{'-' * 44}")
    print(f"\t\t|{' ' * 19}Stats{' ' * 18}|")
    print(f"\t\t|{'-'* 42}|")
    print(f"\t\t|{' ' * 4}Daily number {data['daily_number']} (since 02/01/2022){' ' * 4}|")
    print(f"\t\t|{'-'* 42}|")
    for person in data['fintech-plataform']:
        print(
            f"\t\t|{' ' * 15}{person} - {data['fintech-plataform'][person]['daily_chosen']}/{data['daily_number']}{' ' * (20 - len(person))}|")
    print(f"\t\t|{'-'* 42}|")
    return data


def setup(data):
    odds = []
    print('Do you want to take someone out of the draw?')
    take_out = input().split()
    print(f"\t\t{'-' * 44}")
    print(f"\t\t|{' '* 14}Odds of the day:{' ' * 12}|")
    print(f"\t\t|{'-'* 42}|")
    print(f"\t\t|{' ' * 8}Person{' ' * 7}|{' ' * 8}Odds{' ' *8}|")
    print(f"\t\t|{'-' * 21}|{'-' * 20}|")
    for person in data['fintech-plataform']:
        if person in take_out:
            print(f"\t\t|{assets.bcolors.WARNING}{person}{assets.bcolors.ENDC} {' ' * (19 - len(person))} | {assets.bcolors.WARNING}0.00%{' ' * 14}{assets.bcolors.ENDC}|")
            odds.append(0)
        else:
            spaces_odds = 13 if data['fintech-plataform'][person]['odds'] > 10 else 14
            print(f"\t\t|{person} {' ' * (19 - len(person))} | {data['fintech-plataform'][person]['odds']:.2f}%{' ' * spaces_odds}|")
            odds.append(data['fintech-plataform'][person]['odds'])
    print(f"\t\t|{'-' * 42}|")
    return odds


def main():
    clear()
    data = loadJson('data.json')
    print(assets.arts['daily'])
    odds = setup(data)
    print('\nPress enter to start the draw')
    input()
    chosen = draw(data, odds)
    animation(data)
    print(assets.arts['daily'])
    print(f"{assets.bcolors.OKGREEN}\t\t{chosen} you have been chosen!")
    print(
        f"\t\t{chosen} was chosen with a {data['fintech-plataform'][chosen]['odds']:.2f}% chance{assets.bcolors.ENDC}")
    if validateDraw():
        print(f'{assets.bcolors.OKGREEN}Daily validated{assets.bcolors.ENDC}\n')
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
