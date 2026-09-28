from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
import pandas as pd
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

all_books = []
service = Service(r"E:\Users\ALNOUR-320\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
x = webdriver.Chrome(service=service)
#x.get("https://books.toscrape.com/")
time.sleep(5)
def page_scrape(url, retries=3):
    for attempt in range(1, retries + 1):
        try:
            x.get(url)
            time.sleep(2)
            break
        except WebDriverException as e:
            print(f"  Attempt {attempt} failed for {url}: {e.msg[:80]}")
            if attempt == retries:
                return False
            time.sleep(2 ** attempt)  # exponential backoff
    try:
        title= x.find_elements(By.XPATH, '//h3/a')
        price = x.find_elements(By.XPATH, "//div/p[1]") # or  "//div[@class='product_price']/p[@class='price_color']""
        in_stock = x.find_elements(By.XPATH, "//div/p[2]") 
        rate = x.find_elements(By.XPATH, "//article/p") 

        titles = [elem.text.strip() for elem in title]
        prices = [float(elem.text.strip().replace("£", "")) for elem in price]
        in_stock = [elem.text.strip() == "In stock" for elem in in_stock]
        urls = [elem.get_attribute("href") for elem in title]

        word_to_number = {
            "One": 1,
            "Two": 2,
            "Three": 3,
            "Four": 4,
            "Five": 5
        }

        rates = [
            word_to_number.get(
                elem.get_attribute("class").replace("star-rating", "").strip()
            )
            for elem in rate
        ]


        
        for title, price, rating, in_stock, url in zip(titles, prices, rates ,in_stock, urls):
            all_books.append({
                "title": title,
                "price": price,
                "rating": rating,
                "in_stock": in_stock,
                "url": url,
                
            })    
    except (ValueError, WebDriverException) as e:
            print(f"  Skipping book: {e}")  # log it, don't hide it
   

num_of_scraped_pages=5 # num of pages you want to scrape
try:
    for i in range(0,num_of_scraped_pages):
        print('Scraping page', i+1)  
        page_scrape(f"https://books.toscrape.com/catalogue/page-{i+1}.html")  
        if(i!=(num_of_scraped_pages-1)):                 
            next_button = x.find_element(By.XPATH, "//a[text()='next']") # to navigate to next page 
            next_button.click()
finally:
    x.quit()  # Close the browser after scraping           
    df = pd.DataFrame(all_books)       
    df.to_csv("books.csv", index=False)