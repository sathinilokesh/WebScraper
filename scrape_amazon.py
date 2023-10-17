import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

# Function to scrape product information from a page
def scrape_amazon_page(url):
    headers = {
        "User-Agent": "WebScraper/1.0 (Language=Python/3.11.4; Platform=Windows)"
    }
    product_info = []
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        products = soup.find_all("div", {"data-component-type": "s-search-result"})

        for product in products:
            product_url = product.find("a", class_="a-link-normal")
            product_name = product.find("span", class_="a-text-normal").text
            product_price = product.find("span", class_="a-price-whole")
            rating = product.find("span", class_="a-icon-alt")
            num_reviews = product.find("span", class_="a-size-base")

            product_data = {}  # Creating a dictionary to store product data

            if product_url:
                product_data["Product URL"] = "https://www.amazon.in" + product_url['href']
            if product_name:
                product_data["Product Name"] = product_name
            if product_price:
                product_data["Product Price"] = product_price.text
            if rating:
                product_data["Rating"] = rating.text
            if num_reviews:
                product_data["Number of Reviews"] = num_reviews.text

            if product_data:  # Check if product data is available
                product_info.append(product_data)

        return product_info

# Scrape multiple pages
product_urls = [
    "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1",
    # "https://www.amazon.in/s?k=mobiles&ref=nb_sb_noss_1"
    # "https://www.amazon.in/s?k=computers&ref=nb_sb_noss_1"
    # Add more URLs here
]

# Create a list of dictionaries to store the scraped data
data = []
for url in product_urls:
    for page_number in range(1, 21):  # Scraping 20 pages
        page_url = f"{url}&page={page_number}"
        print(f"Scraping Page {page_number}...")
        product_info = scrape_amazon_page(page_url)
        if product_info:
            data.extend(product_info)

# Create a Pandas DataFrame from the data
df = pd.DataFrame(data)

# Export the data to a CSV file
df.to_csv('amazon_product_data.csv', index=False)
