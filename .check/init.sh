#!/bin/bash

function check_z1(){
testnum=1
pathz1=./.task_tests/zad1_test.py

if [ -f $pathz1 ]; then
    code --list-extensions > ./.task_tests/z1_extensions.txt
    python3 $pathz1
else
    echo 'Test do zadanie' $testnum 'nie istnieje. Skontaktuj się z prowadzącym.'
fi

}

function check_z2(){
testnum=2
pathz2=./.task_tests/zad2_test.py

if [ -f $pathz1 ]; then
    code --list-extensions > ./.task_tests/z1_extensions.txt
    python3 $pathz2
else
    echo 'Test do zadanie' $testnum 'nie istnieje. Skontaktuj się z prowadzącym.'
fi

}

function check_z3(){
if [ -f ./.task_tests/zad3_test.py ]; then
    echo 'File exists.'
    python3 ./.task_tests/zad3_test.py

else
    echo 'File does not exist.'
fi


}

