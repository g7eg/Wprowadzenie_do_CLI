
# Terminal samouczek
Poniżej zostały opisane czynności, które należy wykonać jeden po drugim w celu przejścia całego samouczka. Pominięcie którejś z operacji może spowodować niezamierzony efekt lub któryś z kolejnych kroków nie będzie możliwy do wykonania o czym zostaniemy poinformowani stosowynm komentarzem w terminalu.


## Uruchomienie i konfiguracja środowiska:
Na samym początku nalezy uruchomić środowisko Codespace logując się przy tym na swoje konto GitHub.

Po jego uruchmieniu upewnij się ze w dolnej części okna przeglądarki znajduje się Terminal.


Jezeli go nie widzisz z menu wybierz ikonę <b> ≡ (ikona menu hamburgera)</b>  -> następnie terminal -> nowy terminal.

Powinieneś zauwazyc w oknie terminalu coś podobnego do:
```cmd
@nazwaUżytkownika -> /workspaces/aktualna_ścieżka/ (gałąź repozytowrium) $
```
Przykładowy zrzut ekranu z terminalu:

![Przykładowy zrzut erkanu z terminalu](./img/terminal.png)

Oznacza to że wszystko zostało uruchomione poprawnie i możemy przystąpić do dalszej pracy!

# Podstawowe polecenia bash - wprowadzenie
Tutaj opisanych zostało kilka podstawowych poleceń, które są niezbędnę do poruszania się po katalogach i plikach na naszym komputerze oraz wykonywania podstawowych operacji na nich.

## ls - wyświetl zawartość katalogu
ls - list. Wpisanie tego polecenia w takiej formie:
```bash
ls
```
Wyświetli nam listę elementów znadujących się w katalogu w którym się obecnie znajdujemy.

![Przykład ls](img/ls.png)
Te same informacje możesz znaleźć w GUI - eksploratorze plików.

<img src="img/drzewko.png"  height="100" />

Polecenie ls możemy wywołac jeszcze z pewnymi parametrami.
Najważniejszymi i naczęściej wykorzystywanymi są:

```bash
ls -a
```
Pozwala wyświetlić wszystkie ukryte pliki w katalogu.

![ls-a](img/ls-a.png)

```bash
ls -l
```
Pozwala wyświetlić listę plików z bardziej szczegółowym opisem.

![ls-l](img/ls-l.png)

## cd - przejdź do katalogu
## pwd - wyświetl ścieżkę do obecnego katalogu
## mkdir - utwórz nowy katalog
## mv - przenieś plik
## rm - usuń plik lub katalog
## clear - wyczyść okno terminalu
# Dodatkowe komendy

## code - otwiera edycję pliku w VSCode - jeśtli jest zainstalowny
