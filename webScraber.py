from bs4 import BeautifulSoup
import requests

search=input("enter search value:")
params={"q": search}

request=requests.get("https://www.google.com/search",params=params)
soup=BeautifulSoup(request.text,"html5lib")
print(soup.prettify())