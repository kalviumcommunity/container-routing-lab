"""incident-api: returns incidents as JSON. Standard library only."""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = "127.0.0.1"
PORT = 8080

INCIDENTS = [
    {"id": 1, "title": "Checkout page slow", "status": "open"},
    {"id": 2, "title": "Login email delayed", "status": "resolved"},
]


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            body = {"status": "ok"}
        elif self.path == "/incidents":
            body = {"incidents": INCIDENTS}
        else:
            self.send_error(404)
            return
        data = (json.dumps(body) + "\n").encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


if __name__ == "__main__":
    print(f"incident-api listening on {HOST}:{PORT}", flush=True)
    HTTPServer((HOST, PORT), Handler).serve_forever()
