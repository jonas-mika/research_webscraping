# imports
import json
from random import choice
from classes import TwitterScraper 
from timeit import default_timer as timer

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
    print('Initializing Twitter Scraper with given credentials...')
    twitter_scraper = TwitterScraper(un, pw, path)
    twitter_scraper.login()
    print(f'Logged in as:   {twitter_scraper.username}')
    print('-------------------')
    print('\nStarting to scrape...')

    for searchterm in searchterms:
        print(f'\nStarting to scrape [{searchterm}]')
        start = timer()
        twitter_scraper.scrape(searchterm)
        stop = timer()
        print(f'Finished Scraping every tweet up to 01/01/2020 in {round((stop-start)/60, 2)}min')
        print('-------------------')
    print(f'Scraped {len(twitter_scraper.get_data())} Searchterms')
    print(f'Saving data...')
    twitter_scraper.save_data()
    twitter_scraper.close_driver()
    print('DONE!')

main()