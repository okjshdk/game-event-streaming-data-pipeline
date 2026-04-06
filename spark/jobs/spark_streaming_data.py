from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark = SparkSession.builder \
        .appName("EventGameStreamingData") \
        .config(
            "spark.jars.packages",
            "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1,"
            "org.apache.hadoop:hadoop-aws:3.3.4"
        ) \
        .config("spark.hadoop.fs.s3a.endpoint", "http://minio:9000") \
        .config("spark.hadoop.fs.s3a.access.key", "minio") \
        .config("spark.hadoop.fs.s3a.secret.key", "minio123") \
        .config("spark.hadoop.fs.s3a.path.style.access", "true") \
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
        .config("spark.hadoop.fs.s3a.connection.ssl.eclenabled", "false") \
        .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

schema = StructType([
    StructField("event_id", StringType(), False),
    StructField("game_id", StringType(), False),
    StructField("event_name", StringType(), False),
    StructField("platform", StringType(), False),
    StructField("event_time", StringType(), False),
    StructField("properties", MapType(StringType(), StringType()), True)
])

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:29092") \
    .option("subscribe", "streaming-data") \
    .option("startingOffsets", "earliest") \
    .load()

parsed_df = df.selectExpr("CAST(value AS STRING) AS json_value") \
    .select(from_json(col("json_value"), schema).alias("data")) \
    .select("data.*")

cleaned_df = parsed_df.withColumn("game_id", col("game_id").cast("int")) \
    .withColumn("event_time", to_timestamp("event_time")) \
    .withColumn("date", to_date("event_time"))

cleaned_df = cleaned_df.withWatermark("event_time", "1 hour") \
    .dropDuplicates(["event_id"])


bronze_query = cleaned_df.writeStream \
    .format("parquet") \
    .outputMode("append") \
    .trigger(processingTime="1 minute") \
    .option("checkpointLocation", "s3a://game-datalake/checkpoint") \
    .option("path", "s3a://game-datalake/bronze/game_events") \
    .partitionBy("date") \
    .start()

bronze_query.awaitTermination()