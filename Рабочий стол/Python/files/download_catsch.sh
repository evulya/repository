#!/bin/bash
cat_server='https://cataas.com/cat'
for ((i=1;i<10,i++))
do 
    curl -o 'NIKONO30$i.png' $cat_server
done