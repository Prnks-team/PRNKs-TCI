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

input("Waiting for input from user: ")
commands = input().lower()

helpcommands = ["end", "exit", "open" ]

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
    

    
