from kafka import KafkaProducer
import json
import requests
from datetime import datetime
from json import dumps
import pandas as pd
from time import sleep

p = KafkaProducer(bootstrap_servers=['localhost:9092'],
	                         value_serializer=lambda x: dumps(x).encode('utf-8'),
	                         api_version=(2,0,2))
i = 0
while True:

    url = "https://api-access.electricitymaps.com/tw0j3yl62nfpdjv4/carbon-intensity/latest?zone=FR"
    headers = { "X-BLOBR-KEY":"gLdlqaQBBEaSfAuX5UIcWNUnaVD3Zpmn"}

    data_co2 = requests.get(url, headers=headers)
    contenu_txt = json.loads(data_co2.text)
 
    print(contenu_txt)
   
    p.send('Hello-Kafka', value=contenu_txt)
    p.flush()
    sleep(2)
    i += 1
   
  