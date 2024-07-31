import requests
import json
import sys
import time
from bs4 import BeautifulSoup

def produitTopAchat(url):
    
    page = requests.get(url,headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"})
    soup = BeautifulSoup(page.content, "html.parser")
    
    productName = soup.find('h1', class_='ps-main__product-title').get_text().strip()
    productPrice = soup.find("span", attrs={'class':'offer-price__price'}).get_text().replace("€","").strip()
    productMessage = soup.find("div", attrs={'class':'offer-stock'}).get_text().strip()
    productDevise = "EUR"

    if(("En stock" in productMessage) or ("en stock" in productMessage) or ("EN STOCK" in productMessage)):
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

produitResult = produitTopAchat("https://www.topachat.com/pages/detail2_cat_est_micro_puis_rubrique_est_wpr_puis_ref_est_in20016203.html")
print(produitResult)
