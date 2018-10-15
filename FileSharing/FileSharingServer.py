import socket
from threading import Thread
#from SocketServer import ThreadingMixIn

TCP_IP = 'localhost'
TCP_PORT = 9001
BUFFER_SIZE = 1024

class ClientThread(Thread):

    def __init__(self, ip, port, sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        print("New Thread for "+ip+":"+str(port))


    def run(self):
        print('run method running')
        #filename = 'file.txt'
        filename = 'vid.m4v'
        f = open(filename,'rb')
        print("file opened")
        while True:
            l = f.read(BUFFER_SIZE)
            #print("Value of l: ", l)
            while(l):
                self.sock.send(l)
                l = f.read(BUFFER_SIZE)
            if not l:
                f.close()
                self.sock.close()
                break

tcpsock  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    tcpsock.listen(5)
    print("Waiting for incoming connections")
    (conn, (ip, port)) = tcpsock.accept()
    print("Got connection from ",(ip, port) )
    newthread = ClientThread(ip, port, conn)
    newthread.start()
    print('thread Started')
    threads.append(newthread)

for t in threads:
    t.join()
