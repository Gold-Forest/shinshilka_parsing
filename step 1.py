import requests
import json
from bs4 import BeautifulSoup

# 1. GET ALL URL PAGES
products_url_list =[]

for page in range(0, 13):
    url = f"https://shinshilka.com/?page={page}"

    q = requests.get(url)
    result = q.content

    soup = BeautifulSoup(result, "lxml")
    products = soup.find_all(class_="product_card-thumb product_card-thumb--1x1 product_card-thumb--contain")

    for product in products:
        product_page_url = product.get("href")
        products_url_list.append(product_page_url)

with open("products_url_list.txt", "a") as file:
    for line in products_url_list:
        file.write(f"https://shinshilka.com{line}\n")

# 2. Get data from url list, save to json
# with open("products_url_list.txt") as file:
#     lines = [line.strip() for line in file.readlines()]
#
#     data_dict = []
#     count = 0
#
#     for line in lines:
#         q = requests.get(line)
#         result = q.content
#
#         soup = BeautifulSoup(result, "lxml")
#         product_name = soup.find(class_="product-data").find("h1").text
#
#         product_prices = soup.find(class_="product-prices").find(class_="product-price").text
#         product_price = product_prices.strip()
#
#         data = {
#             "product_name": product_name,
#             "product_price": product_price
#         }
#         count += 1
#         print(f"#{count}: {line} is done!")
#
#         data_dict.append(data)
#
#         with open("data.json", "w", encoding="utf-8") as json_file:
#             json.dump(data_dict, json_file, sort_keys=False, indent=4, ensure_ascii=False, separators=(",", ": "))
