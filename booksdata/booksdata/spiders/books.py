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
        
        filename = f"books-{page}.html"
        bookdetails = {}
        # Save the content as file
        # Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")

        cards = response.css(".product_pod")
        ''' Print all the anchor tag from the website
        b = a.css("a")
        print(b) '''
        for card in cards: 
            title = card.css("h3>a::text").get()
            print(title) 

            rating = card.css(".star-rating").attrib["class"].split()[-1]
            print(rating)

            price = card.css(".product_price>.price_color::text").get()
            print(price)

            image = card.css(".image_container img")
            print(image.attrib["src"])

            stock = card.css(".availability")
            if len(stock.css(".icon-ok")) > 0:
                inStock = True
            else:
                inStock = False