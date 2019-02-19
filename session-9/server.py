import socket

# Configuring the port and the IP
PORT = 8080
IP = "212.128.253.100"
MAX_OPEN_REQUEST = 5

# Creat a socket with the 2 parameters for connecting to the clients, a socket like a file.
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

serversocket.listen(MAX_OPEN_REQUEST)

print("Socket ready: {}".format(serversocket))

while True:

    print("Waiting for connections at: {}, {}".format(IP, PORT))
    (clientsocket, address) = serversocket.accept() #it will return the client socket and the IP address

    #-- Process the client request
    print("Attending client: {}".format(address))

    #-- Close the socket
    clientsocket.close()