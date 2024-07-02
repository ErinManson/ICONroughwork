import requests

url = "https://canadabuys.canada.ca/en/search-feed?q=a%3A6%3A%7Bs%3A13%3A%22search_filter%22%3Ba%3A1%3A%7Bi%3A0%3Bs%3A0%3A%22%22%3B%7Ds%3A6%3A%22status%22%3Ba%3A1%3A%7Bi%3A0%3Bs%3A2%3A%2287%22%3B%7Ds%3A13%3A%22Apply_filters%22%3Ba%3A1%3A%7Bi%3A0%3Bs%3A13%3A%22Apply%20filters%22%3B%7Ds%3A15%3A%22record_per_page%22%3Ba%3A1%3A%7Bi%3A0%3Bs%3A2%3A%2250%22%3B%7Ds%3A11%3A%22current_tab%22%3Ba%3A1%3A%7Bi%3A0%3Bs%3A1%3A%22t%22%3B%7Ds%3A5%3A%22words%22%3Bs%3A12%3A%22rotary%20chair%22%3B%7D&sid=23222"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Success")
    print(response.content)
else:
    print(f"Failed to retrieve RSS feed. Status code: {response.status_code}")
