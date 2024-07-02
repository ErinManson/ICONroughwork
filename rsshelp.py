from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/rss-proxy')
def rss_proxy():
    url = "https://canadabuys.canada.ca/en/search-feed?q=a%3A6%3A%7Bs%3A13%3A%22search_filter%22%3Ba%3A1%3A%7Bi%3A0%3Bs%3A0%3A%22%22%3B%7Ds%3A6%3A%22status%22%3Ba%3A1%3A%7Bi%3A0%3Bs%3A2%3A%2287%22%3B%7Ds%3A13%3A%22Apply_filters%22%3Ba%3A1%3A%7Bi%3A0%3Bs%3A13%3A%22Apply%20filters%22%3B%7Ds%3A15%3A%22record_per_page%22%3Ba%3A1%3A%7Bi%3A0%3Bs%3A2%3A%2250%22%3B%7Ds%3A11%3A%22current_tab%22%3Ba%3A1%3A%7Bi%3A0%3Bs%3A1%3A%22t%22%3B%7Ds%3A5%3A%22words%22%3Bs%3A12%3A%22rotary%20chair%22%3B%7D&sid=23222"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    return Response(response.content, status=response.status_code, content_type=response.headers['Content-Type'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    #comment