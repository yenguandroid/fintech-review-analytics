import psycopg2

conn = psycopg2.connect(
    dbname="bank_reviews",
    user="postgres",
    password="yengu123@",
    host="127.0.0.1",
    port="5432"
)

print("Connected successfully!")

conn.close()