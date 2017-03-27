from lxml import html
import requests
from bs4 import BeautifulSoup

url = "https://paytm.com/shop/h/electronics"
r  = requests.get(url)
data = r.text
soup = BeautifulSoup(data,"html.parser")

product = raw_input("Enter product name: ")
product = product.replace(' ', '%20')
# page = requests.get('https://search.paytm.com/search/?page_count=2&userQuery='+product+'&items_per_page=30&resolution=960x720&quality=high&q=tv&cat_tree=1')
page = requests.get('https://paytm.com/shop/search?q='+product+'&from=organic&child_site_id=1&site_id=1')
# print page.content
tree = html.fromstring(page.content)

try:
    item = tree.xpath('//div[@class="_2apC"]/text()')
    # print item
    price = tree.xpath('//span[@class="_1kMS"]/text()')

    print item[0] +"  "+price[0]

except:
    print "Item not found"


