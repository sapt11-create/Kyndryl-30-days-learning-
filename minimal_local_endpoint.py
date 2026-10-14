"""
+--------------------------------+
| Client sends a GET request     |
| GET /student                   |
+--------------------------------+
                |
                v
+--------------------------------+
| Python Server                  |
| Receives request on port 8000  |
+--------------------------------+
                |
                v
+--------------------------------+
| Check the endpoint             |
| Is the path /student?          |
+--------------------------------+
          /             \
        YES              NO
         |                |
         v                v
+------------------+  +------------------+
| HTTP 200         |  | HTTP 404         |
| Return student   |  | Endpoint not     |
| JSON             |  | found             |
| ID, name, course |  +------------------+
+------------------+           |
         |                     |
         v                     v
+------------------+  +------------------+
| Client receives  |  | Client receives  |
| student response |  | error response   |
+------------------+  +------------------+
         |                     |
         +----------+----------+
                    |
                    v
          +------------------+
          |       End        |
          +------------------+
"""


# 2. Creating minimal local endpoint

from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class MyAPI(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/student":
            data = {
                "id": 1,
                "name": "Rahul",
                "course": "Python"
            }

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            self.wfile.write(json.dumps(data).encode())

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

server = HTTPServer(("localhost", 8000), MyAPI)

print("Server running at http://localhost:8000")
server.serve_forever()
