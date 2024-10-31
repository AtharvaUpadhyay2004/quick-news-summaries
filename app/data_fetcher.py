import requests

def fetch_news(api_key, query='latest news', page_size=5):
    url = f'https://newsapi.org/v2/everything?q={query}&pageSize={page_size}&apiKey={api_key}'
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Failed to fetch news articles")

    articles = response.json().get('articles', [])
    return articles
