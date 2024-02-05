import os.path

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

    if len(list_of_exist_files) == 4:
        print('_'*30)
        print('🟢 Wszystkie katalogi zostały utworzone poprawnie.')
        print('Możesz przystąpić do kolejnego zadania.')