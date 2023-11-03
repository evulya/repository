#кот-пример использования модулей
#мы принимаем имена котов
#скачиваем их через python
 #записываем в json
#предлагаем выбрать котов для объединения в 
#ооо кот на python   
#изображения котовтв одно изображение
import requests #для веб запросов
import PIL #для изображений
from progress.bar import Bar  #для отображения прогресса скачивания
import os 
cat_names= []
CATAAS_URL = 'http://cataas.com/cat'
OK =200
while True:
    name =input('Введитеимя очередного кота:')
    if name.lower() in ['q', 'quit', 'exit', 'й']:
        break
    cat_names.append(name)
if not cat_names:
    print('Вы не ввели имя ни одного кота')
    exit(0)
directory = 'cats'
if not os.path.isdir(directory):
    os.mkdir(directory)
    full_name = os.path.join(os.getcwd(), directory)
    print(f'Директория {full_name} не существует, создаем')
 for cat in cat_names:
    response = requests.get(CATAAS_URL)
    if not response.status_code =OK:
        print(f'Для котов  {cat} не скачалась аватарка')
    else:
        write cat(cat, response)
print(cats_files)
menu= 'Выберите кота, которого хотите посмотреть'
for index, cat in enumerate(cat_names):
    menu+=f'\n{index+1}.cat'
num_cats = len(cat_names)
while True:
    num = input(menu)
    if num.lower() in EXIT_SEQS:
        break
    try:
        index=int(num)
    except ValueError:
        print('Вы должны вводить число от 1 до {num_cats}')
    else:
        if index<=0 or index>num_cats:
            print(f'Вы должны вводить число от 1 до {num_cats}')
        show_cat(cats_files[cat_names[index-1]])
start = 'Выберите котов-учередителей ООО Кот на Python(через пробел)'
while True:
    indexes = input(f'{start}{cats_menu}\n')
    if indexes.lower() in EXIT_SEQS:
        break
    try:
        indexes = list(map(int, indexes.split()))
