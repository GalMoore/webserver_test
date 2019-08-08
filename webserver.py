#!/usr/bin/env python
 
from http.server import BaseHTTPRequestHandler, HTTPServer
from ohbot import ohbot
import re


# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
 
  # GET 
  # MOVE THE ROBOT! 
  def do_GET(self):
        # keep this- otherwise ERROR 
        # Send response status code
        self.send_response(200)
        # Send headers
        # self.send_header('Content-type','text/html')
        self.end_headers()

        string_to_split = self.path.replace("/","")
        array_of_words = re.split('[^a-zA-Z0-9]', string_to_split)

        print(array_of_words)

        ohbot.move(int(array_of_words[1]),int(array_of_words[3]),int(array_of_words[5]))

        #   # Send message back to client
        #   message = "Hello world!" +"\n"
        #   # Write content as utf-8 data
        #   # self.wfile.write writes to window where we curl
        #   self.wfile.write(bytes(message, "utf8"))

        return
  
# curl 127.0.0.1:9976/move?engine=1?x=1?y=2.2?speed=1.1

def run(): 
  # Server settings
  print("starting server")
  # Choose port 8080, for port 80, which is normally used for a http server, 
  # you need root access
  server_ip = "127.0.0.1"
  server_port = 8081
  # server_port_str = str(server_port)
  # server_address = ('127.0.0.1', 8081)
  server_address = (server_ip,server_port)
  sentence = 'ip: {}\nport: {}'
  print(sentence.format(server_ip,server_port))

# print("Hello, %s!" % name)

  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()
 
run()
