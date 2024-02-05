# Wprowadzenie do CLI (Comand Line Interface):
## Jak korzystać z niniejszych materiałów?
W celu realizacji zadań zgodnie z treścią polecenia wymagane jest utworzenie konta na platformie Github.com
Po utworzeniu konta zalecamy zweryfikować status studenta w celu uzyskania dostępu do szerszych zasobów platformy.
Więcej informacji na ten temat moźna znaleść pod adresem: [https://education.github.com/](https://education.github.com/)

!UWAGA
___
Niektóre z zawartych tu informacji stanowią bardzo duże uproszczenie opisanych zagadnień. Zabieg ten jest celowy i ma za zadanie zbliżyć Cię do poruszanych tu informacji. Wraz z dalszą nauką bardziej szczegółowe informacje będą uzupełniać wiedzą zdobytą na początkowym etapie.

## CLI - Comand Line Interface
CLI - Comand Line Interface to wbudowane w system operacyjny narzędzie programistyczne pozwalające na wykonanie wielu czynności na komputerze za pomocą odpowiednich komend. Zazwyczaj jako uzytkowicy kompterów PC przyzwyczajeni jesteśmy do pracy z komputerem za pomocą graficznego interfejsu (GUI - Graphical User Interface). Często skomplikowane procedury klikologii w celu wykonania jakiś czynności można zastąpić jedna linią polecenia. Zdażają się również czynności których nie da się wyklikać. Z tego względu programiści zazwyczaj preferują wykorzystanie CLI jako jednego z narzędzi do programowania.

Część czynności, które będziemy wykonywać w tym kursie można również wyklikać, jednak zachęcam i jednocześnie zalecam powstrzymać się przed tym i skorzystać z komend opisanych w materiałach. Po pewnym czasie zauważysz że napisanie prostej komendy zajmuje zdecydowanie mnej czasu niż klikanie.

### Uwagi techniczne:
___
#### Windows (CMD/PowerShell) vs UNIX (Terminal) - w bardzo dużym uproszczeniu.
UNIX - większość systemów operacyjnych jest obecnie oparta o system UNIX, wyjątkiem jest tutaj Windows (MS-DOS). Po więcej szczegółów odsyłam do internetu. 
Windows'owe CMD/ PowerShell jak i Unixowy Terminal to nic innego jak programy pozwalające na pracę z powłoką systemu UNIX (SHELL). Ze względu na różnice pomiędzy systemami występują również pewne różnice w pracy SHELL. Główna różnica polega na różnych komendach wykorzystywanych do tych samych czynności. W szczególności jesli mowa o Windowsowy CMD ponieważ Widowsowy PowerShell wspiera polecenia Unixowe.

Generalnie będziemy korzystać w tym kursie z systemu Unix'owego i wszystkie poznane komendy będą również działać na innych wesjach i dystrybucjach systemu Unixowego (np Linux, macOS, Android) jak i w PowerShell Windowsa. Po więcej szczegółów odsyłam do interntu, przykładowe róznice w komendach można znaleźć np tutaj: [linux-vs-windows-commands](https://www.geeksforgeeks.org/linux-vs-windows-commands/).

#### SHELL - powłoka
Shell (powłoka) - to nic innego jak interface wiersza poleceń łączący hardware i temrinal (w uproszczeniu to element który wykonuje coś po wpisaniu przez użtkonika komendy np uruchomienie programu). Możemy wyróżnic kilka różniących się miedzy sobą powłok np: bash, ksh, csh, tcsh, zsh. Nie wgłębiając się w temat, na chwilę obecną powinieneś wiedziec to że jest coś takiego jak powłoka i jest ich kilka typów. My natomiast skupimy się na powłocje bash.

#### Terminal
Terminal to po prostu program, który obsługuje daną powłokę. Pozwala na uruchomienie powłoki i komunikacji użytkonika z nią. To w nim wpisujemy polecenia, które są wykonywane przez Shell.

Jeżeli chodzi o terminal należy pamiętać że jest to jedno z narzędzi, które można dosyć mocno dostosować pod swoje potrzeby. Z tego względu część informacji jak i sposób ich wyświetlania może się róznić w zależności od ustawień.

![img not found](img/image.png)
Źródło: [LINK](https://medium.com/@Abhishek_kumar_/console-vs-terminal-vs-shell-difference-betweeen-them-b9acd3270dae)
___
## Startujemy!

Zapraszam do ->
[Wprowadzenie do poleceń - bash](./wprowadzenie.md)