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


def check_ports():
    open_ports = [80, 443, 22, 3000, 3001]


def check_update():
    update = "sudo apt-get -y update"
    upgrade = "sudo apt-get -y upgrade"
    autoremove = "sudo apt-get -y autoremove"

    


check_sestatus()
check_ports()
check_update()


