import requests
import math
import random 
import time
from random import randrange


message = "http://127.0.0.1:8081/motor={}?position={}?speed={}"


def random_head_turn_nod():
	requests.get(message.format(1,round(random.uniform(4,6),3),1))
	requests.get(message.format(0,round(random.uniform(4,6),3),1))	

def blink():
	requests.get(message.format(3,round(random.uniform(0,1),3),randrange(1,3)))
	time.sleep(round(random.uniform(0,0.3),1))
	requests.get(message.format(3,round(random.uniform(3,6),3),1))

def eye_lid_tilt():
	requests.get(message.format(2,round(random.uniform(0,10),3),1))
	requests.get(message.format(3,round(random.uniform(1,9),3),1))
	requests.get(message.format(6,round(random.uniform(2,8),3),1))

def slight_mouth_move():
	requests.get(message.format(4,round(random.uniform(5,6),3),1))
	requests.get(message.format(5,round(random.uniform(5,6),3),1))

def shake_disagreement(num_shakes):
	requests.get(message.format(1,5,1))
	time.sleep(0.2)
	requests.get(message.format(3,1,1))
	time.sleep(0.2)
	requests.get(message.format(4,5,1))
	requests.get(message.format(5,5,1))

	for i in range(num_shakes):
		# disagreement_size = round(random.uniform(0.7,1)
		disagreement_size = 0.4
		requests.get(message.format(1,5 - disagreement_size,1))
		time.sleep(0.7)
		requests.get(message.format(1,5 + disagreement_size,1))	
		time.sleep(0.7)

def agree_nod(nod_times):

	for i in range(nod_times):
		requests.get(message.format(0,5,1))
		agreement_size = round(random.uniform(0.5,1.3))
		requests.get(message.format(0,5-agreement_size,1))
		time.sleep(0.8)
		requests.get(message.format(0,5+agreement_size,1))
		time.sleep(0.6)

def centrlize_face():
		requests.get(message.format(1,5,1))
		time.sleep(0.2)
		requests.get(message.format(0,5,1))
		time.sleep(0.2)
		requests.get(message.format(2,5,1))
		time.sleep(0.2)
		requests.get(message.format(3,5,1))
		time.sleep(0.2)

if __name__ == "__main__":

	for i in range(30):
		centrlize_face()

		if i%10==0:
			agree_nod(2)

		random_head_turn_nod()
		blink()
		time.sleep(round(random.uniform(0.5,1.8),3))

		eye_lid_tilt()
		time.sleep(round(random.uniform(0.3,1.6),3))
		slight_mouth_move()

		if i==0:
			shake_disagreement(4)

		print("yo ",i)














# instruction = message.format(1,3,5)
# 127.0.0.1:9976/move?engine=1?x=1?y=2.2?speed=1.1
# r = requests.get(url)
# print(r.content)
