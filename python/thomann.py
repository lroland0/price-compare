# pip3 install requests bs4

import requests
from bs4 import BeautifulSoup



thomann = [
    #'rme_quadmic_ii.htm',
    'electro_harmonix_bigmuff_pi.htm',
    #'B089HG351D'
]

for i in thomann:
    url = "https://www.thomann.de/fr/" + i
    print ("Processing: " + url)
    page = requests.get(url,headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"})
    soup = BeautifulSoup(page.content, "html.parser")
    
    productName = soup.find("h1", attrs={'class':'product-title__title'}).get_text()
    productPrice = soup.find(itemprop="price").get("content")
    
    productCurrency = soup.find(itemprop="priceCurrency").get("content")
    if(productCurrency=="EUR"):
        productDevise="EUR"
    else:
        productDevise="N/A"
    
    productMessage = (soup.find("span", attrs={'class':'fx-availability'}).get_text()).strip()
    if(("Disponible immédiatement" in productMessage)):
        productDispo="Oui"
    else:
        productDispo="Non"

    product={
        "produitNom": productName,
        "dispoValeur": productDispo,
        "dispoMessage": productMessage,
        "prixValeur": productPrice,
        "prixDevise": productCurrency
    }
    
    print(product)
