import psycopg2
from . import config



# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host=config.host,
    database=config.database,
    user=config.user,
    password=config.password
)

# Create a table to store user information (execute this once)
with conn.cursor() as cursor:
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            nickname VARCHAR(255) UNIQUE,
            password VARCHAR(255)
        );
        """
    )
    conn.commit()
