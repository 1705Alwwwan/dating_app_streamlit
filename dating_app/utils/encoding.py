from sklearn.feature_extraction.text import CountVectorizer

def encode_interests(interests):
    vectorizer = CountVectorizer()
    encoded = vectorizer.fit_transform(interests)
    return encoded.toarray(), vectorizer
