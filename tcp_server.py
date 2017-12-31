import socket
from handlers import *
import thread


def client_handler(client, address):
    """
    Handles a client with a separate socket.
    :param client: client socket
    :param address: client address
    :return: None
    """
    stop = False

    while not stop:
        try:
            client.settimeout(5)

            # Receive a request.
            request = client.recv(1024)
            # print 'Received:\n', request

            # Handle the request.
            response = handle_request(request)
            # print 'Response to ', address, ':\n', response, '\n'

            # Send the response.
            client.send(response)

        except socket.timeout:
            stop = True
        except IndexError:
            return

    # print 'Client disconnected\n'
    try:
        client.close()
    except socket.error:
        pass


if __name__ == '__main__':

    # Create server welcome socket.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = '127.0.0.1'
    server_port = 80
    server.bind((server_ip, server_port))
    server.listen(5)

    # Keep accepting new connections.
    while True:
        client_socket, client_address = server.accept()
        # print 'Connection from: ', client_address

        # Handle client in a separate thread.
        thread.start_new_thread(client_handler, (client_socket, client_address))


