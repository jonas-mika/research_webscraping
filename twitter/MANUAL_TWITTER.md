# Manual: Twitter Scraper

## Description

The 'Twitter' Directory contains the Scipts used for scraping Twitter Data, the results from the srape and the quantitative analysis performed on it. 

## TODO

- [ ] Further implement Classes in Python Script
- [ ] Separate the twitter_scraper.py to make it more readable (maybe create a separate folder containing all those files)
- [ ] Add Requirements (Path and Installation of Driver from Selenium) in Manual Markdown

## To Run
### Libraries needed
For the scripts to work you need some libraries. Most of them come pre-installed with python. The selenium library, which is primarily used for navigating the browser and scraping, needs to be installed, if it is not already:  

In shell type:
`pip install selenium`

### Running the Scripts
1. Jupyter Notebook (you need to install the jupyter package in order to work with .ipynb files):  
In Shell Type:  
`jupyter notebook`  
to start a temporary server to access the jupyter notebooks on your local machine. 

In the automatically opened webbrowser, navigate to where the '.ipynb' file is located and open it. You should now be able to work with the Notebook.

2. Script:  
Navigate to the directory your '.py' is located and type:  
`python twitter_scraper.py` *(ie. Twitter Scraper)*  
to run the code. If you have all the necessary downloads, the code should work.

## Note!
Webscraping projects need high maintenance, since the script won't work, if changes are made to the structure of a website. If one of the scripts fails to work, please open an Issue or correct the code yourself and send a pull request. I will happily review your code and implement it, if I find it to be good.


**Happy Scraping!**
