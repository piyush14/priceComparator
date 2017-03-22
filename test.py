from bs4 import BeautifulSoup
import re
import requests
import os
url = "www.pythonforbeginners.com/?page=2"

r  = requests.get("http://" +url)
data = r.text
soup = BeautifulSoup(data,"html.parser")

# ----------------> print title <--------------------#

# if soup.find_all('li',class_="hentry"):
#     for s in soup.find_all("a"):
#         if s.get('title') != None and 'bookmark' in str(s.get('rel')):
#             print (s.get('title'))


# ------------> print content <-----------------#

# if soup.find_all('li',class_="hentry"):
#     for s in soup.find_all('div'):
#         if 'post-bodycopy' in str(s.get('class')):
#             # print (s.string)
#             print re.sub(' +', ' ', s.string) # remove unnecessary white spaces


# if soup.find_all('ul',class_='nav nav-pills'):
#     for s in soup.find_all('a'):
#         if 'ul' in str(s.parent):
#             print s.get('title')

# if soup.find_all('ul',class_="nav nav-pills"):
#     for s in soup.find_all('a'):
#         if s.get('title') != None:
#             print s.get('title')

# if soup.find_all('div',class_="categories"):


# ---------> get all categories <----------------#
# divTag = soup.find_all("div", {"class": "categories"})
#
# for tag in divTag:
#     tdTag =  tag.find_all('a')
#     for t in tdTag:
#         print t.text
#

# divFooter = soup.find_all("div",{"class":"post-footer"})
# for tag in divFooter:
#     td = tag.find_all("ul",{"class":"nav nav-pills"})
#     for t in td:
#         if t != '\n':
#             count = count +1
#             text = os.linesep.join([s for s in t.text.splitlines() if s])
#             print text


prod_column=soup.find_all(attrs={'rel':'bookmark'})
for a in prod_column:
    print a.text