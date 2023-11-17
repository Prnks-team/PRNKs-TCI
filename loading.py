from alive_progress import alive_bar; import time
import sys

for total in 5000, 7000, 4000, 0:
    with alive_bar(total) as bar:
        for _ in range(5000):
            time.sleep(.001)
            bar()

print(""" __          __  _                                                _ 
 \ \        / / | |                                              | |
  \ \  /\  / /__| | ___ ___  _ __ ___   ___   _   _ ___  ___ _ __| |
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | | | / __|/ _ \ '__| |
    \  /\  /  __/ | (_| (_) | | | | | |  __/ | |_| \__ \  __/ |  |_|
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__,_|___/\___|_|  (_)
                                                                    

                                                                           """)

def start():
    input("Waiting for input from user: ")
commands = input().lower()

print("It's recomended that you use the setup command if this is your first time starting the program.")

helpcommands = ["end", "exit", "open", "create file", "file write", "faq", "info", "banana", "name", "setup"]

if "help" in commands:                                #prints the list of commands WIP
    print(helpcommands)

if "end" in commands:                               #ends the command system
    sys.exit(1)

if "create file" in commands:                               #creates file text.txt (shocking name)
    open('text.txt', 'w')

if "file write" in commands:                            #Opens the file that was created an writes a string inside of it
    file = open('text.txt', 'a')
    input("Write what you want to write: ")
    filewrite = input().lower()
    file.write(filewrite)

if "info" in commands:                                      #Displays current info
    print("""CURRENT INFO
          VERSION 0.1
          STABLE VERSION
           """)

if "faq" in commands:                                              #Displays owner ship
    print("CREATED BY PRNK DO NOT STEAL THIS CODE ")


if "banana" in commands:
    print("""  .----------------.  .----------------.  .-----------------. .----------------.  .-----------------. .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |   ______     | || |      __      | || | ____  _____  | || |      __      | || | ____  _____  | || |      __      | |
| |  |_   _ \    | || |     /  \     | || ||_   \|_   _| | || |     /  \     | || ||_   \|_   _| | || |     /  \     | |
| |    | |_) |   | || |    / /\ \    | || |  |   \ | |   | || |    / /\ \    | || |  |   \ | |   | || |    / /\ \    | |
| |    |  __'.   | || |   / ____ \   | || |  | |\ \| |   | || |   / ____ \   | || |  | |\ \| |   | || |   / ____ \   | |
| |   _| |__) |  | || | _/ /    \ \_ | || | _| |_\   |_  | || | _/ /    \ \_ | || | _| |_\   |_  | || | _/ /    \ \_ | |
| |  |_______/   | || ||____|  |____|| || ||_____|\____| | || ||____|  |____|| || ||_____|\____| | || ||____|  |____|| |
| |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' """)
    

if "name" in commands:
    name = input("Please enter your name: ")
    print(name)


if "setup" in commands:
 name = input("Please enter your user name:")
 print("You're all setup now!" )
 time.sleep(5)
 start()