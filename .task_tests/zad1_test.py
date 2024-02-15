import os.path
from os import listdir
import re
# GitHub.copilot-chat
# GitHub.copilot
pwd = '/workspaces/Wprowadzenie_do_CLI'
path1 = f'{pwd}/przedmioty'
path2 = f'{pwd}/przedmioty/programowanie'
path3 = f'{pwd}/przedmioty/programowanie/studenci'
path4 = f'{pwd}/przedmioty/programowanie/prowadzacy'

list_of_exist_files = []

if __name__ == '__main__':
    print('Uruchamiam testy zadania 1.')
    print('_'*30)

    if os.path.exists(path1):
        print('🟢 Katalog przedmioty istnieje.')
        list_of_exist_files.append('przedmioty')
    else:
        print('🔴 Katalog przedmioty nie istnieje.')
        print('Sprawdź czy katalog został utworzony w odpowiednim miejscu.')
        exit(1)

    if os.path.exists(path2):
        print('🟢 Katalog programowanie istnieje i znajduje się w katalogu przedmioty.')
        list_of_exist_files.append('programowanie')
    else:
        print('🔴 Katalog programowanie nie istnieje.')
        print('Sprawdź czy katalog został utworzony w odpowiednim miejscu.')
        exit(1)

    if os.path.exists(path3):
        print('🟢 Katalog studenci istnieje i znajduje się w katalogu programowanie.')
        list_of_exist_files.append('studenci')
    else:
        print('🔴 Katalog studenci nie istnieje.')
        print('Sprawdź czy katalog został utworzony w odpowiednim miejscu.')
        exit(1)

    if os.path.exists(path4):
        print('🟢 Katalog prowadzacy istnieje i znajduje się w katalogu programowanie.')
        list_of_exist_files.append('prowadzacy')
    else:
        print('🔴 Katalog prowadzacy nie istnieje.')
        print('Sprawdź czy katalog został utworzony w odpowiednim miejscu.')
        exit(1)
    
    list_of_id_match = []
    for dir in os.listdir(path3):
        x = re.search(r"^\d{6}$", dir)
        if x:
            print('🟢 Katalog z Twoim nr indeksu istnieje i znajduje się w katalogu studenci.')
            list_of_exist_files.append(dir)
            list_of_id_match.append(dir)
    if list_of_id_match == []:
        print('🔴 Katalog z Twoim nr indeksu nie istnieje.')
        print('Sprawdź czy katalog został utworzony w odpowiednim miejscu.')
        exit(1)


    if len(list_of_exist_files) == 5:
        print('_'*30)
        print('🟢 Wszystkie katalogi zostały utworzone poprawnie.')
        print('Możesz przystąpić do kolejnego zadania.')
    else:
        print('🟡 Niektóre z wymagaych kroków nie zostały spełnione poprawnie. Dokonaj stosonej modyfikacji i uruchom test raz jeszcze.')