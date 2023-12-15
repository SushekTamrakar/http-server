from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import time

HOST = "172.19.29.72"
PORT = 9999


class HTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")

        self.end_headers()

        self.wfile.write(bytes("<html><body><h1> HELLO WORLD! </body></html>", "utf-8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")

        self.end_headers()

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.wfile.write(bytes())


server = HTTPServer((HOST, PORT), HTTPRequestHandler)
print("Server is now running in Port", HOST)

sdfasdfsadf
sdsadas
asdasdasdasdas
asdasdasdasdasdasdas
asdasdasdasdasdasdasdasd
sadsdasdasdasdasdasdasd
asdasdasdasdasdasdasdasdasdasasd
asdasdasdasdasd
asdfasdfa
asdasdasdasdadasdasdasdasdaaaaaaaaaassddddqweqweqweqweqweqwew
asdfasdfasqqweqweqweqweqweqwewqeqwe
xzcvzxcvzcvzvz
sdasdasdSADSDASSADA

server.serve_forever()
server.server_close()
print('Server Stopped')




    