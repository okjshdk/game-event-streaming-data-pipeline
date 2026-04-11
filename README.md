### Data Engineer Project | End-to-end Game Event Streaming Data Pipeline

# 1. Tổng quan
  Dự án này xây dựng 1 pipeline end-to-end để thu thập, xử lý và lưu trữ dữ liệu game events \
  từ các trò chơi online theo giời gian thực vào data lake.

# 2. Kiến trúc hệ thống
<img width="1636" height="654" alt="system-architecture" src="https://github.com/user-attachments/assets/1c377b32-0041-4599-af12-3f41d32c8d27" />


Hệ thống bao gồm các thành phần như sau:
* **Data Source**: Dữ liệu người dùng về game events (login, purchase,...) được tạo ngẫu nhiên.
* **Apache Airflow**: Điều phối và lập lịch thu thập dữ liệu từ nguồn.
* **Apache Kafka & Zookeeper**: Tiếp nhận, lưu trữ và quản lý luồng dữ liệu (event stream).
* **Kafka UI**: Giao diện giám sát và theo dõi hiệu suất của Kafka Broker.
* **Apache Spark**: Xử lý, làm sạch và chuẩn hóa dữ liệu từ Kafka.
* **MinIO**: Data Lake lưu trữ dữ liệu sau khi xử lý (Bronze, Silver, Gold).
* **PostgreSQL**: Lưu trữ metadata cho Airflow.

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
