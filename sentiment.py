from textblob import TextBlob

def analyze_sentiment(review):
    return TextBlob(review).sentiment.polarity
