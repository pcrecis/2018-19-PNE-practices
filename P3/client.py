import socket
import termcolor

# SERVER IP, PORT
PORT = 8096
IP = "212.128.253.99"

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    set = ""
    while True:
        msg = (input("Introduce: ") + "\n")
        if msg and msg.strip():
            set += msg
        else:
            break

    if len(set) == 0:
        set = " "

    s.send(str.encode(set))
    print(set)

    # Send the request message to the server

    # Receive the servers respoinse
    response = s.recv(2048).decode('utf-8')

    # Print the server's response
    termcolor.cprint("Response: \n{}".format(response), 'red')

    s.close()