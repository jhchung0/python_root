import urllib.request
from bs4 import BeautifulSoup

url = 'http://10.10.10.38:13000/app2jhc'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

print (html)