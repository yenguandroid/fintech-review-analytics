import pandas as pd
from sqlalchemy import text
from database import engine

# Load processed dataset
df = pd.read_csv("data/raw/final_thematic_output.csv")
#print(df.columns)
#print(df.head())

# Insert banks
banks = df["bank"].unique()

with engine.connect() as conn:

    for bank in banks:

        query = text("""
            INSERT INTO banks (bank_name, app_name)
            VALUES (:bank_name, :app_name)
            ON CONFLICT (bank_name) DO NOTHING
        """)

        conn.execute(
            query,
            {
                "bank_name": bank,
                "app_name": bank
            }
        )

    conn.commit()

# Retrieve bank IDs
bank_df = pd.read_sql("SELECT * FROM banks", engine)

bank_mapping = dict(
    zip(bank_df["bank_name"], bank_df["bank_id"])
)

# Prepare reviews table (correct mapping)
df["bank_id"] = df["bank"].map(bank_mapping)

df["review_text"] = df["review"]
df["review_date"] = df["date"]

review_df = df[[
    "bank_id",
    "review_text",
    "rating",
    "review_date",
    "sentiment_label",
    "sentiment_score",
    "identified_theme",
    "source"
]]

review_df["review_id"] = range(1, len(review_df) + 1)

review_df = review_df[[
    "review_id",
    "bank_id",
    "review_text",
    "rating",
    "review_date",
    "sentiment_label",
    "sentiment_score",
    "identified_theme",
    "source"
]]


# Insert into PostgreSQL
review_df.to_sql(
    "reviews",
    engine,
    if_exists="append",
    index=False
)

print("Data inserted successfully.")