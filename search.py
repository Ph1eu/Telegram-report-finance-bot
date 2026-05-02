import feedparser
from urllib.parse import urlencode

def search_news():
    query = "NHNN lãi suất liên ngân hàng OMO"
    params = {"q": query, "hl": "vi", "gl": "VN", "ceid": "VN:vi"}
    url = "https://news.google.com/rss/search?" + urlencode(params)

    feed = feedparser.parse(url)

    articles = []
    for entry in feed.entries[:5]:
        articles.append({
            "title": entry.title,
            "summary": entry.summary
        })

    return articles