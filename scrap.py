import requests
from bs4 import BeautifulSoup
URL= 'https://www.amazon.in/Fujifilm-Instax-Instant-Camera-Grape/dp/B00R17NEJE/ref=sr_1_8?crid=1OZ45JGC5QO6N&keywords=fujifilm+instax+mini+9&qid=1568361632&sprefix=fujifilm%2Caps%2C1004&sr=8-8'

headers ={"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
page=requests.get(URL,headers=headers)

soup=BeautifulSoup(page.content,'lxml')
#title = soup.find(id="productTitle")
#ti=soup.find("span", {"id": "productTitle"})

title = soup.find(id="productTitle").get_text()
price =soup.find(id="priceblock_ourprice").get_text()
converted_price = int(price[2:7])
print(converted_price)
print(title.strip())