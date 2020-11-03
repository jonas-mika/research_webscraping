# Manual: Twitter Scraper

## Description

The 'Twitter' Directory contains the Scipts used for scraping Twitter Data, the results from the srape and the quantitative analysis performed on it. 

## TODO

- [x] Change Script to run until all tweets from 2020 (or from start of lockdown are scraped)
- [ ] Add Requirements (Path and Installation of Driver from Selenium) in Manual Markdown
- [x] Format Output during Scraping
- [x] Make Chromedriver run in Background (maybe even as a class attribute)
- [ ] Add Docstrings
- [ ] Change save_data() method such that it needs to be saved after every iteration -> make it less viable to breaking of code through unexpected errors

## To Run
### Requirements
The script is written in Python, meaning that you need to have a Python installed on your machine. To avoid any complications, download the newest version from the [Python Website](https://www.python.org/downloads/) or within the most recent [Conda Distribution](https://www.anaconda.com/products/individual).

The Script uses a number of libraries, of which most come preinstalled with Python (ie. `os`, `json`, `time`, `random`, `csv`). However, the script is heavily based on the browser navigation functionality of `Selenium`, an external library to automate browsers ([Selenium](https://www.selenium.dev/)). If you don't already have this package installed, do so by running the following command line command:

In shell type:
`pip install selenium`

### Running the Scripts
1. Jupyter Notebook (you need to install the jupyter package in order to work with .ipynb files):  
In Shell Type:  
`jupyter notebook`  
to start a temporary server to access the jupyter notebooks on your local machine. 

In the automatically opened webbrowser, navigate to where the '.ipynb' file is located and open it. You should now be able to work with the Notebook.

2. Script:  
Navigate to the directory of 'twitter_scraper.py'. Make sure, that all `helpers.py`, `classes.py` and the configuration file `config.json` are located in the same directory. Open the configuration file and adjust the credentials, if you wish to (list of searchterms and twitter login data). Make sure that you have specified your path to the chrome webdriver. The Script won't run, if selenium can't access the Chrome webdriver.
If you have done the above steps, type:

`python twitter_scraper.py`

in yoyur shell to run the code. If you have all the necessary downloads, the code should work.

## Note!
Webscraping projects need high maintenance, since the script won't work, if changes are made to the structure of a website. If one of the scripts fails to work, please open an ssue or correct the code yourself and send a pull request. I will happily review your code and implement it, if I find it to be good.
