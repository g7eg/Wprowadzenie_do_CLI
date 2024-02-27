import os.path
from os import listdir
import re
# GitHub.copilot-chat
# GitHub.copilot
pwd = './'
path1 = f'{pwd}/backups'
path2 = f'{pwd}/backups/v1'
path3 = f'{pwd}/backups/v1/przedmioty'
path4 = f'{pwd}/backups/v1/przedmioty/programowanie'
path5 = f'{pwd}/backups/v1/przedmioty/programowanie/prowadzacy'
path6 = f'{pwd}/backups/v1/przedmioty/programowanie/studenci'


list_of_exist_files = []

if __name__ == '__main__':
    print('Uruchamiam testy zadania 2.')
    print('_'*30)

    if os.path.exists(path1):
        print('🟢 Katalog backups istnieje.')
        list_of_exist_files.append('backups')
    else:
        print('🔴 Katalog backups nie istnieje.')
        print('Sprawdź czy katalog został utworzony w odpowiednim miejscu.')
        exit(1)

    if os.path.exists(path2):
        print('🟢 Katalog v1 istnieje i znajduje się w katalogu przedmioty.')
        list_of_exist_files.append('v1')
    else:
        print('🔴 Katalog v1 nie istnieje.')
        print('Sprawdź czy katalog został utworzony w odpowiednim miejscu.')
        exit(1)

    if os.path.exists(path3):
        print('🟢 Wykonano kopię katalogu przedmioty.')
        list_of_exist_files.append('studenci')
    else:
        print('🔴 Nie wykonano kopi katalogu przedmioty.')
        print('Sprawdź czy katalog został utworzony w odpowiednim miejscu.')
        exit(1)

    if os.path.exists(path4):
        print('🟢 Wykonano kopię katalogu programowanie.')
        list_of_exist_files.append('programowanie')
    else:
        print('🔴 Nie wykonano kopi katalogu programowanie.')
        print('Sprawdź czy katalog został utworzony w odpowiednim miejscu.')
        exit(1)
    
    if os.path.exists(path5):
        print('🟢 Wykonano kopię katalogu prowadzacy.')
        list_of_exist_files.append('prowadzacy')
    else:
        print('🔴 Nie wykonano kopi katalogu prowadzacy.')
        print('Sprawdź czy katalog został utworzony w odpowiednim miejscu.')
        exit(1)
    
    if os.path.exists(path6):
        print('🟢 Wykonano kopię katalogu studenci.')
        list_of_exist_files.append('studenci')
    else:
        print('🔴 Nie wykonano kopi katalogu studenci.')
        print('Sprawdź czy katalog został utworzony w odpowiednim miejscu.')
        exit(1)
    
    list_of_id_match = []
    for dir in os.listdir(path6):
        x = re.search(r"^\d{6}$", dir)
        if x:
            print('🟢 Katalog z Twoim nr indeksu został skopiowany poprawie.')
            list_of_exist_files.append(dir)
            list_of_id_match.append(dir)
    if list_of_id_match == []:
        print('🔴 Nie wykonano kopi katalogu z nr indeksu.')
        print('Sprawdź czy katalog został utworzony w odpowiednim miejscu.')
        exit(1)


    if len(list_of_exist_files) == 5:
        print('_'*30)
        print('🟢 Wszystkie katalogi zostały utworzone poprawnie.')
        # print('Możesz przystąpić do kolejnego zadania.')
    else:
        print('🟡 Niektóre z wymagaych kroków nie zostały spełnione poprawnie. Dokonaj stosonej modyfikacji i uruchom test raz jeszcze.')