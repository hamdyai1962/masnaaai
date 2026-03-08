import http.server
import socketserver
import os
import webbrowser

PORT = 3000
os.chdir(r"C:\HamdyAI-Factory\dist")

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache')
        super().end_headers()
    
    def log_message(self, format, *args):
        pass

print("")
print("  ========================================")
print("  HAMDY.AI Factory v2.0 is running!")
print("  http://localhost:3000")
print("  ========================================")
print("")
print("  [!] Important: Disable AdBlocker on this page!")
print("  [!] مهم: أوقف مانع الإعلانات على هذه الصفحة!")
print("")
print("  Press Ctrl+C to stop")
print("")

webbrowser.open("http://localhost:3000")

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n  Server stopped.")