from sqlalchemy import create_engine
from sqlalchemy import text

DB_USER = "postgres"
DB_PASSWORD = "yengu123%40"
DB_HOST = "127.0.0.1"
DB_PORT = "5432"
DB_NAME = "bank_reviews"

DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    result = conn.execute(text("SELECT version();"))

    for row in result:
        print(row)

print("Connection successful!")