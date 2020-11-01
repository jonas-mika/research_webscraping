# imports 
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
# we use the chrome browser for the twitter webscraping
from selenium.webdriver import Chrome


# helper functions 
def get_tweet_data(card):
    """
    Extract data from tweet card using xpath searches for each important element of the tweet
    """

    username = card.find_element_by_xpath('.//span').text
    try:  # since advertised post dont have a handle and a postdate, we can easily filter them out using error handling
        handle = card.find_element_by_xpath(
            './/span[contains(text(), "@")]').text
    except NoSuchElementException:
        return

    try:
        postdate = card.find_element_by_xpath(
            './/time').get_attribute('datetime')
    except NoSuchElementException:
        return

    comment = card.find_element_by_xpath('.//div[2]/div[2]/div[1]').text
    responding = card.find_element_by_xpath('.//div[2]/div[2]/div[2]').text
    text = comment + responding
    reply_cnt = card.find_element_by_xpath('.//div[@data-testid="reply"]').text
    retweet_cnt = card.find_element_by_xpath(
        './/div[@data-testid="retweet"]').text
    like_cnt = card.find_element_by_xpath('.//div[@data-testid="like"]').text

    # concatenate all the scraped data into a tuple return it
    tweet = (username, handle, postdate, text,
             reply_cnt, retweet_cnt, like_cnt)

    return tweet