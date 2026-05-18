# Sentiment Analysis Using DistilBERT

from transformers import pipeline

# Load transformer sentiment model
classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def predict_sentiment(review):

    try:
        result = classifier(str(review))[0]

        label = result["label"]
        score = result["score"]

        if label == "POSITIVE":
            sentiment = "positive"
        else:
            sentiment = "negative"

        return sentiment, score

    except:
        return "neutral", 0.5