'''
TODO
This is where the script will be which should check on the following:
    SE Linux is enabled.

    Make sure the host is updating.

    Autoremove old packages

    Ports: 80, 443, 22, 3000, 3001 , 5000
    
'''
import os


def check_sestatus():
    sestatus = "sudo sestatus"
    sestatus_result = os.system(sestatus)

    print("SE Status Result: " + sestatus_result)


def check_ports():
    open_ports = [80, 443, 22, 3000, 3001, 5000]


def check_update():
    update = "sudo apt-get -y update"
    upgrade = "sudo apt-get -y upgrade"
    autoremove = "sudo apt-get -y autoremove"
    update_result = os.system(update)
    upgrade_result = os.system(upgrade)
    autoremove_result = os.system(autoremove)

    print("Upgrade Result: " + update_result + "\n" + "Upgrade Result: " +
          upgrade_result + "\n" + "Autoremove Result: " + autoremove_result)

# check_sestatus()
# check_ports()
# check_update()
