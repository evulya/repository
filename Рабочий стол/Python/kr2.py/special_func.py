from subprocess import getstatusoutput
import os
import time
class OpenTerminal:
    """Python-styled opening of gnome terminal"""
    def __init__(self)->None:
        self.__calls= []
    def __call__(self)->None:
        if not os.system('gnome-terminal'):
            print('Gnome terminal successfully started')
            print(time.ctime())
        else:
            print('Gnome terminal failed to start')
    def get_all_calls(self)->list[str]:
        return self.__calls
    def get_calls_counter(self)->int:
        return len(self.__calls)

terminal_opener= OpenTerminal()
for _ in range(20):
    terminal_opener()
print('Terminal opener calls datetimes')
for timetamp in terminal_opener.get_all_calls():
    print(timetamp)
print(f'Terminal opener successful calls: {terminal_opener.get_calls_counter()}')
terminal_opener()