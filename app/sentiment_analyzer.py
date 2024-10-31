from transformers import pipeline
sentiment_analyzer = pipeline('sentiment-analysis')

def analyze_sentiment(text):
    if text:  
        sentiment = sentiment_analyzer(text)
        return sentiment[0]
    return {"label": "neutral", "score": 0.0}