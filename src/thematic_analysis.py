import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from nlp_pipeline import preprocess_text

# Load data
df = pd.read_csv("data/raw/sentiment_results.csv")

# Preprocess reviews
df["processed_review"] = df["review"].apply(preprocess_text)

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer(
    max_features=50,
    ngram_range=(1,2)
)

X = vectorizer.fit_transform(df["processed_review"])

keywords = vectorizer.get_feature_names_out()

print("Top Keywords:")
print(keywords)

# Authomatic Theme Assignment (Simple Keyword Matching)

def assign_theme(text):

    text = text.lower()

    if "login" in text or "password" in text:
        return "Account Access Issues"

    elif "transfer" in text or "payment" in text:
        return "Transaction Performance"

    elif "ui" in text or "interface" in text:
        return "UI & Design"

    elif "support" in text or "service" in text:
        return "Customer Support"

    else:
        return "Feature Requests"

df["identified_theme"] = df["review"].apply(assign_theme)

# Save final results
df.to_csv("data/raw/final_thematic_output.csv", index=False)

print(df.head())