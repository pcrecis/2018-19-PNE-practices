import socket
import termcolor
import sys

# Configuring the port and the IP
PORT = 8087
IP = "212.128.253.100"
MAX_OPEN_REQUEST = 5

def process_client(cs):
    # Reading the message from the client
    msg = cs.recv(2048).decode("utf-8")
    if msg == 'EXIT':
        sys.exit(0)
    else:
        termcolor.cprint("Message from the client: {}".format(msg), 'red')

    # Sending the message back to the client
    # (because we are an echo server)
    cs.send(str.encode('Message sent'))

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

    process_client(clientsocket)