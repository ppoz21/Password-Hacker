import socket
import sys

with socket.socket() as socket:
    ip = sys.argv[1]
    port = int(sys.argv[2])
    message = sys.argv[3]
    address = (ip, port)
    socket.connect(address)
    message = message.encode()
    socket.send(message)
    response = socket.recv(1024)
    response = response.decode()
    print(response)
