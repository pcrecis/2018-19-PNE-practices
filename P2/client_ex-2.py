# We are programming a client

import socket
from Seq import Seq

# Create a socket for communicating with the server

PORT = 8082
IP = "212.128.253.95"

condition = True
while condition:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created")
    s.connect((IP, PORT))

    s1 = input("Please, enter a sequence: ").upper()
    if s1 == 'exit':
        condition = False

    else:
        s1 = Seq(s1)
        s2 = Seq(s1.reverse())
        s3 = s2.complement()
        s.send(str.encode(s3))

    s.close()

print("The end")