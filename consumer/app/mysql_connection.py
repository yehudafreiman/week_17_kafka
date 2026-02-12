import os
import mysql.connector


mysql_config = {
    "host": os.getenv("MYSQL_HOST", "mysql"),
    "port": int(os.getenv("MYSQL_PORT", "3306")),
    "database": os.getenv("MYSQL_DATABASE", "db"),
    "user": os.getenv("MYSQL_USER", "user"),
    "password": os.getenv("MYSQL_PASSWORD", "pass")
}


def get_mysql_connection():
    return mysql.connector.connect(**mysql_config)


def init_schema():
    conn = get_mysql_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            customerNumber INT PRIMARY KEY,
            customerName VARCHAR(255),
            contactLastName VARCHAR(255),
            contactFirstName VARCHAR(255),
            phone VARCHAR(255),
            addressLine1 VARCHAR(255),
            addressLine2 VARCHAR(255),
            city VARCHAR(255),
            state VARCHAR(255),
            postalCode VARCHAR(255),
            country VARCHAR(255),
            salesRepEmployeeNumber INT,
            creditLimit VARCHAR(255)
        )
    """)
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                orderNumber INT PRIMARY KEY,
                orderDate VARCHAR(255),
                title VARCHAR(255),
                requiredDate VARCHAR(255),
                shippedDate VARCHAR(255),
                status VARCHAR(255),
                comments VARCHAR(255),
                customerNumber INT,
                FOREIGN KEY (customerNumber) REFERENCES customers(customerNumber) ON DELETE CASCADE
            )
        """)
    conn.commit()
    cursor.close()
    conn.close()
    print("MySQL schema initialized")

