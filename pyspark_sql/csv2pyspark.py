import json
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark=SparkSession.builder.appName("pyspark_sql").getOrCreate()
spark.sql("set spark.sql.legacy.timeParserPolicy=LEGACY")
ratings=spark.read.csv('../data/ratings.csv', header=True, inferSchema=True)
pyspark_queries=open('../config/pyspark_queries.json')
query_data=json.load(pyspark_queries)

# executing pyspark queries one by one

for query, pdtxt in query_data.items():
    print(query+':\n')
    exec(pdtxt)