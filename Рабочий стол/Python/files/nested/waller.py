import os
from pprint import pprint
for path, folder, files in os.walk('files'):#вывести папки и файлы из папки
    print(path, folder, files)
#folder
#--folder2
#---file
#--folder3
import os
sep ='-- '
for path, folder, files in os.walk('files'):
    level = path.count('/')
    #print(f'{level*sep}{path[path.rindex('/')+1:]}')# вывести файлы
    path = path[path.rindex('/')+1:] if '/' in path else path
    print(f'{level*sep}{path}')
    for file in files:
        print(f'{(level +1)* sep}{file}')
directory = 'files'
dir_struct = {
    directory: {}
}
keys = [directory]
for path, folders, files in os.walk(directory):
    print(path, folders,files)
    keys = path.split('/')
    cur_dir = keys[-1]
    for index, key in enumerate(keys):
        if index ==0:
            current = dir_struct[key]
        else:
            current = current[key]
    struct = {folder: {} for folder in folders}
    struct.update({file: None for file in files})
    current[cur_dir] = struct
    keys.append(cur_dir)
    print(dir_struct)
