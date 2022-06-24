import requests
from bs4 import BeautifulSoup as bs

URL = input("Enter URL of the item you want to get the price of: \n")

page = requests.get(URL ,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"})

soup = bs(page.content,"html.parser")

title = soup.find(id='productTitle').get_text().strip()
print(f'Title: {title}')

try:
    availabilty = soup.find(id='outOfStock').get_text()
    availabilty = availabilty.lower()
    if 'currently unavailable' in availabilty:
        available = False

except:
    available= True

if available:
    print('Item is available')
    price = soup.find(id="tp-tool-tip-subtotal-price-value").get_text()
    price = price[1:]
    price = price[:len(price)//2]
    price = price.replace(',', '')
    price = float(price)
    print(f'Price: {price}')

else:
    print('Item isnt available')