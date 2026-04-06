### Data Engineer Project | End-to-end Game Event Streaming Data Pipeline

# 1. Tổng quan
  Dự án này xây dựng 1 pipeline end-to-end để thu thập, xử lý và lưu trữ dữ liệu game events \
  từ các trò chơi online theo giời gian thực vào data lake.

# 2. Kiến trúc hệ thống
  Hệ thống bao gồm các thành phần như sau:
    - Data Source: Dữ liệu người dùng về game events (login, purchase, ...) được tạo ngẫu nhiên.
    - Apache Airflow: Được dùng để điều phối và thu thập dữ liệu từ source.
    - Apache Kafka và Zookeeper: Tiếp nhận, lưu trữ và quản lý event stream data.
    - Kafka UI: Giám sát và theo dõi hiệu suất của kafka broker.
    - Apache Spark: Xử lý, làm sạch, chuyển đổi event stream data và lưu vào data lake.
    - Minio: Nơi lưu trữ dữ liệu sau khi được xử lý.
    - PostgreSQL: Lưu trữ metadata cho Airflow.

# 3. Công nghệ sử dụng
  - Storage: MinIO, PostgreSQL
  - Streaming/Message Queue: Apache Kafka, Zookeeper
  - Processing: Apache Spark (PySpark)
  - Orchestration: Apache Airflow
  - Infrastructure: Docker, Docker Compose

# 4. Hướng dẫn chạy project
  - B1: Run docker-compose.yml: docker compose up -d
  - B2: Run DAG in Airflow (http://localhost:8080/)
  - B3: Run spark streaming job in terminal: .\run_spark_streaming.ps1 
