#Scraping Script
from google_play_scraper import reviews, Sort
import pandas as pd

BANK_APPS = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp"
}

all_reviews = []

for bank, app_id in BANK_APPS.items():
    print(f"Scraping reviews for {bank}...")

    result, _ = reviews(
        app_id,
        lang='en',
        country='et',
        sort=Sort.NEWEST,
        count=500
    )

    for review in result:
        all_reviews.append({
            "review_id": review["reviewId"],
            "review": review["content"],
            "rating": review["score"],
            "date": review["at"],
            "bank": bank,
            "source": "Google Play"
        })

df = pd.DataFrame(all_reviews)

# Save raw dataset
df.to_csv("data/raw/raw_reviews.csv", index=False)

print(f"Total reviews collected: {len(df)}")