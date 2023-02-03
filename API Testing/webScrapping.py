import requests
from bs4 import BeautifulSoup

li = []
# actionTVSerialsURL = "https://www.imdb.com/find/?s=ep&q=Action&ref_=nv_sr_sm"
# top250MoVieList = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
trainListUrl = "https://www.makemytrip.com/railways/listing?classCode=&className=All%20Classes&date=20230120&destCity=Miraj&destStn=MRJ&srcCity=Pune&srcStn=PUNE"
data = requests.get(trainListUrl)
soup = BeautifulSoup(data.content, 'html.parser')
print(soup.prettify())
# moviesTable = soup.find('table', {'class': 'lister'})
# print(moviesTable.prettify())
