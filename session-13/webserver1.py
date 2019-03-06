import http.server
import socketserver

# Define the Server's port
PORT = 8005

# -- Use the http.server Handler
Handler = http.server.SimpleHTTPRequestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd: # inside "" we are inserting our local IP address
    print("Serving at PORT", PORT)

    httpd.serve_forever()











