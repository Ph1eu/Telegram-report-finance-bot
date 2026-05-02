import feedparser

def search_news():
    query = "NHNN lãi suất liên ngân hàng OMO"
    url = f"https://news.google.com/rss/search?q={query}&hl=vi&gl=VN&ceid=VN:vi"

    feed = feedparser.parse(url)

    articles = []
    for entry in feed.entries[:5]:
        articles.append({
            "title": entry.title,
            "summary": entry.summary
        })

    return articles