# Website scraping and formating bot. 
# In presentation show how thats useful for a travel agency app we've been collaborating with, to scape sites that dont have api's
from dotenv import load_dotenv
import os
from firecrawl import FirecrawlApp

load_dotenv()
api_key = os.getenv('FIRECRAWL_API_KEY')

#outputs: API Key: fc-952f24c631a74e6ab02cdbb85a594464

# Initialize the FirecrawlApp with your API key
app = FirecrawlApp(api_key=api_key)
# Scrape a single URL
url = 'https://mendable.ai'
scraped_data = app.scrape_url(url)

print(scraped_data)
