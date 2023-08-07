from pyspark.sql import SparkSession

'''
RDD - Resilient Distributed Dataset
RDD는 스파크의 기본 데이터 구조로서 분산 변경 불가능한 객체 모음이며
스파크의 모든 작업은 새로운 RDD를 만들거나 존재하는 RDD를 변형하거나
결과 계산을 위해 RDD에 연산하는 것을 표현하고 있다.

RDD의 5가지 특성
Resilent
- Failure 발생시 Lineage Information을 갖고 자동적으로 복구한다.

Distributed
- RDD는 여러 노드에 분산되어 있기에 데이터의 병렬적인 처리를 지원한다.
따라서 대용량 데이터 처리시에 성능이 탁월하다.

Immutable
- RDD는 한번 생성되면 그 데이터는 변경될 수 없다. RDD에
transformation이 발생하면 새로운 RDD를 생성한다. data 일관성과
fault-tolerance하기 위해서

Lazy evaluation
- RDD에 대한 transformation이 즉시 이루어지지 않는다. 대신
transformation의 일련의 과정으로 기록해놓고 call 되기 전까지는 실행되지 않음
이 기능 덕분에 Spark가 transformation을 엮어서 효율적으로 처리할 수 있게 한다.

In Memory Computing
- 메모리에 데이터를 올려두고 하기에 데이터를 여러번 올렸다 내렸다 할 필요가 없다.
'''

spark = SparkSession.builder\
    .master("local[1]")\
    .appName("SparkByExamples.com")\
    .getOrCreate()

dataList = [("Java", 200000), ("Python", 100000), ("Scala", 3000)]
rdd = spark.sparkContext.parallelize(dataList)
print(rdd.collect())
print(rdd.collect())
print(rdd.take(1)) # 처음 N개 보여주기 take()
print(rdd.take(2))
print(rdd.take(3))


data = [('James','','Smith','1991-04-01','M',3000),
('Michael','Rose','','2000-05-19','M',4000),
('Robert','','Williams','1978-09-05','M',4000),
('Maria','Anne','Jones','1967-12-01','F',4000),
('Jen','Mary','Brown','1980-02-17','F',-1)
]

columns = ["firstname","middlename","lastname","dob","gender","salary"]
df = spark.createDataFrame(data=data, schema = columns)
# Spark dataframe은 csv, text, xml 등 여러 파일 포맷 지원한다.
df.show()

# SQL을 사용하기 위해서는 dataframe을 임시 테이블로 만들어야한다. 
# 해당 테이블에 sql() 메소드를 활용하여 쿼리를 날리면 새로운 데이터프레임을 return한다.

df.createOrReplaceTempView("PERSON_DATA")
df2 = spark.sql("SELECT firstname, gender, salary FROM PERSON_DATA")
df2.printSchema()
df2.show()