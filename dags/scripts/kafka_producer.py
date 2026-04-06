def stream_kafka():
    from kafka import KafkaProducer
    import json, time, logging
    from scripts.data_generator import generate_event

    producer = KafkaProducer(
        bootstrap_servers=[
            'kafka:29092',
        ],
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    start_time = time.time()

    while time.time() - start_time < 300:
        try:
            event = generate_event()

            producer.send(
                "streaming-data",
                key=str(event["user_id"]).encode("utf-8"),
                value=event
            )

            logging.info(f"Sent event: {event}")

        except Exception as e:
            logging.error(f"Error: {e}")

        time.sleep(1)

    producer.flush()