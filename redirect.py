import urllib
# import urllib2
#
# def get_redirected_url(url):
#     opener = urllib2.build_opener(urllib2.HTTPRedirectHandler)
#     request = opener.open(url)
#     return request.url
#
# print get_redirected_url("http://google.com/")
import requests
#
# response = requests.get('http://google.com/')
# if response.history:
#     print "Request was redirected"
#     for resp in response.history:
#         print resp.status_code, resp.url
#     print "Final destination:"
#     print response.status_code, response.url
# else:
#     print "Request was not redirected"


from lxml import html
import requests
from bs4 import BeautifulSoup

url = "https://paytm.com/shop/h/electronics"
r  = requests.get(url)
data = r.text
soup = BeautifulSoup(data,"html.parser")

product = raw_input("Enter product name: ")
# product = product.replace(' ', '%20')
page = requests.get('https://search.paytm.com/search/?page_count=2&userQuery='+product+'&items_per_page=30&resolution=960x720&quality=high&q=tv&cat_tree=1')
# page = requests.get('https://paytm.com/shop/search?q='+product+'&from=organic&child_site_id=1&site_id=1')
data = page.json()

for group in data['grid_layout']:
    print group['name']+"  "+str(group['actual_price'])
