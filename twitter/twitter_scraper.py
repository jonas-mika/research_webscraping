# imports
import json
from random import choice
from classes import TwitterScraper 


# load configurations
with open('config.json', 'r') as f:
    CONFIG = json.load(f)

# load the configuartions into more readable global variables
path = CONFIG['PATH']
searchterms = CONFIG['SEARCHES']
un = choice(CONFIG['CREDENTIALS']['USER'])
pw = CONFIG['CREDENTIALS']['PASSWORD']

# executed script
def main():
    twitter_scraper = TwitterScraper(un, pw, path)
    twitter_scraper.login()
    print(twitter_scraper.username)
    print(twitter_scraper.get_data())

    for searchterm in searchterms:
        twitter_scraper.scrape(searchterm)
        print(f'Finished Scraping for {searchterm}')      
    print(len(twitter_scraper.get_data()))
    twitter_scraper.save_data()
    twitter_scraper.close_driver()

main()