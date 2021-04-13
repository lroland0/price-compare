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

topachat = [
    'detail2_cat_est_micro_puis_rubrique_est_wpr_puis_ref_est_in20005853.html'
]

materielnet = [
    '202010120110.html'
]

grosbill = [
    '4-amd_ryzen_5_5600x_4_6ghz_35mo_am4_box-758584-informatique-_processeur'
]

for i in amazon:
    url = "http://www.amazon.fr/dp/" + i
    print ("Processing: " + url)
    page = requests.get(url,headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"})
    soup = BeautifulSoup(page.content, "html.parser")
    price = soup.find(id="priceblock_ourprice").get_text().strip()
    print(price)

for i in ldlc:
    url = "https://www.ldlc.com/fiche/" + i
    print ("Processing: " + url)
    page = requests.get(url,headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"})
    soup = BeautifulSoup(page.content, "html.parser")
    for price in soup.find_all("div", class_="price", limit = 4):
        test = ''.join(price.find_all(text=True)).strip()
        print (test)

for i in topachat:
    url = "https://www.topachat.com/pages/" + i
    print ("Processing: " + url)
    page = requests.get(url,headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"})
    soup = BeautifulSoup(page.content, "html.parser")
    for price in soup.find_all("span", class_="priceFinal"):
        test = ''.join(price.find_all(text=True)).strip()
        print (test)

for i in materielnet:
    url = "https://www.materiel.net/produit/" + i
    print ("Processing: " + url)
    page = requests.get(url,headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"})
    soup = BeautifulSoup(page.content, "html.parser")
    for price in soup.find_all("span", class_="o-product__price"):
        test = ''.join(price.find_all(text=True)).strip()
        print (test)

for i in grosbill:
    url = "https://www.grosbill.com/" + i
    print ("Processing: " + url)
    page = requests.get(url,headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"})
    soup = BeautifulSoup(page.content, "html.parser")
    price = soup.find("b", itemprop="price").get_text().strip()
    print(price)
