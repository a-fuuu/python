from pyspark.sql import SparkSession

spark = SparkSession.builder\
    .master("local[1]")\
    .appName("Spark")\
    .getOrCreate()

file_path = '../dataset/Airline Dataset.csv'

df = spark.read.option("header", True).csv(file_path)

# df.show()

df.createOrReplaceTempView('airplane')

result = spark.sql('''SELECT `Country Name`, COUNT(`Passenger ID`) AS num_of_passenger 
                   FROM airplane
                   GROUP BY `Country Name`
                   ORDER BY num_of_passenger DESC;''')
result.show()

# pyspark sql에서 띄어쓰기가 있는 column을 select 할떄는 ``(backticks)로 묶어줘야한다.
result = spark.sql('''SELECT `Airport Name`, COUNT(`Passenger ID`) AS num_of_passenger 
                   FROM airplane
                   GROUP BY `Airport Name`
                   ORDER BY num_of_passenger DESC;''')
result.show()
