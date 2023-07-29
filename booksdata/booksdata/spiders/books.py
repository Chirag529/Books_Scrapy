import scrapy
from pathlib import Path
import csv
import pandas as pd

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["toscrape.com"]
    start_urls = ["https://toscrape.com"]
    
    def start_requests(self):
        # Define the initial URLs to be scraped.
        urls = [
            "https://books.toscrape.com/catalogue/category/books/travel_2/index.html",
            "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
        ]

        for url in urls:
            # For each URL in the 'urls' list, yield a scrapy.
            yield scrapy.Request(url=url, callback=self.parse)

    # Default callback function to handle the response for each request.
    def parse(self, response):
        # Extract the last part of the URL and use it as part of the filename to save the scraped data.
        page = response.url.split("/")[-2]
        
        # Create the filename to save the scraped data. 
        filename = f"books-%s.html" % page

        # Create a list to store the scraped data.
        bookdetails = []

        # Extract the list of books from the response body.
        cards = response.css(".product_pod")
        for card in cards:
            title = card.css("h3 a::text").get()
            price = card.css(".price_color::text").get()
            instock = card.css(".instock availability::text").get() 
        
            print(title)
            print(price)
            print(instock)
        
            # Save the extracted data to the list as a dictionary.
            bookdetails.append({
                "title": title,
                "price": price,
                "instock": instock
            })

        # Log a message indicating that the file has been saved
        self.log('Saved file %s' % filename)

        # Save the data into a CSV using a DataFrame and pandas
        df = pd.DataFrame(bookdetails)
        df.to_csv("books.csv", index=False)
