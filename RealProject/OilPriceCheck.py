from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time 


baseUrl2 = 'http://www.opinet.co.kr/user/dopcsavsel/dopCsAvselSelect.do'
# year_val = input('년도를 4자리를 입력하세요 :') 
# month_val = input('달을 입력해주세요')

driver = webdriver.Chrome()

url = 'http://www.opinet.co.kr/user/main/mainView.do'
driver.get(url)

time.sleep(5)

url = 'http://www.opinet.co.kr/user/dopospdrg/dopOsPdrgSelect.do'
driver.get(url)

time.sleep(1)

html = driver.page_source 

# soup = BeautifulSoup(html,'html.parser')
soup = BeautifulSoup(html,"html.parser")

btn1 = soup.find('#radio1_2')

print(btn1)