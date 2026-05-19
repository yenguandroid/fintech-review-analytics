# Thematic Analysis Using TF-IDF

from sklearn.feature_extraction.text import TfidfVectorizer

# Create vectorizer
vectorizer = TfidfVectorizer(
    max_features=50,
    ngram_range=(1, 2)
)

def extract_keywords(text_data):

    X = vectorizer.fit_transform(text_data)

    keywords = vectorizer.get_feature_names_out()

    return keywords.tolist()


def assign_theme(review):

    review = str(review).lower()

    if any(word in review for word in ["loan", "credit", "borrow"]):
        return "Loan Services"

    elif any(word in review for word in ["transfer", "transaction", "payment"]):
        return "Money Transfer"

    elif any(word in review for word in ["app", "bug", "crash", "error"]):
        return "App Performance"

    elif any(word in review for word in ["support", "service", "help"]):
        return "Customer Support"

    else:
        return "Other"