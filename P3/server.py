import socket

import termcolor
from Seq import Seq

# Configure the Server's IP and PORT
PORT = 8096
IP = "212.128.253.99"
MAX_OPEN_REQUESTS = 5

def valid_characters(seq):
    valid = 'ACTG'
    for l in seq:
        if l not in valid:
            return False
    return True

# Counting the number of connections
number_con = 0

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    serversocket.bind((IP, PORT))
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        # accept connections from outside
        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (clientsocket, address) = serversocket.accept()

        # Another connection!e
        number_con += 1

        # Print the conection number
        print("CONNECTION: {}. From the IP: {}".format(number_con, address))

        # Read the message from the client, if any
        msg = clientsocket.recv(2048).decode("utf-8")
        if msg == " ":
            # Send the message
            message = "ALIVE"
            send_bytes = str.encode(message)
            # We must write bytes, not a string
            clientsocket.send(send_bytes)
            clientsocket.close()
        else:
            note = msg.split("\n")
            new_msg = ""
            if valid_characters(note[0]):
                message = 'OK\n'
                new_msg += message
                termcolor.cprint('Message from client: {}'.format(note), 'blue')
                s1 = Seq(note[0])
                note.pop(0)
                for i in range(len(note)):
                    if note[i] == 'len':
                        tl = s1.len()
                        message = str(tl)
                        new_msg += message +'\n'
                    elif note[i] == 'complement':
                        c1 = s1.complement()
                        new_msg += c1 + '\n'
                    elif note[i] == 'reverse':
                        r1 = s1.reverse()
                        new_msg += r1 + '\n'
                    elif note[i] == 'countA':
                        counter_A = s1.count_bases('A')
                        message = str(counter_A)
                        new_msg += message + '\n'
                    elif note[i] == 'countT':
                        counter_T = s1.count_bases('T')
                        message = str(counter_T)
                        new_msg += message + '\n'
                    elif note[i] == 'countG':
                        counter_G = s1.count_bases('G')
                        message = str(counter_G)
                        new_msg += message + '\n'
                    elif note[i] == 'countC':
                        counter_C = s1.count_bases('C')
                        message = str(counter_C)
                        new_msg += message + '\n'
                    elif note[i] == 'percA':
                        perc_A = s1.perc('A')
                        message = str(perc_A)
                        new_msg += message + '%' + '\n'
                    elif note[i] == 'percT':
                        perc_T = s1.perc('T')
                        message = str(perc_T)
                        new_msg += message + '%' + '\n'
                    elif note[i] == 'percG':
                        perc_G = s1.perc('G')
                        message = str(perc_G)
                        new_msg += message + '%' + '\n'
                    elif note[i] == 'percC':
                        perc_C = s1.perc('C')
                        message = str(perc_C)
                        new_msg += message + '%' + '\n'
                    elif note[i] == '':
                        pass
                    else:
                        message = 'ERROR\n'
                        new_msg += message
            else:
                message = 'ERROR'
                new_msg += message
        clientsocket.send(str.encode(new_msg))
        clientsocket.close()

except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()