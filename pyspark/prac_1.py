from pyspark.sql import SparkSession
from pyspark.sql.types import ArrayType, StringType, MapType, IntegerType
from pyspark.sql.functions import udf, array, explode
from collections import defaultdict, Counter
import re

def tokenizer(text):
    '''
    파이썬 정규식을 활용한 tokenizer입니다.
    '''
    if not isinstance(text, str):
        text = str(text)
    tokens = []
    pattern = re.compile(r'([가-힣]+|[ㄱ-ㅎㅏ-ㅣ]+|[a-zA-Z0-9-]+|[^\s])')
    matches = pattern.finditer(text)

    for match in matches:
        word = match.group()
        tokens.append(word)

    return tokens

def count_tokens(tokens):
    counter = Counter(tokens)
    return dict(counter)

count_tokens_udf = udf(count_tokens, MapType(StringType(), IntegerType()))
tokenize_udf = udf(tokenizer, ArrayType(StringType()))
# Create a SparkSession
spark = SparkSession.builder.appName("bgzt slasher").getOrCreate()

file_path = "../dataset/de_exam_product.parquet"

df = spark.read.format("parquet").load(file_path)

df_tokenized = df.withColumn("name", tokenize_udf("name")) \
                .withColumn("description", tokenize_udf("description")) \
                .withColumn("tokens", array("name", "description"))

df_flattend = df_tokenized.select("id", "name", explode("tokens").alias("tokens"))
df_flattend = df_flattend.withColumn("TF", count_tokens_udf("tokens"))
df_flattend.show(truncate=False)