# Copyright (C) <2023>  <Anthony J Counts>
 # This software is a terminal that you can execute command's in.

   # This program is free software: you can redistribute it and/or modify
    #it under the terms of the GNU Affero General Public License as published
    #by the Free Software Foundation, either version 3 of the License, or
   # (at your option) any later version.

   # This program is distributed in the hope that it will be useful,
   # but WITHOUT ANY WARRANTY; without even the implied warranty of
   # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   # GNU Affero General Public License for more details.

   # You should have received a copy of the GNU Affero General Public License
   # along with this program.  If not, see <https://www.gnu.org/licenses/>.

    # SOURCE CODE:
    # https://github.com/prnk1243/Prnks-terminal/tree/main

import os
import subprocess 
import platform

def execute_python_file(file_path):
   try:
      completed_process = subprocess.run(['python', file_path], capture_output=True, text=True)
      if completed_process.returncode == 0:
         print("Execution successful.")
         print("Output:")
         print(completed_process.stdout)
      else:
         print(f"Error: Failed to execute '{file_path}'.")
         print("Error output:")
         print(completed_process.stderr)
   except FileNotFoundError:
      print(f"Error: The file '{file_path}' does not exist.")

file_path = '/workspaces/H-/aaaa.py'

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
start()
commands = input().lower()

print("It's recomended that you use the setup command if this is your first time starting the program.")

helpcommands = ["end", "exit", "open", "create file", "file write", "faq", "info", "banana","setup", "secret (REQUIRES PIN)", "machine info"]

if "help" in commands:                                #prints the list of commands WIP
    print(helpcommands)
    start()

if "end" in commands:                               #ends the command system
    sys.exit(1)
    

if "create file" in commands:                         #creates file text.txt (shocking name)
    open('text.txt', 'w')
    start()

if "file write" in commands:                            #Opens the file that was created an writes a string inside of it
    file = ('text.txt', 'a')
    input("Write what you want to write: ")
    filewrite = input().lower()
    file.write(filewrite)
    start()

if "info" in commands:                                      #Displays current info
    print("""CURRENT INFO
          VERSION 0.1
          STABLE VERSION
           """)
    print(platform.python_version())
    start()

if "faq" in commands:                                              #Displays owner ship
    print("""CREATED BY PRNK DO NOT STEAL THIS CODE
          The source code can be accessed here: https://github.com/prnk1243/PRNKs-terminal/tags
          
          
        
          
          Use the copyright command to see the copyright.""")
    start()


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
    start()



if "setup" in commands:
 input("Please enter your user name:")
 name = input().lower()
 print("You're all setup now!" )
 time.sleep(5)
 start()


if "copyright" in commands:
    print(""" Copyright (C) <2023>  <Anthony J Counts>
  This software is a terminal that you can execute command's in.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.""")
    start()

if "secret" in commands:
    execute_python_file(file_path)




if "machine info" in commands:
    print(platform.uname())

