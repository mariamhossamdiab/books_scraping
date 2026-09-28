# books_scraping
## What broke, or took longer than you expected?

The web scraping and data cleaning took longer than expected because some fields required additional processing and validation. I also had to make sure that the scraped values, especially price, rating, and stock status, were correctly extracted and converted into appropriate data types before loading them into SQL. I  also handled if the table in data base was created just append data to it and remove duplicates , Debugging and validating the scraped data was the main part that took extra time.


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

<img width="1486" height="822" alt="image" src="https://github.com/user-attachments/assets/49433648-30d1-4256-b94b-46b55fedde23" />
<img width="873" height="536" alt="image" src="https://github.com/user-attachments/assets/623d440b-e06a-4247-82d7-2dd206b1d2ab" />


<img width="1535" height="817" alt="image" src="https://github.com/user-attachments/assets/5ac13c30-f1c0-4aad-ae0a-da5280799447" />
<img width="1373" height="703" alt="image" src="https://github.com/user-attachments/assets/3e3052e9-7def-44df-acfa-54f53687477f" />


   
