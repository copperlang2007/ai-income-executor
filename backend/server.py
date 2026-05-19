#!/usr/bin/env python3
"""
Simple Production-Ready Web Dashboard for AI Income Executor
Serves HTML frontend + API endpoints.
Run: python backend/server.py
Access: http://localhost:8080
"""

import http.server
import socketserver
import os
import json
from datetime import datetime

PORT = 8080
DIRECTORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class AIIncomeHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/frontend/index.html'
        elif self.path == '/api/ideas':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            ideas = [
                {"id": 1, "name": "etsy_printables", "title": "Etsy Coloring Pages", "potential": "$5-20/sale", "time": "Hours"},
                {"id": 2, "name": "gumroad_ebooks", "title": "Gumroad eBooks", "potential": "$10-50/book", "time": "1-2 hrs"},
                {"id": 20, "name": "voice_clips", "title": "Voice Clips Licensing", "potential": "Royalties", "time": "Fast"}
            ]
            self.wfile.write(json.dumps(ideas).encode())
            return
        elif self.path == '/api/execute':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "success", "message": "Execution started (demo)"}).encode())
            return
        return super().do_GET()

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

if __name__ == "__main__":
    os.chdir(DIRECTORY)
    with socketserver.TCPServer(("", PORT), AIIncomeHandler) as httpd:
        print(f"🚀 AI Income Executor Dashboard running at http://localhost:{PORT}")
        print("Open in browser. Use CLI for full power: python main.py list")
        httpd.serve_forever()