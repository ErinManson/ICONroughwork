import feedparser
NewsFeed = feedparser.parse("file:///home/coop/search-feed%20.xml")
entry = NewsFeed.entries[1]

print(entry.keys())