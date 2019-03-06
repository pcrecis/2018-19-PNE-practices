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

        content = "I am the happy server! :)"

        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')        #Content type, to know the type of message
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