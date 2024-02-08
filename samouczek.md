[Wróć do wprowadzenie](./wprowadzenie.md)

# Samouczek

## Słowem wstępu

Poniżej zostały opisane czynności, które należy wykonać jeden po drugim w celu przejścia całego samouczka. Pominięcie którejś z operacji może spowodować niezamierzony efekt lub któryś z kolejnych kroków nie będzie możliwy do wykonania o czym zostaniemy poinformowani stosowynm komentarzem w terminalu.

Z powyższego akapitu należy wyciągnąć następujące wnioski:

-   Czynności które należy wykonać muszą być wykonane w ściśle określonej kolejności np. nie da się usunąć danego pliku jeżeli on nie istanieje,
-   Jeżeli spróbujemy wykonać polecenie, które jest niepoprawne efektem będzie stosowny kompunikat błędu. np. wywołanie polecenia sd które nieistnieje 'bash: sd: command not found',
-   Nieczytanie błędów nie zwalania nas z myślenia. Jeżeli uzyskujesz jakikolwiek błąd lub coś nie działa, zastanów się co może być przyczyną. Podpowiem że komunikat błędu zazwyczaj wskazuje na przyczynę tego, dlaczego coś nie działa.

---

## Zadanie 1

Zapamiętaj że wszystkie operacja które bedziemy wykonywać robimy w katalogu domyślnym: _/workspaces/Wprowadzenie_do_CLI_. Dlatego też przed uruchomieniem polecenia upewnij się że przed (po lewej stronie) znakiem zachęty _$_ znajduje się freagment ścieżki _/workspaces/Wprowadzenie_do_CLI_.

Pamięteż że w każdej chwilii możesz sprawdzić ścieżkę do akutalnego katalogu gdzie sie znajdujesz, wykonując polecenie _pwd_.

Jeżeli wpiszesz przez przypadek polecenie _cd_ bez podania jakiejkolwiek ścieżki i przeniesie Cię do katalogu głównego naszego systemu, nie przejmuj się tym. Możesz wrócić do poprzedniego katalogu wykonując polecenie '_cd -_' lub _cd /workspaces/Wprowadzenie_do_CLI_.

Dla pewności przed rozpoczęciem pracy wykonaj polecenie:

```bash
cd /workspaces/Wprowadzenie_do_CLI
```

### UWAGA! Jeżeli czytając treść polecenia uznasz że jest to na chwilę obecną zbyt trudne i i nie ogarniasz tego tematu, nie przejmuj się tylko zernij do podpowidzi które znajdują się poniżej treści zadania (ps. trzeba kliknąć w strzełeczkę aby się pojawiły 😉.

---

Krok 1. W katalogu domyślnym (_/workspaces/Wprowadzenie_do_CLI_) gdzie obecnie powinieneś się znajować, utwórz katalog nazywający się:

-   _przedmioty_

wewnątrz tego katalogu utwórz kolejny katalog nazwywający się:

-   _programowanie_

wewnątrz niego utwórz dwa katalogi:

-   _prowadzacy_ \*(unikaj PL nazków w nazwach katalogów oraz plików)
-   _studenci_

wewnątrz katalogu studenci utwórz katalog z własnym nr indeksu np:

-   _123123_ \*(podaj swój nr indeksu)

Krok 2. Wróć do katalogu _przedmioty_. Wyświetl strukturę katalogów.

Krok 3. Zweryfikuj czy wszystko się zgadza zogdnie z Krok 1 - czyli katalog _programowanie_ znajduje się w katalogu _przedmioty_, katalogi _prowadzacy_ oraz _studenci_ są wewnątrz _programowanie_, a katalog z Twoim nr indeksu jest wewnątrz katalogu _studenci_. Jeżeli nie dokonaj stosownych poprawek (usun katalogi i utwórz je jeszcze raz).

Krok 4. Przejdź do katalogu studenci a następnie do katalogu z Twoim nr indeku (no chyba że wiesz i zrobić to bez przechodzenia tam? To zrób bez przechodzenia w to mejsce) i utwórz w nim plik o nazwie _zad1.txt_. Upewnij się że plik nazywa się poprawnie!
Wpisz w nim swój ulubiony cytat z filmu, książki, piosenki, dowolnego źródła.

Zapisz zmianę i zakmnik plik.

Jeżeli wykonałeś wszystkie czynności po kolei i zogdnie z treścią polecenia, to rezultat może być tylko jeden.
Przejść do kolejnego podpunktu samouczka: 'Test zadania 1'.

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

12. Wróć do katalogu _/workspaces/Wprowadzenie_do_CLI_

```bash
cd /workspaces/Wprowadzenie_do_CLI
```

13. Wykorzystaj polecenie

```bash
tree
```

14. Wykorzystaj polecenie

```bash
cd /przedmiot/programowanie/studenci/123123
```

15. Wykorzystaj polecenie

```bash
code zad1.txt
```

</details>

## Test zadania 1

W celu weryfikacji czy wykonałeś zadanie 1 poprawnie należy wykonać polecenie.

Najpier wykonaj:

```bash
cd /workspaces/Wprowadznie_do_CLI/
```

,a następnie:

```bash
check_z1
```

Wynik weryfikacji uzyskasz w formie raportu wyświetlonego w terminalu.

---

### Do realizacji zadania nr 2 wymagane jest poprawne wykonanie zadania 1. Jeżeli test zadaia 1 zwrócił informację że coś jest NOK (not ok). Wróć do tego miejsca i dokonaj stosownych poprawek. Nie wiesz gdzie zacząć? Zacznij od początku i sprawdź poszczególne etapy po kolei.

---

## Zadanie 2

Krok 1. Wykonaj poprawnie zadanie 1.

Krok 2. Otwórz ponownie plik _raport_zad1.txt_ w katalogu z Twoim nr indesku. Zweryfikuj czy w raporcie znajdują się takie same informaje jak te które otrzymałeś z uruchomienia testów dla Zadania 1.
Jeżeli tak, super. Możesz zamknąć plik i przejść do kolejnogo kroku. Jeżli nie, możliwe że zapominałeś przetestować zadanie 1, w takim wypadku odsyłam do akapitu _Test zadania 1_.

Krok 3. W katalogu domyślnym (_/workspaces/Wprowadzenie_do_CLI_) gdzie znajduje się katalog _przedmioty_ utwórz nowy katalog i nazwij go _backups_\_ (tak z podkreśleniem na końcu).

Krok 4. W katalogu backup\_ uwtórz katalog _V1_\_.

Krok 5. Wykonaj kopię pliku _przedmioty_ wraz z jego zawartością do katalogu: _backup/\_V1_\_.
