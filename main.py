import csv
import time
import json
import random 
import datetime
from os import system


from core.json.config import DOMEN,URL,HEADERS


import requests
from bs4 import BeautifulSoup
count_site= int(input('сколько страниц спарсить: '))
# # ------------------------------------------------------------------------------------------------



for count in range(1,count_site +1):
    response= requests.get(url=URL,headers=HEADERS,params={"page":f"page-{count}"})

    with open(f"core/html/index.html","a",encoding="UTF-8") as file:
        file.write(response.text)


# # -------------------------------------------------------------------------------

    with open("core/html/index.html","r") as file:
        srs = file.read()

        soup = BeautifulSoup(srs,"lxml").find_all("div",class_="product-item-container")

    with open("core/html/index.html","w") as file:
            file.write(str(soup))
#     # -------------------------------------------------------------------------------


    with open("core/html/index.html", "r") as file:
        srs = file.read()


    soup = BeautifulSoup(srs,"lxml").find_all("a")

    info = []

    for i in soup:
        url_product = DOMEN + i.get("href")
        name_product = i.get("data-name")
        cotegory_prodauct = str(i.get("data-category")).replace("/", " ")
        price = i.find("span", class_="new-product__new-price").text.strip()

        info.append(

            {
                "Название": name_product,
                "Ссылка" : url_product, 
                "Котегории" : cotegory_prodauct,
                "Цена" : price
            }
        )

        # print("Название", name_product)
        # print("Ссылка", url_product)
        # print("Котегории", cotegory_prodauct)
        # print(f"Цена: {price}\n")


with open("core/json/info.json", "w", encoding="utf-8") as file:
    json.dump(info, file, indent=4, ensure_ascii=False)