import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

# Creating empty arrays to store data and a empty dataframe
info = []
sku = []
price = []
ship_time = []
# products = [643085] #pi zero 2 w 
# # products = [650108] #pico w
products = {
  "pi zero 2 W": 643085,
  "pi 4 model b 8gb": 622539,
  "pi 4 model b 4gb": 637834,
  "pi 4 model b 2gb": 621439,
  "pi zero w": 486575,
}

def init():
    # Initial loops through each page
    res = requests.get('https://www.microcenter.com')
    soup = BeautifulSoup(res.text, "html.parser")
    
    for product in products:
        print("Inventory for %s" % product)
        for item in soup.select("ul.dropdown-menu > li.dropdown-itemLI a.dropdown-item"):        
            href = item['href']
            x = re.search("\d{3}", href)
            storeNumber = x.group()
            # print("%s%s%s" % (item.span.string, item.span.next_sibling.string, item.span.next_sibling.next_sibling.string))
            #print('href: %s' % href)
            #print('storeNumber: %s' % storeNumber)

            #storeRes = requests.get('https://www.microcenter.com/product/%s/raspberry-pi-zero-2-w?storeid=%s' % (product, storeNumber))
            storeRes = requests.get('https://www.microcenter.com/product/%s/raspberry-pi-pico-w?storeid=%s' % (products[product], storeNumber))
            storeSoup = BeautifulSoup(storeRes.text, "html.parser")
            stock = storeSoup.select_one("div#pnlInventory > div.inventory i.text-slate-blue")
            #print(stock)
            if(stock is not None):
                print('Stock Avalable @ %s%s%s' % (item.span.string, item.span.next_sibling.string, item.span.next_sibling.next_sibling.string))
            

init()
# for pgn in range(1,8):
#     url = "https://www.microcenter.com/search/search_results.aspx?N=4294967288&NTK=all&page=" + str(pgn) + "&cat=Laptops/Notebooks-:-MicroCenter"

#     url = "https://www.microcenter.com/product/643085/raspberry-pi-zero-2-w?storeid=065"
#     url = "https://www.microcenter.com/product/622539/raspberry-pi-4-model-b-8gb-ddr4?storeid=181"
#     url = "https://www.microcenter.com/product/637834/raspberry-pi-4-model-b-4gb-ddr4?storeid=181"
#     url = "https://www.microcenter.com/product/621439/raspberry-pi-4-model-b-2gb-ddr4?storeid=181"
#     url = "https://www.microcenter.com/product/486575/raspberry-pi-zero-w-microcontroller-development-board?storeid=181"

#     #document.querySelectorAll('ul.dropdown-menu > li.dropdown-itemLI > a.dropdown-item')[0].href
#     res = requests.get(url)
#     soup = BeautifulSoup(res.text)
#    #loops to get each text from each CSS selector 
#     for info_select in soup.select(".normal a"):
#         info.append(info_select.text)
#     for sku_select in soup.select(".sku"):
#         sku.append(sku_select.text)
#     for price_select in soup.select(".price > span"):
#         price.append(price_select.text) 
#     for ship_time_select in soup.select(".availabilityTrunc"):
#         ship_time.append(ship_time_select.text)   

# # Creating dataframe
# df=pd.DataFrame(columns=['info','sku','price','ship_time'])
# df['info']=pd.DataFrame(info)
# df['sku']=pd.DataFrame(sku)
# df['price']=pd.DataFrame(price)
# df['ship_time']=pd.DataFrame(ship_time)

# df