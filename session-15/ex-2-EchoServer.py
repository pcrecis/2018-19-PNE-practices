import http.server
import socketserver
import termcolor

PORT = 8008


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self): #it is essential to use this name, with any other it won work

        print(' Cmd: ' + self.command)
        print(' Path: ' + self.path)

        #-- printing the request line
        termcolor.cprint(self.requestline, 'green')

        if self.path == '/':
            f = open("ex-2-form.html")
            content = f.read()
            f.close()
        elif "msg" in self.path:
            msg_sent = self.path[self.path.find("=") +1:]
            if "chk" in self.path:
                msg_sent = msg_sent.split("&")[0]
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
                            </html.>""".format(msg_sent.upper()))
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

print(" The server is stopped")