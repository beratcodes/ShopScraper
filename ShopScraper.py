# ----------------------------------------
# Project : ShopScraper
# Author  : beratcodes
# Date    : 2025-12-28
# ----------------------------------------

import requests, codecs, time
from bs4 import BeautifulSoup

headers = {
    "User Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

url = requests.get("https://www.vatanbilgisayar.com/",headers=headers)
x = url.status_code
if x == 200:
    print(f"Status Code: {x}\nBu siteden veri çekilebilir.")
else:
    print(f"Status Code: {x}\nBu siteden veri çekilemez.")

a = url.content 
soup = BeautifulSoup(a, "html.parser")

def get_info():
    count = 1
    for i in soup.find("div",{"class":"opportunity-content clearfix"}).find_all("div",{"class":"col-lg-3"}):
        get_header = i.find("div",{"class":"product-list__product-name"}).h3.text
        get_price = i.find("span", {"class": "product-list__price"}).text
        get_product_code = i.find("div",{"class":"product-list__product-code"}).text.strip()
        get_product_link = i.find("a", {"class":"product-list__link"}).get("href")
        print(f"{count}. {get_header}: {get_price} TL | Product Code : {get_product_code}\nProduct Link: {get_product_link}\n")
        print("-"*40)
        count+=1

def exportToNotepad():
    with codecs.open("product-info.txt","w",encoding="utf-8") as file:
        count = 1
        for i in soup.find("div", {"class": "opportunity-content clearfix"}).find_all("div", {"class": "col-lg-3"}):
            get_header = i.find("div", {"class": "product-list__product-name"}).h3.text
            get_price = i.find("span", {"class": "product-list__price"}).text
            get_product_code = i.find("div", {"class": "product-list__product-code"}).text.strip()
            get_product_link = i.find("a", {"class": "product-list__link"}).get("href")

            file.write(f"{count}. {get_header} | {get_price} TL | {get_product_code} | {get_product_link}\n")
            count += 1
        print("Bilgiler notepad'e aktarılıyor.")
        time.sleep(3)
        print("Bilgiler aktarıldı.")

while True:
    try:
        print("--- SHOP SCRAPER ---")
        select = int(input("0- Çıkış\n1- Verileri Görüntüle\n2- Verileri Notepad'e Aktar\nİŞLEM YAPINIZ: "))
        match select:
            case 0:
                print("Uygulamadan çıkış yapılıyor...")
                break
            case 1:
                print("-"*15, "VATAN BİLGİSAYAR", "-"*15)
                get_info()
            case 2:
                exportToNotepad()
            case _:
                print("Lütfen 0-2 arasında bir değer giriniz.")
    except ValueError:
        print("Lütfen sayısal değer giriniz.")