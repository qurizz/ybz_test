import feedparser

court_rss_feed = [
        'https://ecf.nysd.uscourts.gov/cgi-bin/rss_outside.pl'
]

def fetch_court_update():
    for url in court_rss_feed:
        feed = feedparser.parse(url)

        for entry in feed.entries:
            print(f"Case Title: {entry.title}")
            print(f'Published Date: {entry.Published}')
            print(f'Link: {entry.link}\n')

if __name__ == "__main__":
    fetch_court_update