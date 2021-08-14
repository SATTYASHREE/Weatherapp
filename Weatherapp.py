# Project Requirement : Is to get the weather info of entered city name

# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                          'Chrome/58.0.3029.110 Safari/537.3'}

# https://www.google.com/search?q=testCity&oq=testCity&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8

# "https://www.google.com/search?q=" + "weather" + city

import requests
from bs4 import BeautifulSoup
city = input("Enter city Name: ")

url = "https://www.google.com/search?q=weather " + city  #third party
html = requests.get(url).content # JSON , #XML #html

response_data = BeautifulSoup(html,'html.parser')
# print(response_data)
temp = response_data.find('div',attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
day = response_data.find('div',attrs={'class':'BNeawe tAd8D AP7Wnd'}).text
print(temp)
print(day)

# get list of all near cities near bangalore(Entered city)
