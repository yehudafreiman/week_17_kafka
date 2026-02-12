import asyncio
import json
from confluent_kafka import Producer
import os


KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:29092")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "customers_orders.registered")
producer = Producer({"bootstrap.servers": KAFKA_BOOTSTRAP_SERVERS})


async def create_batches_and_send_to_kafka(customers_orders: list):
    try:
        batch_size = 50
        for i in range(0, len(customers_orders), batch_size):
            batch = customers_orders[i:i + batch_size]
            for doc in batch:
                value = json.dumps(doc).encode("utf-8")
                producer.produce(
                    topic=KAFKA_TOPIC,
                    value=value,
                    callback=lambda err, msg: print(
                        f"Sent" if err is None else f"Failed: {err}"
                    )
                )
                producer.flush()
                if i + batch_size < len(customers_orders):
                    await asyncio.sleep(0.5)
    except Exception as e:
        raise f"Unexpected error: {str(e)}"