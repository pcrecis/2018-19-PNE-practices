import http.server
import socketserver

# Define the Server's port
PORT = 8003


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        print("GET received!")

        print('Request line:' + self.requestline)
        print(' Cmd: ' + self.command)
        print(' Path: ' + self.path)

        if self.path == '/':
            f = open("index.html")
            content = f.read()
            f.close()
        elif self.path == '/pink':
            f = open("pink.html")
            content = f.read()
            f.close()
        elif self.path == '/blue':
            f = open("blue.html")
            content = f.read()
            f.close()
        else:
            f = open("error.html")
            content = f.read()
            f.close()

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')        #Content type, to know the type of message
        self.send_header('Content-Length', len(str.encode(content)))
        self.end_headers()

        self.wfile.write(str.encode(content))
        return


# ------------------------
# - Server MAIN program
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()

print("")
print("Server Stopped")