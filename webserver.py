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
        # array_of_words = re.split('[^a-zA-Z0-9]', string_to_split)
        nums = re.findall('\d*\.?\d+',string_to_split)
        motor_num = int(nums[0])
        motor_position = float(nums[1])
        speed = int(nums[2])
        print("moving motors now with", nums)
        # print(motor_num)
        # print(motor_position)

        ohbot.move(motor_num,motor_position,speed)

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
