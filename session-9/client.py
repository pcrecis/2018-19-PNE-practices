import socket
import termcolor

# SERVER IP, PORT
PORT = 8087
IP = "212.128.253.100"

while True:
    # You only connect to the server if you have data to send, not before
    msg = input("Introduce the message: ")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # Send the request message to the server
    s.send(str.encode(msg))

    # Receive the servers respoinse
    response = s.recv(2048).decode()

    # Print the server's response
    termcolor.cprint("Response: {}".format(response), 'red')

    s.close()