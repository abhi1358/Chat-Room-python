"""Server for multithreaded (asynchronous) chat application."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("Greetings! Now type your name and press enter!", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""

    name = client.recv(BUFSIZ).decode("utf8")
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat!" % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            broadcast(msg, name+": ")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s has left the chat." % name, "utf8"))
            break


def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""

    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)


def receive_file(sock, filename):
    with open(filename, 'wb') as f:
        while True:
            data = sock.recv(BUFSIZ)
            if not data:
                f.close()
                break
            f.write(data)
        print("File Received")
    
    sock.close()
    
    


def file_accept_incoming_connections():
    while True:
        client, client_address = FILE_SERVER.accept()
        filename = "received_file"  # Take from sender
        Thread(target=receive_file, args=(client, filename,)).start()
        


        
clients = {}
addresses = {}

HOST = ''
PORT = 22020
FILE_PORT = 22021

BUFSIZ = 1024

ADDR = (HOST, PORT)
FILE_ADDR = (HOST, FILE_PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

FILE_SERVER = socket(AF_INET, SOCK_STREAM)
FILE_SERVER.bind(FILE_ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    FILE_SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    FILE_ACCEPT_THREAD = Thread(target=file_accept_incoming_connections)
    
    ACCEPT_THREAD.start()
    FILE_ACCEPT_THREAD.start()
    
    ACCEPT_THREAD.join()
    FILE_ACCEPT_THREAD.join()
    
    SERVER.close()
    FILE_SERVER.close()
