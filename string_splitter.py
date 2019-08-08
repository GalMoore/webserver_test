import re

# curl 127.0.0.1:9976/move?engine=1?x=1?y=2.2?speed=1.1


string_to_split = "/motor=4?position=2?speed=1"

string_to_split = string_to_split.replace("/","")
array_of_words = re.split('[^a-zA-Z0-9]', string_to_split)

print(array_of_words)