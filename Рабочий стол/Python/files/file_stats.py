# принимая название папки вывести статистику форматов файлов в ней в процентах
# для папки 1.txt 2.py выведится txt: 50%, py 50%
"""This is some code"""
import argparse
import os
import sys

parser = argparse.ArgumentParser()
DIRECTORY_HELP = 'The directory for getting atats (default is folder)'
parser.add_argument('-d', '--directory',
                    defaults='folder',
                    help=DIRECTORY_HELP)
args = parser.parse_args(sys.argv[1:])
if not os.path.isdir(args.directory):
    print(f'The getting directory (${args.directory}) is not a directory')
    sys.exit(1)
ALL_COUNT = 0
filenames_postfixes = {}
for filename in os.listdir():
    full_name = os.path.join(args.directory, filename)
    if not os.path.isfile(full_name):
        continue
    filename_posfix = filename.split('.')[-1].lower() if '.' in filename else ''
    