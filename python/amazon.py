import requests
from bs4 import BeautifulSoup

amazon = [
    'B08166SLDF',
    #'B089HG351D'
]

for fr in amazon:
    url = "http://www.amazon.fr/dp/" + fr
    print ("Processing: " + url)
    page = requests.get(url,headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"})
    soup = BeautifulSoup(page.content, "html.parser")
    
    priceTitle = (soup.find("span", attrs={'id':'productTitle'}).get_text())
    priceDecimal = (soup.find("span", class_="a-price-whole").get_text())
    priceFration = soup.find("span", class_="a-price-fraction").get_text()
    priceDevise = soup.find("span", class_="a-price-symbol").get_text()
    priceAvailability = soup.find("div", attrs={'id':'availability'}).span.get_text()

    print(priceTitle.lstrip())
    print(priceDecimal+priceFration)
    print(priceDevise)
    print(priceAvailability.lstrip())

for de in amazon:
    url = "http://www.amazon.de/dp/" + de
    print ("Processing: " + url)
    page = requests.get(url,headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"})
    soup = BeautifulSoup(page.content, "html.parser")
    
    priceTitle = (soup.find("span", attrs={'id':'productTitle'}).get_text())
    priceDecimal = (soup.find("span", class_="a-price-whole").get_text())
    priceFration = soup.find("span", class_="a-price-fraction").get_text()
    priceDevise = soup.find("span", class_="a-price-symbol").get_text()
    priceAvailability = soup.find("div", attrs={'id':'availability'}).span.get_text()

    print(priceTitle.lstrip())
    print(priceDecimal+priceFration)
    print(priceDevise)
    print(priceAvailability.lstrip())

for es in amazon:
    url = "http://www.amazon.es/dp/" + de
    print ("Processing: " + url)
    page = requests.get(url,headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"})
    soup = BeautifulSoup(page.content, "html.parser")
    
    priceTitle = (soup.find("span", attrs={'id':'productTitle'}).get_text())
    priceDecimal = (soup.find("span", class_="a-price-whole").get_text())
    priceFration = soup.find("span", class_="a-price-fraction").get_text()
    priceDevise = soup.find("span", class_="a-price-symbol").get_text()
    priceAvailability = soup.find("div", attrs={'id':'availability'}).span.get_text()

    print(priceTitle.lstrip())
    print(priceDecimal+priceFration)
    print(priceDevise)
    print(priceAvailability.lstrip())
