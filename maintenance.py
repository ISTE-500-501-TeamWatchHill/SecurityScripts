import os
import socket


def check_sestatus():
    sestatus = "sudo sestatus"
    sestatus_result = os.system(sestatus)

    print("SE Status Result: " + sestatus_result)


def check_ports():
    open_ports = [80, 443, 22, 3000, 3001, 5000]

    for port in open_ports:
        a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        location = ("127.0.0.1", port)

        result_of_check = a_socket.connect_ex(location)

        if result_of_check == 0:

            print(port + " is open")

        else:

            print(port + " is not open")

        a_socket.close()


def check_update():
    update = "sudo apt-get -y update"
    upgrade = "sudo apt-get -y upgrade"
    autoremove = "sudo apt-get -y autoremove"
    update_result = os.system(update)
    upgrade_result = os.system(upgrade)
    autoremove_result = os.system(autoremove)

    print("Upgrade Result: " + update_result + "\n" + "Upgrade Result: " +
          upgrade_result + "\n" + "Autoremove Result: " + autoremove_result)


check_sestatus()
check_ports()
check_update()
