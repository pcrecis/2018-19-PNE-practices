import http.server
import socketserver
import termcolor
from Seq import Seq

PORT = 8002


def valid_characters(seq):
    valid = 'ACTG'
    for l in seq:
        if l not in valid:
            return False
    return True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self): #it is essential to use this name, with any other it won work

        print(' Cmd: ' + self.command)
        print(' Path: ' + self.path)

        #-- printing the request line
        termcolor.cprint(self.requestline, 'green')

        if self.path == '/':
            f = open("form.html")
            content = f.read()
            f.close()
        elif "msg" in self.path:
            msg_sent = self.path.split("&")
            print(msg_sent)
            seq = msg_sent[0][msg_sent[0].find("=") +1:]
            print(seq)
            if valid_characters(seq.upper()):
                content = ("""<!DOCTYPE html>
                            <html lang="en">
                            <head>
                                <meta charset="UTF-8">
                                <title>RESPONSEOF THE SEQUENCE RECEIVED:</title>
                            </head>
                            <body style="background-color: lightpink;">
                                <h1>Echo</h1>
                                <p>{}</p>
                                <br>
                                <p>{}</p>
                                <br>
                                <p>{}</p>
                                <br>
                                <a href="/">Main page</a>
                            </body>
                            </html.>""")

                seq = Seq(seq)
                sequence = ""
                length = ""
                operation = ""

                sequence += "Sequence: " + str(seq)
                print(sequence)

                for i in range(len(msg_sent)):
                    if "chk=on" in msg_sent[i]:
                        tl = seq.len()
                        length += "Len:" + str(tl)
                        print(length)
                    elif "base" in msg_sent[i]:
                        base = msg_sent[i].split("=")
                        b = base[1]
                    elif "operation" in msg_sent[i]:
                        oper = msg_sent[i].split("=")
                        if oper[1] == "count":
                            counter = seq.count_bases(b)
                            operation += "Base {} appears {} times in the sequence".format(b, str(counter))
                            print(operation)
                        elif oper[1] == "perc":
                            perc = seq.perc(b)
                            operation += "The percentage for base {} is: {}".format(b, str(perc))
                            print(operation)

                content = content.format(sequence, length, operation)

            else:
                f = open("error.html")
                content = f.read()
                f.close()
        else:
            f = open("error.html")
            content = f.read()
            f.close()

        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(content)))
        self.end_headers() # we indicate the haeder is done

        # -- Sending the body of the response message
        self.wfile.write(str.encode(content))


# -- Main program
with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at PORT: {}".format(PORT))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
