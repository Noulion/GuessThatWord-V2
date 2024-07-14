import os, time
from main import start_menu

def start_up():
    print("starting game....\n")
    time.sleep(1.5430)
    print("Enjoy The Game!")
    time.sleep(1.432)
    os.system('cls')
    return start_menu()
start_up()