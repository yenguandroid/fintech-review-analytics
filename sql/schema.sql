CREATE TABLE IF NOT EXISTS banks (
    id SERIAL PRIMARY KEY,
    bank_name VARCHAR(100) UNIQUE NOT NULL,
    app_name VARCHAR(100)
);

DROP TABLE IF EXISTS reviews;

CREATE TABLE reviews (
    review_id TEXT PRIMARY KEY,
    bank_id INTEGER REFERENCES banks(bank_id),
    review_text TEXT NOT NULL,
    rating INTEGER,
    review_date DATE,
    sentiment_label TEXT,
    sentiment_score FLOAT,
    identified_theme TEXT,
    source TEXT
);