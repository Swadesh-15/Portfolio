import http.server
import socketserver
import json
import urllib.request
import os

PORT = 3000

class ProxyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/api/chat':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            api_key = None
            try:
                with open('.env', 'r') as f:
                    for line in f:
                        line = line.strip()
                        if line.startswith('GROQ_API_KEY'):
                            api_key = line.split('=', 1)[1].strip().strip('"').strip("'")
                            break
            except Exception as e:
                print("Error reading .env:", e)

            if not api_key:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'API key not found in .env'}).encode('utf-8'))
                return

            req = urllib.request.Request(
                'https://api.groq.com/openai/v1/chat/completions',
                data=post_data,
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {api_key}',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                },
                method='POST'
            )

            try:
                with urllib.request.urlopen(req) as response:
                    response_data = response.read()
                    self.send_response(response.status)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(response_data)
            except urllib.error.HTTPError as e:
                error_data = e.read()
                self.send_response(e.code)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(error_data)
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': {'message': str(e)}}).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

Handler = ProxyHTTPRequestHandler

# Set allow_reuse_address to True to avoid "Address already in use" errors
socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving files and /api/chat proxy at http://localhost:{PORT}/index.html")
    httpd.serve_forever()
