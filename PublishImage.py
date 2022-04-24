import http.server
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer

class mJPEGRequestHandler(BaseHTTPRequestHandler ):
    #def __init__(self):
        #self.getImage = getImage
    def do_GET(self):
        self.send_response(200)# say the request worked
        self.send_error("content-type", "image/jpeg")
        self.end_headers()

        self.wfile.write(self.getImage())
        return




http = ThreadingHTTPServer(('', 9000), mJPEGRequestHandler)
http.serve_forever()