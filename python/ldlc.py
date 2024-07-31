import requests
import json
import sys
import time
from bs4 import BeautifulSoup

def produitLDLC(url):
    
    page = requests.get(url,headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"})
    soup = BeautifulSoup(page.content, "html.parser")
    
    productName = soup.find("div", attrs={'class':'title'}).h1.get_text().strip()
    productPrice = soup.find("div", attrs={'class':'wrap-aside'}).find("div", attrs={'class':'price'}).get_text().replace('\xa0', '').replace("€",".")
    productMessage = soup.find("div", attrs={'class':'modal-stock-web'}).get_text()
    productDevise = "EUR"

    if(("En stock" in productMessage) or ("en stock" in productMessage)):
        productDispo="Oui"
    else:
        productDispo="Non"
    
    product={
        "produitNom": productName,
        "dispoValeur": productDispo,
        "dispoMessage": productMessage,
        "prixValeur": productPrice,
        "prixDevise": productDevise
    }
    
    return product

produitResult = produitLDLC("https://www.ldlc.com/fiche/PB00409883.html")
print(produitResult)
