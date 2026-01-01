import time
import os

text = ">>> Moving Text >>> "
width = os.get_terminal_size().columns -  len(text)
for pos in range(width):
    print(" " * pos + text) 
    time.sleep(0.02)
    os.system('cls' if os.name == 'nt' else 'clear')
print("going back!!!")
for pos in range(width, 0, -1):
    print(" " * pos + text) 
    time.sleep(0.02)
    os.system('cls' if os.name == 'nt' else 'clear')