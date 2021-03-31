# pip3 install wheel requests bs4

import requests
from bs4 import BeautifulSoup

amazon = [
    'B08166SLDF',
    #'B089HG351D'
]

ldlc = [
    'PB00387517.html'
]

for i in amazon:
    url = "http://www.amazon.fr/dp/" + i
    print ("Processing: " + url)
    page = requests.get(url,headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"})
    soup = BeautifulSoup(page.content, "html.parser")
    title = soup.find(id="productTitle").get_text().strip()
    price = soup.find(id="priceblock_ourprice").get_text().strip()
    print(title)
    print(price)

for i in ldlc:
    url = "https://www.ldlc.com/fiche/" + i
    print ("Processing: " + url)
    page = requests.get(url,headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"})
    soup = BeautifulSoup(page.content, "html.parser")
    for title in soup.find_all("h1", class_="title-1"):
        print (''.join(title.find_all(text=True)).strip())
    for price in soup.find_all("div", class_="price"):
        print (''.join(price.find_all(text=True)).strip())
