import http.server
import socketserver
import termcolor

PORT = 8000


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self): #it is essential to use this name, with any other it won work

        #-- printing the request line
        termcolor.cprint(self.requestline, 'green')

        f = open("form2.html", 'r')
        contents = f.read()

        self.send_response(200) #what is the status of the response, 200 means everythin is ok

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers() # we indicate the haeder is done

        # -- Sending the body of the response message
        self.wfile.write(str.encode(contents))


# -- Main program
with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at PORT: {}".format(PORT))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

print(" The server is stopped")

