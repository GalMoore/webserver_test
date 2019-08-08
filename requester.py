import requests
import math
import random 
import time
from random import randrange
# instruction = "http://127.0.0.1:8081/motor={}?position={}?speed={}".format(1,3,5)
# 127.0.0.1:9976/move?engine=1?x=1?y=2.2?speed=1.1

# r = requests.get(url)
# print(r.content)

for i in range(10):
	# position = round(random.uniform(2,8),1)
	# print(position)

	command_nod = "http://127.0.0.1:8081/motor={}?position={}?speed={}".format(0,round(random.uniform(3,9),1),1)
	command_turn = "http://127.0.0.1:8081/motor={}?position={}?speed={}".format(1,round(random.uniform(3,7),1),1)
	command_eyes = "http://127.0.0.1:8081/motor={}?position={}?speed={}".format(2,round(random.uniform(1,9),1),1)
	command_eye_lids = "http://127.0.0.1:8081/motor={}?position={}?speed={}".format(3,round(random.uniform(1,9),1),1)
	command_eye_tilt = "http://127.0.0.1:8081/motor={}?position={}?speed={}".format(6,round(random.uniform(2,8),1),1)
	command_top_lip = "http://127.0.0.1:8081/motor={}?position={}?speed={}".format(4,round(random.uniform(5,7),1),1)
	command_bottom_lip = "http://127.0.0.1:8081/motor={}?position={}?speed={}".format(5,round(random.uniform(5,7),1),1)


	requests.get(command_turn).content
	requests.get(command_nod).content
	time_delay = round(random.uniform(1,2),3)
	time.sleep(time_delay)

	requests.get(command_eyes).content
	requests.get(command_eye_lids).content
	requests.get(command_eye_tilt).content
	time_delay = round(random.uniform(0,3),3)
	time.sleep(time_delay)

	requests.get(command_top_lip).content
	requests.get(command_bottom_lip).content

	print("yo ",i)

# url_time_content = requests.get(url_time).content

