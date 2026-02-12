import asyncio
from mongo_connection import collection
from kafka_publisher import create_batches_and_send_to_kafka


async def read_mongodb_and_send_to_kafka_in_background():
    try:
        cursor = collection.find()
        asyncio.create_task(create_batches_and_send_to_kafka(cursor))
        return {
            "status": "started",
            "message": "seeding successfully"
        }
    except Exception as e:
        raise f"Unexpected error: {str(e)}"