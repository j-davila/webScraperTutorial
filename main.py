#Web scraper project using freecodecamp.org tutorial
#https://www.freecodecamp.org/news/scraping-ecommerce-website-with-python/
#José Dávila 03/31/2021

#imports
from bs4 import BeautifulSoup
import requests
import pandas


#setting base url and headers
baseUrl = "https://www.thewhiskyexchange.com"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
 'AppleWebKit''/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

#HTTP call to extract li HTML element(item in a list)
k = requests.get('https://www.thewhiskyexchange.com/c/35/japanese-whisky').text
soup=BeautifulSoup(k, 'html.parser')
productlist = soup.find_all("li",{"class":"product-grid__item"})
print(productlist)


