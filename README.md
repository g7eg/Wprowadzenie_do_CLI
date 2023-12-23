# Wprowadzenie do Terminala:
## Jak korzystać z niniejszych materiałów?
W celu realizacji zadań zgodnie z treścią polecenia wymagane jest utworzenie konta na platformie Github.com
Po utworzeniu konta zalecamy zweryfikować status studenta w celu uzyskania dostępu do szerszych zasobów platformy.
Więcej informacji na ten temat moźna znaleść pod adresem: [https://education.github.com/](https://education.github.com/)

## Terminal - CLI
Terminal (CLI- Comand Line Interface) to narzędzie programistyczne pozwalające na wykonanie wielu czynności na komputerze za pomocą odpowiednich komend. Zazwyczaj jako uzytkowicy kompterów PC przyzwyczajeni jesteśmy do pracy z nimi za pomocą graficznego interfejsu (GUI - Graphical User Interface). Często skomplikowane procedury klikologii w celu wykonania jakiś czynności mozna zastąpić jedna linią polecenia. Zdazają się równiez czynności których nie da się wyklikać. Z tego względu programiści zazwyczaj preferują wykorzystanie CLI jako jednego z narzędzi do programowania.

Część czynności, które będziemy wykonywać w tym kursie można również wyklikać, jednak zachęcam i jednocześnie zalecam powstrzymać się przed tym i skorzystać z komend opisanych w materiałach. Po pewnym czasie zauważysz że napisanie prostej komendy zajmuje zdecydowanie mnej czasu niż klikanie.

### Uwagi techniczne:
___
#### Windows (CMD/PowerShell) vs UNIX (Terminal) - w bardzo dużym uproszczeniu.
UNIX - większość systemów operacyjnych jest obecnie oparta o system UNIX, wyjątkiem jest tutaj Windows. Po więcej szczegółów odsyłam do internetu. 
Windows'owe CMD/ PowerShell jak i Unixowy Terminal to nic innego jak CLI (Command Line Interface). Ze względu na różnice pomiędzy systemami występują również pewne różnice w pracy z CLI. Główna różnica polega na różnych komendach wykorzystywanych do tych samych czynności. W szczególności jesli mowa o Windowsowy CMD ponieważ Widowsowy PowerShell wspiera polecenia Unixowe.

Generalnie będziemy korzystać w tym kursie z terminala Unix'owego i wszystkie poznane komendy będą również działać na innych wesjach i dystrybucjach systemu Unixowego (np Linux, macOS, Android) jak i w PowerShell Windowsa. Po więcej szczegółów odsyłam do interntu, przykładowe róznice w komendach można znaleźć np tutaj: [linux-vs-windows-commands](https://www.geeksforgeeks.org/linux-vs-windows-commands/).

Jeżeli chodzi o terminal należy pamiętać że jest to jedo z narzędzi które można dosyć mocno dostosować pod swoje potrzeby. Z tego względu część informacji jak i sposób ich wyświetlania może się róznić w zależności od ustawień.

# Terminal samouczek
Poniżej zostały opisane czynności, które należy wykonać jeden po drugim w celu przejścia całego samouczka. Pominięcie którejś z operacji może spowodować niezamierzony efekt lub któryś z kolejnych kroków nie będzie możliwy do wykonania o czym zostaniemy poinformowani stosowynm komentarzem w terminalu.


## Uruchomienie i konfiguracja środowiska:
Na samym początku nalezy uruchomić środowisko Codespace logując się przy tym na swoje konto GitHub.

Po jego uruchmieniu upewnij się ze w dolnej części okna przeglądarki znajduje się Terminal.

Jezeli go nie widzisz z menu wybierz ikonę <b> ≡ (ikona menu hamburgera)</b>  -> następnie terminal -> nowy terminal.

Powinieneś zauwazyc w oknie terminala coś podobnego do:
```cmd
@nazwaUżytkownika -> /workspaces/aktualna_ścieżka/ (gałąź repozytowrium) $
```
Przykładowy zrzut ekranu z terminala:

![Przykładowy zrzut erkanu z terminala](./img/image.png)

Oznacza to że wszystko zostało uruchomione poprawnie i możemy przystąpić do dalszej pracy!

## ls - Wyświetl zawartość katalogu
