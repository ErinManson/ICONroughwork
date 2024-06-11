import feedparser
NewsFeed = feedparser.parse("file:///home/coop/search-feed%20.xml")
entry = NewsFeed.entries[1]

print('Number of RSS posts :', len(NewsFeed.entries))
print(entry.keys())
print("Title:")
for i in NewsFeed.entries:
    print(entry.title)