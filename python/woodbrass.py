# pip3 install requests bs4

import requests
from bs4 import BeautifulSoup

woodbrass = [
    #'rme_quadmic_ii.htm',
    'distortion-fuzz-overdrive-ibanez-tube-screamer-ts9-p21342.html',
    'reverb-delay-anasounds-dystopia-edition-limitee-p385145.html'
    #'B089HG351D'
]

for i in woodbrass:
    url = "https://www.woodbrass.com/" + i
    print ("Processing: " + url)
    page = requests.get(url,headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"})
    soup = BeautifulSoup(page.content, "html.parser")
    
    productName = soup.find("div", attrs={'class':'prodTitleContainer'}).get_text().strip().upper()
    productPrice = soup.find("span", attrs={'class':'fs28-sm'}).get_text()
    productMessage = soup.find("div", attrs={'data-id':'dispo-popup'}).get_text()
    productDevise = "EUR"

    if(("Stock Internet : en stock !" in productMessage) or ("en stock" in productMessage)):
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
    
    print(product)
