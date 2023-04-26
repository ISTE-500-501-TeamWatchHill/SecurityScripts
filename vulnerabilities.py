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
    print("System Users: \n" + str(list_results))

# List Open Ports

#NOTE: THIS WILL OPEN IN VIM, USE :Q TO GET OUT.
def open_ports():
    ports_list = os.system("sudo cat /etc/services | less")
    print("Open ports: \n" + str(ports_list))


def running_process():
    proc_list = os.system("sudo ps ax")
    print("Running processes: \n" + str(proc_list))

#NOTE: THIS WILL OPEN IN VIM, USE :Q TO GET OUT.
def list_lsof():
    lsof_results = os.system("sudo lsof | less")
    print("Open files: \n" + str(lsof_results))


def run_maintenance():
    main_result = os.system("sudo python3 maintenance.py")
    print("Results from maintenace script: \n" + str(main_result))


list_users()
open_ports()
running_process()
list_lsof()
run_maintenance()
