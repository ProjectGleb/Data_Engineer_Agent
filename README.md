# Data_Engineer_Agent
AI data engineer automating the ETL process.
This agent crew takes in a query + URL, scrapes the website/websites, cleans & structures the data, and populates your documents/database with the correct scraped data.

Demo: https://drive.google.com/file/d/12km0Efs2Z8g7aaBlYi_6iq7IUlomP8V_/view?usp=sharing

## AGENTS:
1. Scraper/Crawler + Data Processor: Extracts, cleans, and processes website content.
2. Writer: Reads the dataset/document to familiarise with its structure, cleans the data and appends it to the dataset/document (e.g., PDFs, CSV, websites).
4. Reviewer: Ensures data entry accuracy.

## TOOLS:
1. Scraper/Crawler:
   - Firecrawl tool
2. Writer:
   - Directory reading tool
   - Document Reading tool
   - Document Creation tool
   - (Would be good to add a schema tool to constrain the agent.)
3. Reviewer
   - Directory reading tool
   - Document Reading tool
