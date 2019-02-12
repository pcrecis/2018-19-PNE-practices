# We are programming our first client

import socket

# Create a socket for communicating with the server

condition = True
while condition:
    c = input("What you want to write? : ")
    if c == 'exit':
        condition = False
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # we always use these 2 PARAMETERS, it is like opening a file

    print("Socket created")

    PORT = 8081
    IP = "212.128.253.100"

    # Connect to the server
    s.connect((IP, PORT))

    s.send(str.encode(c))

    msg = s.recv(2048).decode("utf-8")
    print("MESSAGE FROM THE SERVICE")
    print(msg)

    s.close()

print("The end")