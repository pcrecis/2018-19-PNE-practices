import socket

# SERVER IP, PORT
IP = "192.168.1.36"
PORT = 8087

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # The client is blocking the server....  NOT A GOOD DESIGN!!!
    msg = input("> ")
    """We should not put the input after having connected to the server because we block the server, and until we write
     the message other clients have to wait. So you only connect to the server if you have data to send, not before"""

    # Send the request message to the server
    s.send(str.encode(msg))

    # Receive the servers respoinse
    response = s.recv(2048).decode()

    # Print the server's response
    print("Response: {}".format(response))

    s.close()