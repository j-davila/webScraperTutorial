#Web scraper project using freecodecamp.org tutorial
#https://www.freecodecamp.org/news/scraping-ecommerce-website-with-python/
#José Dávila 03/31/2021

#imports

from bs4 import BeautifulSoup
import requests
import pandas as pd


#setting base,headers, variables, and lists
baseUrl = "https://books.toscrape.com/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ''AppleWebKit''/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
productlinks = []
data=[]
c = 0

#HTTP call to extract li HTML element(item in a list)
# k = requests.get('https://books.toscrape.com/index.html').text
# soup=BeautifulSoup(k,'html.parser')
# productlist = soup.find_all("li",
#                             {"class":"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
# print(productlist)

for x in range(1, 51):
    k = requests.get('https://books.toscrape.com/index.html?pg={}&psize=24&sort=pasc%27'.format(x)).text
    soup = BeautifulSoup(k, 'html.parser')
    productlist = soup.find_all("li",{"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"})

    for product in productlist:
        link = product.find("article",{"class":"product_pod"}).find(
            "h3").find("a").get('href')
        productlinks.append(baseUrl + link)

for link in productlinks:
    f = requests.get(link,headers=headers).text
    hun=BeautifulSoup(f,'html.parser')

    try:
        price=hun.find("p",{"class":"price_color"}).text.replace('\n',"")
    except:
        price = None

    try:
        about=hun.find("p",{"class":"product_page"}).text.replace('\n',"")
    except:
        about=None

    try:
        inStock = hun.find("p",{"class":"instock availability"}).text.replace(
            '\n',"")
    except:
        inStock=None

    try:
        name=hun.find("h1",{"class":"col-sm-6 product_main"}).text.replace(
            '\n',"")
    except:
        name=None

    try:
        rating = hun.find("p", {"class":"star-rating Five"}).text.replace(
            '\n', "")
    except:
        rating = None

    books = {"name":name,"price":price,"in-stock":inStock,"about":about,
              "rating":rating}

    data.append(books)
    c=c+1
    print("completed",c)

df = pd.DataFrame(data)

print(df)
