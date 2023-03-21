import requests
from bs4 import BeautifulSoup
import re

# Send a request to the search page and parse the HTML response
search_url = "https://www.trendyol.com/sr?q=hello+kitty&pi=1"
search_response = requests.get(search_url)
search_soup = BeautifulSoup(search_response.content, 'html.parser')

# Extract the total number of search results and calculate the total number of pages
dscrptn_div = search_soup.find('div', {'class': 'dscrptn'})
dscrptn_text = dscrptn_div.get_text(strip=True)
total_results = int(re.search(r'(\d+) sonuç listeleniyor', dscrptn_text).group(1))
num_pages = (total_results) // 24

# Loop through each page and scrape the data
for page_number in range(1, num_pages+1):
    url = f"https://www.trendyol.com/sr?q=hello+kitty&pi={page_number}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    products = soup.find_all('div', {'class': 'prdct-cntnr-wrppr'})

    for product in products:
        name = product.find('span', {'class': 'prdct-desc-cntnr-name'}).text
        price = product.find('div', {'class': 'prc-box-dscntd'}).text
        print(name, price)