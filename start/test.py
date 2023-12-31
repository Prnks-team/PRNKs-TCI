#RUN github rebase if its not letting you sync

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

def setuptext():
    print("It's recomended that you use the setup command if this is your first time starting the program.")

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

from alive_progress import alive_bar; import time                       # * [FIXED] loading bar runs 4 times before program starts fix this now!!!!!!
import sys

with alive_bar(1200000, ctrl_c='b', unit='b', scale='SI', precision=2) as bar: 
               for I in range(1200000): 
                bar()

print(""" __          __  _                                                _ 
 \ \        / / | |                                              | |
  \ \  /\  / /__| | ___ ___  _ __ ___   ___   _   _ ___  ___ _ __| |
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | | | / __|/ _ \ '__| |
    \  /\  /  __/ | (_| (_) | | | | | |  __/ | |_| \__ \  __/ |  |_|
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__,_|___/\___|_|  (_)
                                                                    """)
 
print("Type help to see the list of commands.")
def start():
    setuptext()


    input("Waiting for input from user (Press enter once): ")
start()




helpcommands = ["end", "exit", "open", "create file", "file write", "faq","banana","setup", "secret (REQUIRES PIN)", "machine info", "file open", "license"]


if "help" in commands:                                # *prints the list of commands WIP
    print(helpcommands)
    start() 

if "end" in commands:                               # *ends the command system
    sys.exit(1)
    

if "create file" in commands:                       # * creates file text.txt (shocking name)
    open('text.txt', 'w')                           
    start()

if "file write" in commands:                            # *Opens the file that was created an writes a string inside of it
    file = ('text.txt', 'a')
    input("Write what you want to write: ")
    filewrite = input().lower()
    file.write(filewrite)
    start()


if "faq" in commands:                                              # * Displays owner ship / Version / source code / etc
    print("""CREATED BY PRNK DO NOT STEAL THIS CODE 
            Version: 0.0.3 (DEV BUILD)
          Current build: Dev build 0.0.3
          Build date: 11/30/2023
          build description: This build is a dev build and is not stable.
          IF YOU ARE NOT A DEV YOU SHOULD NOT BE USING THIS BUILD.


==

if "faq" in commands:                                              # * Displays owner ship / Version / source code / etc
    print("""CREATED BY PRNK DO NOT STEAL THIS CODE
            Version: a0.0.3
            Current build: Canary a0.0.3 



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
    execute_python_file('/workspaces/PRNKs-terminal/start/story.py')




if "machine info" in commands:
    print(platform.uname())
    start()


if "license" in commands:
    file = open('/workspaces/PRNKs-TCI/start/License.txt', 'r')
    print(file.read())
    start()
     

