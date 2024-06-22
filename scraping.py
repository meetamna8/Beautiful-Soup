import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)
# print(r)

soup = BeautifulSoup(r.text, "lxml")
    # lxml is generally considered more convenient than html.parser
# print(soup.prettify())

boxes = soup.find_all("div", class_ = "col-md-4 col-xl-4 col-lg-4")
# print(boxes)
# print(len(boxes))

names = soup.find_all("a", class_ = "title")
# print(names)
# for name in names:
    # print(name.text)

prices = soup.find_all("h4", class_ = "price float-end card-title pull-right")
# print(prices)
# for price in prices:
#     print(price.text)

discriptions = soup.find_all("p", class_ = "description card-text")
# print(discriptions)
# for discription in discriptions:
#     print(discription.text)

ratings = soup.find_all("p", class_ = "review-count float-end")
# print(ratings)
for rating in ratings:
    print(rating.text)


















