from kafka import KafkaProducer
import yahoo_fin.stock_info as fi
from datetime import datetime
from json import dumps
import pandas as pd
from time import sleep

if __name__ == "__main__":
	
	producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
	                         value_serializer=lambda x: dumps(x).encode('utf-8'),
	                         api_version=(2,0,2))

	for e in range(1, 10000):
	    
	    data = {
			"date":str(datetime.now()),
	    	"petrol": fi.get_live_price("BZ=F"),
			"gaz": fi.get_live_price("NG=F")
	    	
	    }

	    print("send N°: ",e)
	    producer.send('Hello-Kafka', value=data)
	    print(data)
	    sleep(1)
