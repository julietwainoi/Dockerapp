import os
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        response = f"""
PID: {os.getpid()}
Hostname: {socket.gethostname()}
Current directory: {os.getcwd()}
Files in /data: {os.listdir('/data') if os.path.exists('/data') else 'No /data'}
"""
        self.wfile.write(response.encode())

server = HTTPServer(("0.0.0.0", 8080), Handler)
print("Server running on port 8080")
server.serve_forever()
