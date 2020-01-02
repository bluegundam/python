import requests
from bs4 import BeautifulSoup



#URL = "https://whatismyipaddress.com/"
URL = "https://www.whatismyip.com/"
agent = {"User-Agent":"Mozilla/5.0"}

result = requests.get(URL, headers=agent)
soup = BeautifulSoup(result.text, 'html.parser')

#pargination = soup.find("div", {"class": "pagination"})

#target = soup.find("div", {"class" : "cf-error-footer cf-wrapper" })

print(soup)
#print(target)
