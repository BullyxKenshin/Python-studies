import requests
from bs4 import BeautifulSoup
url="https://www.imdb.com/chart/top/"
response=requests.get(url)
htmlsee=response.content
soup=BeautifulSoup(htmlsee,"html.parser")
for i in soup.find_all("td",{"class":"titleColumn"}):
   print(i.text)