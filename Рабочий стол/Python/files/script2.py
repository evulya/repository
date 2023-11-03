#скрипт собирающий датасет {0}.png
#скрипт принимает заданный формат файла
# скрипт принимает папку из которой берет файлы
#копирует все файлы этого формата, переименовывая их
#сохранить порядок
import argparse
import os
import sys
import shutil
parser = argparse.ArgumentParser()
format_help='a format of target files (defaults to png)'
directory_help ='a source directory for files copying'
parser.add_argument('-f', '--format', default='png', help=format_help)
parser.add_argument('-d', '--directory', default='folder', help=directory_help)
args=parser.parse_args(sys.argv[1:])
if not os.path.isdir(args.directory):
    print(f'{args.directory} is not a directory')
    exit(1)
target_dir = 'dataset'
if not os.path.isdir(target_dir):
    os.mkdir(target_dir)
    full_path=os.path.join(os.getcwd(), target_dir)
    print(f'Directory {full_path} does not exist, creating..')
files = os.listdir(args.directory)
files = sorted(list(filter(lambda file: file.endswith(args.format), files)))
index =1
for filename in files:
    source=os.path.join(args.directory, filename)
    target =os.path.join('dataset', f'{index+1}.{args.format}')
    shutil.copy(source, target)
    print(f'File {sourse}')
