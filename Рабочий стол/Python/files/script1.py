#скрипт, который выводит некоторые глобальные переменные окружения 
# меняет все папки, переименовывая их
# префикс переименования берет .env файла
 # название папки принимает как именованный аргумент скрипта
# использует все проверки (папок, файлов и т.д)
import os
import dotenv
import argparse
import sys
user = os.environ.get('USER', default='sirius')
homedir=os.environ.get('HOME', default=f'/home/{user}')
prefix =os.environ.get('prefix', default='')
print(user, homedir)
if not prefix:
    print('Prefix was not provided in .env file')
    exit(1)
parser = argparse.ArgumentParser()
dir_help = 'A directory for file renaming process'
parser.add_argument('--directory', '-d', default = 'folder', help = dir_help)
args= parser.parse_args(sys.argv[1:])
print(args.directory)
if not os.path.isdir(args.directory):# проверяем папка это или нет
    print(f'{args.directory} is not a directory')
    exit(2)
for filename in os.listdir(args.directory): 
    full_name = os.path.join(args.directory, filename)
    if os.path.isfile(full_name):
        new_name =f'{args.directory}{prefix}{filename}'
        os.rename(full_name, new_name)
        print(f'File {full_name} was renamed to {new_name}')