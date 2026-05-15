# Preprocessing Script
import pandas as pd

# Load raw data
df = pd.read_csv("data/raw/raw_reviews.csv")

print("Initial Shape:", df.shape)

# Remove duplicates using review_id
df = df.drop_duplicates(subset=["review_id"])

# Missing values
missing_before = df.isnull().sum()

# Drop rows missing review or rating
df = df.dropna(subset=["review", "rating"])

missing_after = df.isnull().sum()

# Normalize date
df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

# Keep required columns only
df = df[["review", "rating", "date", "bank", "source"]]

print("Missing Before Cleaning:")
print(missing_before)

print("Missing After Cleaning:")
print(missing_after)

print("Final Shape:", df.shape)

# Save clean dataset
df.to_csv("data/raw/clean_reviews.csv", index=False)

print("Clean dataset saved successfully.")