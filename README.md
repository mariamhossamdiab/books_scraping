# books_scraping
## What broke, or took longer than you expected?

The web scraping and data cleaning took longer than expected because some fields required additional processing and validation. I also had to make sure that the scraped values, especially price, rating, and stock status, were correctly extracted and converted into appropriate data types before loading them into SQL. Debugging and validating the scraped data was the main part that took extra time.


## If the site started blocking you after 50 requests, what would
you change?
1. Add a delay between requests, (e.g. 1-3 seconds)

2. If I get a 429 Too Many Requests or 503, wait and retry with exponential backoff, and honor the Retry-After header if the server sends one.

3. Check robots.txt and the terms of service. Look for a Crawl-delay or disallowed paths, and confirm scraping is permitted at all.

4. Look for an official API or data export. This is usually the best fix. APIs come with documented rate limits, and some sites offer bulk downloads or feeds that replace thousands of page requests.

5. Cache responses locally so I never fetch the same page twice.
Use conditional requests (If-Modified-Since / ETag) so unchanged pages cost almost nothing.
Fetch only the pages I actually need.

6. Make the job resumable. Save progress in batches (e.g. 40 requests, then pause), so a block or crash doesn't force me to start over.
   
7. change driver .
## How to run code : 
1. create vm by this command : python -m venv .venv

2. to active it : .venv\Scripts\Activate.ps1
3. to install requirements : python -m pip install -r requirements.txt
4. to run scrap code : python book.py
5. to load csv file too ssms by python : python loading_to_ssms.py

   
