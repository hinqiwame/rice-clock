from datetime import datetime
import time
import os
from colorama import Fore

#current_time = datetime. now(). strftime("%H:%M:%S")

print(Fore.BLUE)
os.system("clear")

while True:
    os.system("clear")
    os.system("banner " + datetime. now(). strftime("%H:%M:%S"))   
    time.sleep(1)
