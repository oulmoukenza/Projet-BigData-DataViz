from kafka import KafkaProducer
import json
import requests
p = KafkaProducer(bootstrap_servers="localhost:9092")
import time
i = 0
while True:

    url = "https://api-access.electricitymaps.com/tw0j3yl62nfpdjv4/power-breakdown/latest?lat=48.8566&lon=2.3522"
    headers = {
    "X-BLOBR-KEY": "Tq7G320ku9KSxHxNq5DIDNziwsvcB59y"
    }

    data_elemap = requests.get(url, headers=headers)
    p.send('test3', json.dumps(data_elemap.text).encode('utf-8'))
    p.flush()
    print(data_elemap)
    time.sleep(3)
    i += 1