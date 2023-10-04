Reference: https://blog.apify.com/how-to-use-langchain/#load-and-process-data-with-langchain-and-pinecone

pip install -r requirements.txt

Start from main: python main.py

Please create an .env file and insert your openai api key:
OPENAI_API_KEY=**USE YOUR KEY**
APIFY_API_TOKEN=**USE YOUR KEY**

The general idea is that we find on Apify store a SCRAPER and we run it
Once it runs we get a datasetid that we can "import" in our code and "query" it

Some useful scrapers:

- streamers/youtube-scraper
- apify/website-content-crawler

- static web pages: apify/beautifulsoup-scraper / apify/cheerio-scraper
- dynamic web pages: apify/playwright-scraper

the example i made was the creation of a youtube scraper that scrapes from my channel: https://www.youtube.com/@schOOlsin/videos
