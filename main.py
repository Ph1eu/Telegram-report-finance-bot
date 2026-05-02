from search import search_news
from analysis import analyze_market
from telegram import send

def main():
    news = search_news()
    report = analyze_market(news)

    print(report)
    send(report)

if __name__ == "__main__":
    main()