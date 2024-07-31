# pip3 install requests bs4

import requests
from bs4 import BeautifulSoup

palf = [
    #'rme_quadmic_ii.htm',
    'saturation/fuzz/autre-fuzz/fjord-fuzz-sol.html#/718-modele-sol_originale',
    'accessoire/alimentation/alimentation-a-decoupage/equerres-de-fixation-pour-k.html',
    #'B089HG351D'
]

for i in palf:
    url = "https://www.palf.fr/" + i
    print ("Processing: " + url)
    page = requests.get(url,headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"})
    soup = BeautifulSoup(page.content, "html.parser")
    
    productName = soup.find("h1", attrs={'class':'product-name-custom'}).get_text().strip()
    productBrand = soup.find("p", attrs={'class':'brand-name-custom'}).get_text().strip()
    productPrice = soup.find(itemprop="price").get("content").strip()
    productDevise = "EUR"
    
    productMessage = ' '.join((soup.find("span", attrs={'id':'product-availability'}).p.get_text(strip=True)).split())
    if(("En stock" in productMessage) or ("en stock" in productMessage)):
        productDispo="Oui"
    else:
        productDispo="Non"

    product={
        "produitNom": productBrand+" "+productName,
        "dispoValeur": productDispo,
        "dispoMessage": productMessage,
        "prixValeur": productPrice,
        "prixDevise": productDevise
    }
    
    print(product)
