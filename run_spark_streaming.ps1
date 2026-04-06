docker exec -u root -it spark-master /opt/spark/bin/spark-submit `
  --master spark://spark-master:7077 `
  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1,org.apache.hadoop:hadoop-aws:3.3.4 `
  /opt/spark/jobs/spark_streaming_data.py