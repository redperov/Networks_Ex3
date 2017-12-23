import socket
from handlers import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '127.0.0.1'
server_port = 80
server.bind((server_ip, server_port))
server.listen(5)

while True:
    client_socket, client_address = server.accept()
    print 'Connection from: ', client_address
    request = client_socket.recv(1024)
    # while not request == '':  # TODO handle case of HTTP 1.1, in which this while loop is needed
    print 'Received:\n', request
    response = handle_request(request)
    print 'Response:\n', response, '\n'
    client_socket.send(response)
    # request = client_socket.recv(1024)

    print 'Client disconnected\n'
    client_socket.close()

# client_socket.send("<html><body><h1>Hello</h1></body></html>")
# data = client_socket.recv(1024)


# print 'Client disconnected'
# client_socket.close()

"""
TODO
To send an image:
open(path, "rb") as file
    file.read()
also, if needed add Content-type: image

To handle hebrew add at top of the page:
# coding=utf-8
"""
