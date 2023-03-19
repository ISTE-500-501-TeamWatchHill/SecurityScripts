"""
TODO:
    1. List users
    2. List open ports
    3. List running processes.
    4. List open files.


"""


import os

# List Users
def list_users():
    os.system("getent passwd")

# List Open Ports

def open_ports():
    #os.system("cat /etc/services | less")
    pass

def running_process():
    pass

def list_lsof():
    pass