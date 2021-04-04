#Web scraper project using freecodecamp.org tutorial
#https://www.freecodecamp.org/news/scraping-ecommerce-website-with-python/
#José Dávila 03/31/2021

#imports

from bs4 import BeautifulSoup
import requests
import pandas as pd


#setting base,headers, variables, and lists
#baseUrl = "https://www.thewhiskyexchange.com"
baseUrl = "https://books.toscrape.com/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ''AppleWebKit''/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
productlinks = []
data=[]
c = 0

#HTTP call to extract li HTML element(item in a list)
#k = requests.get('https://www.thewhiskyexchange.com/c/35/japanese-whisky').text
k = requests.get('https://books.toscrape.com/index.html').text
soup=BeautifulSoup(k,'html.parser')
#productlist = soup.find_all("li", {"class":"product-grid__item"})
productlist = soup.find_all("li",
                            {"class":"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
print(productlist)

for x in range(1, 6):
 k = requests.get(
  'https://www.thewhiskyexchange.com/c/35/japanese-whisky?pg=''{}&psize=24&sort=pasc'.format(x)).text

 soup = BeautifulSoup(k, 'html.parser')
 productlist = soup.find_all("li",{"class": "product-grid__item"})

 for product in productlist:
  link = product.find("a",{"class": "product-card"}).get('href')
  productlinks.append(baseUrl + link)

for link in productlinks:
    f = requests.get(link,headers=headers).text
    hun=BeautifulSoup(f,'html.parser')

    try:
        price=hun.find("p",{"class":"product-action__price"}).text.replace('\n',"")
    except:
        price = None

    try:
        about=hun.find("div",{"class":"product-main__description"}).text.replace('\n',"")
    except:
        about=None

    try:
        rating = hun.find("div",{"class":"review-overview"}).text.replace('\n',"")
    except:
        rating=None

    try:
        name=hun.find("h1",{"class":"product-main__name"}).text.replace('\n',"")
    except:
        name=None

    whisky = {"name":name,"price":price,"rating":rating,"about":about}

    data.append(whisky)
    c=c+1
    print("completed",c)

df = pd.DataFrame(data)

print(df)
