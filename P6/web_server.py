import http.server
import socketserver
import termcolor
from Seq import Seq

PORT = 8001


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
            seq = msg_sent[0][msg_sent[0].find("=") +1:]
            if valid_characters(seq):
                content = ("""<!DOCTYPE html>
                            <html lang="en">
                            <head>
                                <meta charset="UTF-8">
                                <title>RESPONSEOF THE SEQUENCE RECEIVED:</title>
                            </head>
                            <body style="background-color: lightpink;">
                                <h1>Echo</h1>
                                <p>Sequence: {}</p>
                                <br>
                                <p>Len: {}</p>
                                <br>
                                <p>Len: {}</p>
                                <a href="/">Main page</a>
                            </body>
                            </html.>""")
                length = ""

                for i in range(len(msg_sent)):
                    if "chk" in self.path:
                        tl = seq.len()

            else:
                content = ("""<!DOCTYPE html>
                            <html lang="en">
                            <head>
                                <meta charset="UTF-8">
                                <title>Echo of the received message:</title>
                            </head>
                            <body style="background-color: lightgreen;">
                                <h1>Echo</h1>
                                <p>{}</p>
                                <a href="/">Main page</a>
                            </body>
                            </html.>""".format(msg_sent.lower()))

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
