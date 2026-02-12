from confluent_kafka import Consumer
import os
import json
from consumer.app.mysql_connection import get_mysql_connection

kafka_bootstrap = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:29092")
kafka_topic = os.getenv("KAFKA_TOPIC", "customers_orders")

consumer_config = {
    "bootstrap.servers": kafka_bootstrap,
    "group.id": "customers-orders-service-group",
    "auto.offset.reset": "earliest"
}

consumer = Consumer(consumer_config)
consumer.subscribe([kafka_topic])

def listen_and_send_sql():

    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                print(f"Error: {msg.error()}")
                continue

            value = msg.value().decode("utf-8")
            data = json.loads(value)

            conn = get_mysql_connection()
            cursor = conn.cursor()

            if data["type"] == "customer":
                cursor.execute("""
                            INSERT INTO customers
                            (customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1,
                             addressLine2, city, state, postalCode, country, salesRepEmployeeNumber, creditLimit)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """, (data.get("customerNumber"), data.get("customerName"), data.get("contactLastName"),
                              data.get("contactFirstName"),data.get("phone"), data.get("addressLine1"), data.get("addressLine2"),
                              data.get("city"), data.get("state"), data.get("postalCode"), data.get("country"),
                              data.get("salesRepEmployeeNumber"), data.get("creditLimit")))

            elif data["type"] == "order":
                cursor.execute("""
                            INSERT INTO orders
                            (orderNumber, orderDate, title, requiredDate, shippedDate, status, comments, customerNumber)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                        """, (data.get("orderNumber"), data.get("orderDate"), data.get("title"),data.get("requiredDate"),
                              data.get("shippedDate"), data.get("status"), data.get("comments"),data.get("customerNumber")))

    except KeyboardInterrupt:
        print("\nStopping consumer")
    finally:
        consumer.close()