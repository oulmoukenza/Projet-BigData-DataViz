
import findspark
findspark.init()
import pyspark
from pyspark.sql import SparkSession
from xml.dom.minicompat import StringTypes
from kafka import KafkaConsumer
import pandas as pd
from time import sleep
from json import dumps
import json
import warnings 
warnings.filterwarnings('ignore')
from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StructType
from pyspark.sql.types import StringType
from pyspark.sql.types import FloatType
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



if __name__ == "__main__":
     
	spark = SparkSession.builder.master("local[*]").appName('app_test').getOrCreate()
	        
	consumer = KafkaConsumer('Hello-Kafka', bootstrap_servers='localhost:9092')

	
	schema = StructType([  StructField("date",StringType(), True),
	                       StructField("petrol",FloatType(), True), 
						   StructField("gaz",FloatType(), True)
						  ])

    
	for msg in consumer:
		data = pd.DataFrame(json.loads(msg.value),index=[0])
		df = spark.createDataFrame( data = data, schema = schema)
		print(df.select("date","petrol", "gaz").show())
			
		
		print("< recieved ... >")
		sleep(1)
		


		