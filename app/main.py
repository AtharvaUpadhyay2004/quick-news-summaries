import streamlit as st
from data_fetcher import fetch_news
from summarizer import summarize_article
from sentiment_analyzer import analyze_sentiment

def add_background(image_url=None, color="#F5F5F5", opacity=0.5):
    if image_url:
        background_style = f"""
            <style>
            .stApp {{
                background: linear-gradient(rgba(0, 0, 0, {opacity}), rgba(0, 0, 0, {opacity})), 
                            url("{image_url}");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
            }}
            </style>
        """
    else:
        background_style = f"""
            <style>
            .stApp {{
                background-color: {color};
            }}
            </style>
        """
    st.markdown(background_style, unsafe_allow_html=True)

def main():
    # background with 50% opacity
    add_background(image_url="https://static.vecteezy.com/system/resources/previews/046/960/350/non_2x/vintage-newspaper-background-with-blank-space-for-creative-design-photo.jpg", opacity=0.5)

    # Title 
    st.markdown("""
        <h1 style="font-size: 2.5em; font-weight: bold; text-align: center; color: #FFF; 
                   text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.7); 
                   background-color: rgba(0, 0, 0, 0.4); padding: 10px; border-radius: 8px;">
            News Summarization and Analysis Tool
        </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
        <label style="color: #FFF; font-weight: bold;">Enter your NewsAPI key, if not then please get one from <a href='https://newsapi.org/' style='color: #FFD700;'>https://newsapi.org/</a>:</label>
    """, unsafe_allow_html=True)
    api_key = st.text_input("", "")

    st.markdown("""
        <label style="color: #FFF; font-weight: bold;">Enter a keyword to search for news:</label>
    """, unsafe_allow_html=True)
    query = st.text_input("", "latest news")

    if st.button("Fetch News"):
        if api_key:
            news_data = process_news(api_key, query)

            for news in news_data:
                st.markdown(f"""
                    <div style="background-color: rgba(0, 0, 0, 0.6); padding: 15px; border-radius: 8px; color: #FFF;">
                        <h2 style="color: #FFD700;">{news['title']}</h2>
                        <p><b>Summary:</b> {news['summary']}</p>
                        <p><b>Sentiment:</b> {news['sentiment']['label']} | Score: {news['sentiment']['score']}</p>
                        <p><a href="{news['url']}" style="color: #FFD700;">Read more</a></p>
                    </div>
                    <br>
                """, unsafe_allow_html=True)
        else:
            st.error("Please enter a valid API key.")

def process_news(api_key, query):
    articles = fetch_news(api_key, query)
    results = []

    for article in articles:
        title = article['title']
        content = article['content']

        summary = summarize_article(content)
        sentiment = analyze_sentiment(content)

        results.append({
            'title': title,
            'summary': summary,
            'sentiment': sentiment,
            'url': article['url'],
        })

    return results

if __name__ == "__main__":
    main()
