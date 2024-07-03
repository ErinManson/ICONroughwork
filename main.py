import json
import sql

def separate_urls(input_list):
    postings = []
    for item in input_list:
        # Decode the JSON string to get the list of URLs
        urls = json.loads(item)
        postings.append(urls)
    return postings

# Input
input_data = sql.sql_main()
# Separate URLs
postings = separate_urls(input_data)

# Output the separated URLs
for post in postings:
    for url in post:
        print(url)
    print("\n")


#loop through posts

#loop through urls scanning each until we get a hit for a chair builder page in a text format for now