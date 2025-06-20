# -*- coding: utf-8 -*-
"""amazon_reviews_nlp.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lUViXyo-Dvr6Jj87Fa5727EuSNOLHxhi
"""

!pip install spacy
!python -m spacy download en_core_web_sm

import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

reviews = [
    "I love the Apple iPhone 13! The camera quality is amazing.",
    "Samsung's Galaxy phone is overpriced and battery life is poor.",
    "The Bose headphones sound excellent and fit comfortably.",
    "Terrible experience with the Dell laptop, it keeps crashing.",
    "Great value for money with the Sony TV."
]

positive_words = {"love", "amazing", "great", "excellent", "good", "comfortable", "value"}
negative_words = {"overpriced", "bad", "poor", "terrible", "crashing"}

for i, review in enumerate(reviews, 1):
    doc = nlp(review)
    print(f"\nReview {i}: {review}")

    print("Entities:")
    for ent in doc.ents:
        print(f"  - {ent.text} ({ent.label_})")

    sentiment_score = 0
    for token in doc:
        if token.lemma_.lower() in positive_words:
            sentiment_score += 1
        elif token.lemma_.lower() in negative_words:
            sentiment_score -= 1

    sentiment = "Positive" if sentiment_score > 0 else "Negative" if sentiment_score < 0 else "Neutral"

    print(f"Sentiment: {sentiment}")