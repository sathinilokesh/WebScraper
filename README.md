# Amazon Web Scraping in Python

This repository contains a Python script for web scraping Amazon product data. The script uses the `requests` and `BeautifulSoup` libraries to extract information such as product title, price, and customer reviews from Amazon product pages.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [License](#license)

## Prerequisites

Before using this script, you need to have the following prerequisites installed:

- Python
- The `requests` library: You can install it using `pip`:
  ```
  pip install requests
  ```
- The `BeautifulSoup` library: You can install it using `pip`:
  ```
  pip install beautifulsoup4
  ```
- The `Pandas` library: You can install it using `pip`:
  ```
  pip install pandas
  ```

## Installation

1. Clone this repository to your local machine using `git`:

   ```
   git clone https://github.com/sathinilokesh/WebScraper.git
   ```

2. Navigate to the project directory:

   ```
   cd WebScraper
   ```

## Usage

To use the Amazon web scraping script, run the following command from your terminal:

```
python scrape_amazon.py <amazon_product_url>
```

Replace `<amazon_product_url>` with the URL of the Amazon product page you want to scrape.

The script will extract the following information from the product page:
- Product Link
- Product Title
- Product Price
- Rating
- Number of Reviews

The extracted data will be saved to a CSV file named `amazon_product_data.csv` in the project directory.

## Configuration

You can configure the script by editing the `scrape_amazon.py` file:

- `USER_AGENT`: You can set a custom User-Agent to mimic different web browsers.
- `HEADERS`: You can modify the headers sent with the HTTP request.
- `SAVE_TO_CSV`: You can change the filename for the CSV file where the data is saved.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
