# fintech-review-analytics
Scrape reviews from the Google Play Store, preprocess them into a clean, analysis-ready dataset
# Objective
 This project collects and preprocesses customer reviews from Ethiopian banking applications on Google Play Store for sentiment and review analytics.
 # Banks Included
 - Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank
# Methodology
# Task 1: Data Collection and Preprocessing
## Data Collection

Reviews were scraped using the google-play-scraper Python library.

Fields collected:
- Review text
- Rating
- Review date
- Bank name
- Source

Minimum target:
- 400+ reviews per bank
- 1,200+ total reviews
# Preprocessing
## Data Cleaning

- Removed duplicate reviews
- Dropped missing review text and ratings
- Standardized dates to YYYY-MM-DD
- Exported clean CSV dataset
# Limitations
## Limitations

Some applications may expose fewer public reviews depending on Google Play Store availability and API limitations.p
# Task 2: Sentiment and Thematic Analysis
# Objective 
Quantify review sentiment and identify recurring themes to uncover satisfaction drivers and pain points for each bank.
this objective achieved by:
Download spaCy Language Model and Build NLP Pipeline that satsfies
-Tokenization
-Stop-word removal
-Lemmatization
-Modular reusable pipeline
# Sentiment Analysis Using DistilBERT
# Why DistilBERT Is Better
DistilBERT was selected because transformer-based models better understand contextual sentiment in financial/mobile banking reviews compared to lexicon-based approaches like VADER.
-Thematic Analysis
-Aggregation Analysis
## Key Business Insights
Key Insights

## CBE
- Frequent complaints related to login and transfer failures
- High number of negative reviews connected to server downtime

## BOA
- Better UI satisfaction compared to competitors
- Positive feedback regarding ease of use

## Dashen
- Users request additional features and faster transactions

## General Findings
- Transaction delays are a major pain point across all banks
- Positive sentiment is strongly associated with UI simplicity

# Task 3: Data Storage, Sentiment Insights & PostgreSQL Integration
## Overview

This task focused on building a complete data storage and analytics pipeline for bank app reviews. The goal was to transform processed sentiment data into a structured relational database and enable analytical querying using PostgreSQL.

The pipeline connects:

- Cleaned review dataset (CSV)
- Sentiment analysis outputs
- Thematic classification results
- PostgreSQL database (banks + reviews tables)
### Database Design

A relational database was implemented with two main tables:
- Stores bank metadata.
1. banks Table (Dimension Table)
| Column    | Type               | Description             |
| --------- | ------------------ | ----------------------- |
| bank_id   | SERIAL PRIMARY KEY | Unique identifier       |
| bank_name | TEXT               | Name of the bank        |
| app_name  | TEXT               | Mobile application name |
2. reviews Table (Fact Table)

Stores user reviews and analysis results.
| Column           | Type               | Description                     |
| ---------------- | ------------------ | ------------------------------- |
| review_id        | SERIAL PRIMARY KEY | Auto-generated ID               |
| bank_id          | INTEGER            | Foreign key → banks             |
| review_text      | TEXT               | Original review                 |
| rating           | INTEGER            | User rating (1–5)               |
| review_date      | DATE               | Date of review                  |
| sentiment_label  | VARCHAR(20)        | Positive / Negative             |
| sentiment_score  | FLOAT              | Model confidence score          |
| identified_theme | VARCHAR(100)       | Extracted theme                 |
| source           | VARCHAR(50)        | Data source (e.g., Google Play) |
# vData Pipeline Workflow
## Step 1: Load Cleaned Dataset
- Input CSV: final_thematic_output.csv
- Loaded using Pandas
## Step 2: Insert Bank Records
- Extract unique banks
- Insert into banks table
- Avoid duplicates using ON CONFLICT DO NOTHING
## Step 3: Map Bank IDs
- Retrieved bank_id from PostgreSQL
- Mapped to dataset for relational consistency
## Step 4: Insert Reviews
- Selected required columns:
- review_text
- rating
- review_date
- sentiment_label
- sentiment_score
- identified_theme
- source
- bank_id
Inserted into PostgreSQL using pandas.to_sql()
# Key Insights from Database
1. Sentiment Distribution
SELECT sentiment_label, COUNT(*)
FROM reviews
GROUP BY sentiment_label;

Results:

Positive: 918
Negative: 582

-- Reviews per Bank
SELECT b.bank_name, COUNT(r.review_id)
FROM reviews r
JOIN banks b ON r.bank_id = b.bank_id
GROUP BY b.bank_name;

Results:

CBE → 500 reviews
Dashen → 500 reviews
BOA → 500 reviews

#  Key Achievements
- Built a relational PostgreSQL database from scratch
- Successfully fixed schema design issues
- Implemented foreign key relationships
- Automated data insertion using Python + SQLAlchemy
- Performed structured sentiment aggregation
- Enabled SQL-based analytics ready for dashboards
#  Technologies Used
- Python (Pandas, SQLAlchemy)
- PostgreSQL 16
- psycopg2
- CSV data pipeline
- Sentiment analysis outputs
# Outcome

A fully functional end-to-end data pipeline that transforms raw bank app reviews into structured, queryable business insights stored in PostgreSQL.