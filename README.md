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


