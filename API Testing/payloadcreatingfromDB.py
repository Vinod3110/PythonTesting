import requests
from utilities.configurations import *
from payLoad import *
from utilities.resources import *

##-- Add Book
url = getConfig()['API']['qa_endpoint'] + apiResources.addBook
header = {'Content-Type': 'application/json'}
query = 'select * from Books'
payload = buildPayLoadFromDB(query)
print(payload)
resp = requests.post(url, json=buildPayLoadFromDB(query), headers=header, )
print(resp.json())