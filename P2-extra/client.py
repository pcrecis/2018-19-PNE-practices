import socket

PORT = 8083
IP = "212.128.253.100"

condition = True
while condition:
    seq = input("Please, introduce a sequence: ").upper()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created")
    # Connect to the server

    s.connect((IP, PORT))

    s.send(str.encode(seq))

    msg = s.recv(2048).decode("utf-8")
    print("MESSAGE FROM THE SERVER, the complement sequence is: {}".format(msg))

    s.close()

print("The end")