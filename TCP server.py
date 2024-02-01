#!/usr/bin/python3

import socket

#creating the socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 444

#binding to socket
serversocket.bind(('192.168.100.14', port)) #host will be replaced with ip, if changed and not running on host

#starting to TCP listener
serversocket.listen(3)

while True:
    #starting the connection
    client, socket = serversocket.accept()
    
    print("received connection from " % str(address))
    
    message = 'Hello ! thank you for connecting to the server' + "\r\n"
    clientsocket.send(message.encode('ascii'))
    
    clientsocket.close()
    