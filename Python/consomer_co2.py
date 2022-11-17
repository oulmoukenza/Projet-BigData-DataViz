
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
from pyspark.sql.types import DateType
from pyspark.sql.types import FloatType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import ByteType
import seaborn as sns
import plotly.graph_objects as go


if __name__ == "__main__":

	spark = SparkSession.builder.master("local[*]").appName('app_test').getOrCreate()
	        
	consumer = KafkaConsumer('Hello-Kafka', bootstrap_servers='localhost:9092')

	schema = StructType([StructField("carbonIntensity",StringType(), True)])

			
    
	for msg in consumer:
		df = spark.createDataFrame(msg.value, IntegerType())
		df.show()
		print(df.show())
	
		


		