# spx
Scrape Morningstar S&amp;P 500 page, return the list
# Import libraries

import webbrowser, requests, bs4, urllib

from bs4 import BeautifulSoup
#browse through morningstar S&P component holding page
holding = "http://portfolios.morningstar.com/fund/index-holdings?t=SPX&region=usa&culture=en-US" #the link for S&P holding

#TODO locate the HTML for each ticker
page = requests.get(holding)
index = page.content

#prepare the soup to parse the html file
morningSoup = BeautifulSoup((index), 'html.parser')

#locate the table in the html file
table= morningSoup.find("table",{"class","r_table2 text2 equity print97"})

#TODO Extract and paste the list of tickers from the S&P500
#file all occurences of the <a> tag
for ticker in table.findAll('a'):
#only copy the result in text form (remove the hyperlink)
    print(ticker.text)
