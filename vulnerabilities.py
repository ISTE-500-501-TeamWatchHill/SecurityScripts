"""
TODO:
    1. List users
    2. List open ports
    3. List running processes.
    4. List open files.
    5. (Optional) Run Maintence.py script.


"""


import os

# List Users


def list_users():
    list_results = os.system("getent passwd")
    print("System Users: \n" + list_results)

# List Open Ports


def open_ports():
    ports_list = os.system("sudo cat /etc/services | less")
    print("Open ports: \n" + ports_list)


def running_process():
    proc_list = os.system("sudo ps ax")
    print("Running processes: \n" + proc_list)


def list_lsof():
    lsof_results = os.system("sudo lsof")
    print("Open files: \n" + lsof_results)


def run_maintenance():
    main_result = os.system("sudo python3 maintenance.py")
    print("Results from maintenace script: \n" + main_result)


list_users()
open_ports()
running_process()
list_lsof()
run_maintenance()
