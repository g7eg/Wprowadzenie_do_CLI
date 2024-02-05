[Wróć do wprowadzenie](./wprowadzenie.md)
# Samouczek
## Słowem wstępu
Poniżej zostały opisane czynności, które należy wykonać jeden po drugim w celu przejścia całego samouczka. Pominięcie którejś z operacji może spowodować niezamierzony efekt lub któryś z kolejnych kroków nie będzie możliwy do wykonania o czym zostaniemy poinformowani stosowynm komentarzem w terminalu.

Z powyższego akapitu należy wyciągnąć następujące wnioski:
- Czynności które należy wykonać muszą być wykonane w ściśle określonej kolejności np. nie da się usunąć danego pliku jeżeli on nie istanieje,
- Jeżeli spróbujemy wykonać polecenie, które jest niepoprawne efektem będzie stosowny kompunikat błędu. np. wywołanie polecenia sd które nieistnieje 'bash: sd: command not found',
- Nieczytanie błędów nie zwalania nas z myślenia. Jeżeli uzyskujesz jakikolwiek błąd lub coś nie działa, zastanów się co może być przyczyną. Podpowiem że komunikat błędu zazwyczaj wskazuje na przyczynę tego, dlaczego coś nie działa. 

___

## Zadanie 1
Zapamiętaj że wszystkie operacja które bedziemy wykonywać robimy w katalogu domyślnym: */workspaces/Wprowadzenie_do_CLI*. Dlatego też przed uruchomieniem polecenia upewnij się że przed (po lewej stronie)  znakiem zachęty *$* znajduje się freagment ścieżki */workspaces/Wprowadzenie_do_CLI*.

Pamięteż że w każdej chwilii możesz sprawdzić ścieżkę do akutalnego katalogu, wykonując polecenie *pwd*.

Jeżeli wpiszesz przez przypadek polecenie *cd* bez podania jakiejkolwiek ścieżki i przeniesie Cię do katalogu głównego naszego systemu, nie przejmuj się tym. Możesz wrócić do poprzedniego katalogu wykonując polecenie '*cd -*' lub *cd /workspaces/Wprowadzenie_do_CLI*.

Dla pewności przed rozpoczęciem pracy wykonaj polecenie:
```bash
cd /workspaces/Wprowadzenie_do_CLI
```
___
Krok 1. W katalogu domyślnym (*/workspaces/Wprowadzenie_do_CLI*) gdzie obecnie powinieneś się znajować, utwórz katalog nazywający się:
- *przedmioty*

wewnątrz tego katalogu utwórz kolejny katalog nazwywający się: 
- *programowanie*

wewnątrz niego utwórz dwa katalogi:
- *prowadzacy* *(unikaj PL nazków w nazwach katalogów oraz plików)
- *studenci*

wewnątrz katalogu studenci utwórz katalog z własnym nr indeksu np:
- *123123* *(podaj swój nr indeksu)

Krok 2. Wróć do katalogu *przedmioty*. Wyświetl strukturę katalogów.

Krok 3. Zweryfikuj czy wszystko się zgadza zogdnie z Krok 1 - czyli katalog *programowanie* znajduje się w katalogu *przedmioty*, katalogi *prowadzacy* oraz *studenci* są wewnątrz *programowanie*, a katalog z Twoim nr indeksu jest wewnątrz katalogu *studenci*. Jeżeli nie dokonaj stosownych poprawek (usun katalogi i utwórz je jeszcze raz).


Jeżeli na tym etapie nie wiesz jak wykonać poszczególne kroki poniżej znajdują się podpowiedzi. W dalszych etapach samouczka podpowiedzi będą mniej szczegółowe. 

Klikając na strzełeczkę rozwiniesz listę z podpowiedziami.


<details>
  <summary>Podpowiedź</summary>

  0. Wykorzystaj polecenie w celu upewnienia się że jesteś we właściwym katalgu
  ```bash
  pwd
  ```
  jeżeli zwóciona ścieżka to /workspaces/Wprowadzenie_do_CLI znaczy ze jesteś w odpowiednim miejscu.
  Jeżeli nie to wróć do tego katalogu wpisując:
  ```bash
  cd /workspaces/Wprowadzenie_do_CLI
  ```
  1. Wykorzystaj polecenie :
  ```bash
  mkdir przedmiot
  ```
  2. Przejdź do katalogu przedmiot za pomocą:
  ```bash
  cd przedmiot
  ```
  3. Wykorzystaj polecenie:
  ```bash
  ls
  ``` 
  Aby upewnić się że w katalogu nie ma jeszcze każdnych plików.

  4. Wykorzystaj polecenie:
  ```bash
  mkdir programowanie
  ```
  5. Wykorzystaj polecenie:
  ```bash
  cd programowanie
  ```
  6. Wykorzystaj polecenie:
  ```bash
  ls
  ``` 
  Aby upewnić się że w katalogu nie ma jeszcze każdnych plików.

  7. Wykorzystaj polecenie
  ```bash
  mkdir prowadzacy
  ``` 
  8. Wykorzystaj polecenie
  ```bash
  mkdir studenci
  ``` 
  9. Wykorzystaj polecenie:
  ```bash
  ls
  ``` 
  Aby upewnić się że w katalogu zostały utworzone dwa nowe katalogi.

  10. Przejdź do katalogu studenci za pomocą
  ```bash
  cd studenci
  ```
  11. Wykorzystaj polecenie gdzie zamiast 123123 podaj wlasny nr indeksu
  ```bash
  mkdir 123123
  ```
  12. Wróć do katalogu */workspaces/Wprowadzenie_do_CLI*
  ```bash
  cd /workspaces/Wprowadzenie_do_CLI
  ```
  13. Wykorzystaj polecenie
  ```bash
  tree
  ```   
</details>

## Test zadania 1
W celu weryfikacji czy wykonałeś zadanie 1 poprawnie należy uruchomić skrypt testujący.
Należy wykonać:
```bash
cd /workspaces/Wprowadznie_do_CLI/
```
,a następnie:
```bash
bash check1.sh
```



___
Zadanie 2
Do realizacji zadania nr 2 wymagane jest poprawne wykonanie zadania 1.
Jeżeli test zwrócił  

Krok 1. Utwórz plik tekstowy w katalogu studenci/twój_nr_indeksu. Plik powinien mieć nazwę zad1.txt.

Krok 2. W pliku wpisz następujący nagłówek:
'# Raport zadania'
