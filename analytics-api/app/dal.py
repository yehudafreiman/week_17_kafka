from connection import get_mysql_connection

conn = get_mysql_connection()
cursor = conn.cursor()

def get_top_customers():
    result = cursor.execute("""
    SELECT * FROM customers
    FROM customers c
    LEFT JOIN orders o ON c.customerNumber = o.customerNumber
    """)
    return result

def get_customers_without_orders():
    result = cursor.execute("""
    SELECT * FROM customers
    FROM customers c
    LEFT JOIN orders o ON c.customerNumber = o.customerNumber
    """)
    return result

def get_zero_credit_active_customers():
    result = cursor.execute("""
    SELECT * FROM customers
    FROM customers c
    LEFT JOIN orders o ON c.customerNumber = o.customerNumber
    """)
    return result



