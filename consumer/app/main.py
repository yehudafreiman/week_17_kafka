from consumer.app.kafka_consumer import listen_and_send_sql
from consumer.app.mysql_connection import get_mysql_connection, init_schema

if __name__ == "__main__":
    get_mysql_connection()
    init_schema()
    listen_and_send_sql()



