from bs4 import BeautifulSoup
import urllib2


product = raw_input("Enter product name: ")
product = product.replace(' ', '+')
content = urllib2.urlopen('http://www.flipkart.com/search?otracker=start&q='+product).read()

soup = BeautifulSoup(content)

link = soup.find_all("div", class_="_3wU53n")[0].find_all('a')[0].get('href')
link = "https://www.flipkart.com" + link

seller_info = urllib2.urlopen(link).read()
link_soup = BeautifulSoup(seller_info)

try:
    title = link_soup.find_all("h1", class_="title")[0].string.strip()
    print "Title: " + title
except:
    print "Product not found"

try:
    subtitle = link_soup.find_all("span", class_="subtitle")[0].string.strip()
    print "Subtitle: " + subtitle
except:
    print "Subtitle not found"

try:
    price = link_soup.find_all("span", class_="selling-price omniture-field")[0].string.strip()
    print "Price:  " + 	price
except:
    pass

print "Link: " + link

try:
    seller = link_soup.find_all("a", class_="seller-name")[0].string.strip()
    print "Seller: " + seller
except:
    pass