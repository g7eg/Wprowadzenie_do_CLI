#!/bin/bash

function check_z1(){
testnum=1
pathz1=/workspaces/Wprowadzenie_do_CLI/.task_tests/zad1_test.py

if [ -f $pathz1 ]; then
    python3 $pathz1
else
    echo 'Test do zadanie' $testnum 'nie istnieje. Skontaktuj się z prowadzącym.'
fi

}

function check_z2(){

python3 /workspaces/Wprowadzenie_do_CLI/.task_tests/zad2_test.py

}

function check_z3(){
if [ -f /workspaces/Wprowadzenie_do_CLI/.task_tests/zad3_test.py ]; then
    echo 'File exists.'
    python3 /workspaces/Wprowadzenie_do_CLI/.task_tests/zad3_test.py

else
    echo 'File does not exist.'
fi


}

