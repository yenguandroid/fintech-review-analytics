# fintech-review-analytics
Scrape reviews from the Google Play Store, preprocess them into a clean, analysis-ready dataset
# Objective
 This project collects and preprocesses customer reviews from Ethiopian banking applications on Google Play Store for sentiment and review analytics.
 # Banks Included
 - Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank
# Methodology
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

Some applications may expose fewer public reviews depending on Google Play Store availability and API limitations.


