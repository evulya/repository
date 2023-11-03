#!/bin/bash
# punchline ='Все пары'
# echo 'Шутка от группы К0711-23'
# echo 'Сколько пар нужно, чтобы выучить питон'
# sleep 3
# echo 'Все'
# echo 'ОТвет: $punchline'
a=5
b=10
echo 'Сумма a и b'
echo $(($a+$b))
echo 'Результат функции date'
current_date=$(date)
echo $current_date
echo 'Результат date другим способом'
new_date=`date`
echo $new_date
echo 'Название скрипта $0'
echo 'Первый аргумент: $1, второй аргумент: $2'
echo $(($a*$b))
#выведем какой из аргументов больше
#lt - lower than
#gt - greater then
#le -меньше или равно
#ge  -больше или равно
# eq - равно
#ne - не равно
if [[ $a -lt $b ]]
then
    echo 'первый аргумент' $1 'меньше второго $2'  
elif [[ $a -gt $b ]]
then
    echo 'первый аргумент $1 больше второго $2'
else 
    echo 'аргументы равны: $1==$2'
fi
current=0
while [[ $current -lt $a ]]
do
    echo $current
    current=$(($current + 1))
done
echo 'ваше имя пользователя : ' $username
read -s -p 'Введите ваш пароль: ' -t 5 password
if $password
then 
    echo 'ваш пароль: '  $password
echo 'ваш пароль: ' $password