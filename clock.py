# Libraries
from datetime import datetime  # Using this lib, we will get the current time
from time import sleep  # Using this lib, we will create a delay in updating time
from os import system  # Using this lib, we will clear the terminal after delay to show the current time
from colorama import Fore  # Using this lib, we will change the color of the text in terminal
import sys  # Using this lib, we will use the arguments for using our script

# I'll add colors to variables, it's easier to use
red = Fore.RED
green = Fore.GREEN
blue = Fore.BLUE
pink = Fore.MAGENTA  # Not actually pink but still xD
yellow = Fore.YELLOW
cyan = Fore.CYAN
white = Fore.WHITE
# I think there are more colors, but I added the most of it


def clock(color):  # Defining a function
    print(color)  # Changing current terminal font color to chosen color
    system("clear")  # Clearing the terminal
    while True:  # Creating a loop, that repeats itself forever (until it's stopped by user)
        system("clear")  # Clearing the terminal to update the time
        system("banner " + datetime.now().strftime("%H:%M:%S"))  # Printing the time
        sleep(1)  # Making a delay in 1 second


try:
    # Working with arguments
    if sys.argv[1] == "-r":
        clock(color=red)
    elif sys.argv == "-g":
        clock(color=green)
    elif sys.argv[1] == "-b":
        clock(color=blue)
    elif sys.argv[1] == "-p":
        clock(color=pink)
    elif sys.argv[1] == "-y":
        clock(color=yellow)
    elif sys.argv[1] == "-c":
        clock(color=cyan)
    elif sys.argv[1] == "-w":
        clock(color=white)
    elif sys.argv[1] == "-h" or "--help":  # help argument
        print("A rice-like clock for terminals.\nFor usage, enter the command rice-clock + color, tah You want to use\nAvailable colors:\n - r - red\n - g - green\n - b - blue\n - p - pink\n - y - yellow\n - c - cyan\n - w - white")
except IndexError:
    print("A rice-like clock for terminals.\nFor usage, enter the command rice-clock + color, tah You want to use\nAvailable colors:\n - r - red\n - g - green\n - b - blue\n - p - pink\n - y - yellow\n - c - cyan\n - w - white")
except KeyboardInterrupt:
    system("clear")
    exit()
except:  # Except block for issues
    print("Error!")
    sleep(5)
