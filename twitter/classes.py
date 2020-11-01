# imports 
from time import sleep, time

# selenium library to navigate browser and scrape twitter
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
# we use the chrome browser for the twitter webscraping
from selenium.webdriver import Chrome

import os # used to automatically create directories to store the 
import csv  # used to ouput the data into a csv file (that we can analyze)
from helpers import *

# twitter scraper class
class TwitterScraper:


    def __init__(self, username, password, path):
        self.username = username
        self.password = password
        self.path = path
        self.driver = Chrome(self.path)
        self.data = {}

    def __str__(self):
        return f'TwitteeScraper object of user: "{self.username}"'

    def __repr(self):
        return f'<twitter scraper object: ({self.username}))>' # add getpassword 

    def get_driver(self):
        """
        Returns the Driver used for the Scraping
        """
        return self.driver

    def set_driver(self, driver):
        if driver == 'chrome':
            self.driver = Chrome(self.path)
        elif driver == "edge":
            print('Sorry, this feature hasnt yet been implemented.')
        elif driver == "firefox":
            print('Sorry, this feature hasnt yet been implemented.')
        else:
            print('Sorry, I dont know this browser.')

    def get_data(self):
        if self.data == {}:
            return "There hasn't been any data scraped so far"
        else: return self.data

    def login(self):
        # navigate to twitter login page using 'get' module
        self.driver.get('https://twitter.com/login/')
        sleep(2)

        # enter the username and password
        username = self.driver.find_element_by_xpath(
            '//input[@name="session[username_or_email]"]')
        username.send_keys(self.username)
        password = self.driver.find_element_by_xpath(
            '//input[@name="session[password]"]')  # enter the password
        password.send_keys(self.password)
        # login using the login button (similar action than to just press enter)
        password.send_keys(Keys.RETURN)
        sleep(2)

    def scrape(self, searchterm):
        # enter the searchterm
        search_input = self.driver.find_element_by_xpath(
            '//input[@aria-label="Search query"]')
        
        try: search_input.clear()
        except: None
        
        search_input.send_keys(searchterm)
        search_input.send_keys(Keys.RETURN)
        sleep(2)

        self.driver.find_element_by_link_text('Latest').click()
        sleep(1)

        # get all tweets on the page
        self.data[searchterm] = []
        tweet_ids = set() # we use this to make sure that our dataset consist of unique tweets

        timeout = time() + 10

        while True:
            page_cards = self.driver.find_elements_by_xpath('//div[@data-testid="tweet"]')
            for card in page_cards[-15:]:
                tweet = get_tweet_data(card)
                if tweet:
                    tweet_id = ''.join(tweet)
                    if tweet_id not in tweet_ids:
                        tweet_ids.add(tweet_id)
                        self.data[searchterm].append(tweet)
                    
            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            sleep(3)

            if time() > timeout:
                print('The Scrape ended after 10 seconds')
                break
    
    def save_data(self):
        try:
            os.mkdir('scrape_results')
        except: None

        for search in self.data:
            with open(f"scrape_results/scraped_{search}.csv", 'w', newline='', encoding='utf-8') as outfile:
                header = ['Username', 'Twitter-Handle', 'Timestamp', 'Text', 'No. of Comments', 'No. of Likes', 'No. of Retweets']
                writer = csv.writer(outfile)
                writer.writerow(header)
                writer.writerows(self.data[search]) 
            print(f'Sucessfully saved "./scrape_results/scraped_{search}"')

    def close_driver(self):
        self.driver.close()
