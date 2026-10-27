"""dashboard: shows how many incidents are open, by calling incident-api."""
import json
import os
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer

API_URL = os.environ.get("API_URL", "http://localhost:8080")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/":
            self.send_error(404)
            return
        try:
            with urllib.request.urlopen(API_URL + "/incidents", timeout=3) as response:
                incidents = json.load(response)["incidents"]
            open_count = sum(1 for item in incidents if item["status"] == "open")
            status, text = 200, f"Open incidents: {open_count}\n"
        except Exception as error:
            print(f"cannot reach API at {API_URL}: {error}", flush=True)
            status, text = 502, f"Dashboard error: cannot reach API at {API_URL}\n"
        data = text.encode()
        self.send_response(status)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


if __name__ == "__main__":
    print(f"dashboard listening on 0.0.0.0:9000, API_URL={API_URL}", flush=True)
    HTTPServer(("0.0.0.0", 9000), Handler).serve_forever()
