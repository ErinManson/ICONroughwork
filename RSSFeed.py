
# url = 'https://canadabuys.canada.ca/en/search-feed?q=a%3A3%3A%7Bs%3A11%3A%22current_tab%22%3Ba%3A1%3A%7Bi%3A0%3Bs%3A1%3A%22t%22%3B%7Ds%3A15%3A%22record_per_page%22%3Ba%3A1%3A%7Bi%3A0%3Bs%3A3%3A%22200%22%3B%7Ds%3A5%3A%22words%22%3Bs%3A8%3A%2256101700%22%3B%7D&sid=22760'
# response = requests.get(url)
# feed = feedparser.parse(response.content)

# entry = feed.entries[1]
# print(entry.keys)

import re
import feedparser
import requests

def clean_xml_content(content):
    # Remove invalid XML characters
    content = re.sub(r'[^\x09\x0A\x0D\x20-\x7F]', '', content)
    return content

url = 'https://canadabuys.canada.ca/en/search-feed?q=a%3A5%3A%7Bs%3A13%3A%22search_filter%22%3Ba%3A1%3A%7Bi%3A0%3Bs%3A0%3A%22%22%3B%7Ds%3A13%3A%22Apply_filters%22%3Ba%3A1%3A%7Bi%3A0%3Bs%3A13%3A%22Apply%20filters%22%3B%7Ds%3A15%3A%22record_per_page%22%3Ba%3A1%3A%7Bi%3A0%3Bs%3A2%3A%2250%22%3B%7Ds%3A11%3A%22current_tab%22%3Ba%3A1%3A%7Bi%3A0%3Bs%3A1%3A%22t%22%3B%7Ds%3A5%3A%22words%22%3Bs%3A8%3A%2256101700%22%3B%7D&sid=22762'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Check if the request was successful

    raw_content = response.content.decode('utf-8', errors='replace')
    
    # Save the raw content to a file for external inspection
    with open('raw_feed.xml', 'w', encoding='utf-8') as file:
        file.write(raw_content)
    
    print("Raw Content:\n", raw_content[:1000])  # Print the first 1000 characters of the raw XML content

    cleaned_content = clean_xml_content(raw_content)
    print("Cleaned Content:\n", cleaned_content[:1000])  # Print the first 1000 characters of the cleaned XML content

    feed = feedparser.parse(cleaned_content)
    if feed.bozo:
        print("Failed to parse feed: ", feed.bozo_exception)
    else:
        print(f"Feed title: {feed.feed.title}")
        if feed.entries:
            for i, entry in enumerate(feed.entries):
                print(f"Entry {i} title: {entry.title}")
            entry = feed.entries[1] if len(feed.entries) > 1 else feed.entries[0]
            print(entry.keys())
        else:
            print("The feed contains no entries.")
except requests.RequestException as e:
    print(f"An error occurred: {e}")
except UnicodeDecodeError as e:
    print(f"Failed to decode response content: {e}")
