import requests

# url = "http://127.0.0.1:8081/move"

url = "http://127.0.0.1:8081/motor=1?position=2?speed=1"
# 127.0.0.1:9976/move?engine=1?x=1?y=2.2?speed=1.1

# r = requests.get(url)
# print(r.content)

normal_content = requests.get(url).content
# url_time_content = requests.get(url_time).content

