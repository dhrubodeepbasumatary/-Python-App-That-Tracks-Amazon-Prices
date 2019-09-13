import requests
import smtplib
from bs4 import BeautifulSoup
URL= 'https://www.amazon.in/Fujifilm-Instax-Instant-Camera-Grape/dp/B00R17NEJE/ref=sr_1_8?crid=1OZ45JGC5QO6N&keywords=fujifilm+instax+mini+9&qid=1568361632&sprefix=fujifilm%2Caps%2C1004&sr=8-8'

headers ={"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    
def check_price():
    page=requests.get(URL,headers=headers)
    soup=BeautifulSoup(page.content,'lxml')
    title = soup.find(id="productTitle").get_text()
    price =soup.find(id="priceblock_ourprice").get_text()

    price=str(price[2:])
    i=0 
    s=""
    n=len(price)
    while i<n and price[i]!='.':
        if(price[i]!=','):
            s+=price[i]

        i+=1
    #temp=price[5] 
    #converted_price = price[4:5]
    converted_price=float(s)
    print(converted_price)
    # print(title.strip())
    if(converted_price>2000):
        send_mail()

    print(converted_price)
    print(title.strip())



# import requests
# import smtplib
# from bs4 import BeautifulSoup
# URL= 'https://www.amazon.in/Fujifilm-Instax-Instant-Camera-Grape/dp/B00R17NEJE/ref=sr_1_8?crid=1OZ45JGC5QO6N&keywords=fujifilm+instax+mini+9&qid=1568361632&sprefix=fujifilm%2Caps%2C1004&sr=8-8'

# headers ={"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

# def check_price():
# 	page=requests.get(URL,headers=headers)
# 	soup=BeautifulSoup(page.content,'lxml')
# 	#title = soup.find(id="productTitle")
# 	#ti=soup.find("span", {"id": "productTitle"})
# 	title = soup.find(id="productTitle").get_text()
# 	price =soup.find(id="priceblock_ourprice").get_text()

#     # title = soup.find(id="productTitle").get_text() 
#     # price =soup.find(id="priceblock_ourprice").get_text()
#     price=str(price[2:])
#     i=0 
#     s=""
#     n=len(price)
#     while i<n and price[i]!='.':
#         if(price[i]!=','):
#             s+=price[i]

#         i+=1
#     #temp=price[5] 
#     #converted_price = price[4:5]
#     converted_price=float(s)
#         if(converted_price<2000):
#         send_mail()

#         print(converted_price)
#         print(title.strip())


def send_mail():
	server=smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('dohnking123@gmail.com','')

	subject='Price fell down'
    body='check the amazon link'

    msg=f"Subject:{subject}\n\n{body}"
    
    server.sendmail(
     'dohnking123@gmail.com'
     'dhrubodeepbasumatary123@gmail.com'
      msg
    )
    print('email has been send')

    server.quit()