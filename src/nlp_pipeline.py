# Build NLP Pipeline
import spacy
import re

nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    text = str(text).lower()

    # Remove URLs
    text = re.sub(r"http\S+", "", text)

    # Remove special characters
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    return text

def preprocess_text(text):
    text = clean_text(text)

    doc = nlp(text)

    tokens = [
        token.lemma_
        for token in doc
        if not token.is_stop
        and not token.is_punct
        and len(token.text) > 2
    ]

    return " ".join(tokens)