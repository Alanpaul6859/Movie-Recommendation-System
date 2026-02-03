from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def content_similarity(text_data):
    tfidf = TfidfVectorizer(stop_words='english')
    matrix = tfidf.fit_transform(text_data)
    return cosine_similarity(matrix)
