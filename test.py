from bs4 import BeautifulSoup

import requests

url = "www.pythonforbeginners.com/?page=2"

r  = requests.get("http://" +url)
data = r.text
soup = BeautifulSoup(data,"html.parser")

if soup.find_all('li',class_="hentry"):
    for s in soup.find_all("a"):
        if s.get('title') != None and 'bookmark' in str(s.get('rel')):
            print (s.get('title'))

