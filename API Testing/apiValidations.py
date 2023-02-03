import json

import requests

response = requests.get('http://216.10.245.166/Library/GetBook.php',
             params= {"AuthorName":"Rahul Shetty2"},)
print(response.text)
# print(type(response.text))
# dict_response = json.loads(response.text)           ##Using json loads method from json library for converting string to dict
json_response = response.json()                    ## Using .json() method for converting string to dict, it is from requests library
# print(type(dict_response1))
# print(dict_response1)
# print(type(dict_response))
# print(dict_response)

# print(json_response[1]["isbn"])
print(response.status_code)
# print(response.headers)
# print(type(response.headers))
# print(response.history)
assert response.status_code == 200
# print(response.headers["Content-Type"])
# assert response.headers["Content-Type"] == "application/json;charset=UTF-8"

## Retrive book details with ISBN RGHCC
actualBook = []
for book in json_response:
    if book['isbn'] == "RGHCC":
        print(book)
        break                   ## -- break statement added to stop the if and for loop and save the first matched value in book
        # actualBook.append(book)
    # print(Book)
# print(actualBook)
# expectedBook = {
#     'book_name': 'Learn Appium Automation with Java',
#     'isbn': 'RGHCC',
#     'aisle': '997555'
# }


# expectedBook = [{'book_name': 'Learn Appium Automation with Java', 'isbn': 'RGHCC', 'aisle': '22755'}, {'book_name': 'Learn Appium Automation with Java', 'isbn': 'RGHCC', 'aisle': '99755'}, {'book_name': 'Learn Appium Automation with Java', 'isbn': 'RGHCC', 'aisle': '997555'}, {'book_name': 'Learn Appium Automation with Java', 'isbn': 'RGHCC', 'aisle': '997005'}, {'book_name': 'Learn Appium Automation with Java', 'isbn': 'RGHCC', 'aisle': '997055'}]

expected1stBook = {'book_name': 'Learn Appium Automation with Java', 'isbn': 'RGHCC', 'aisle': '22755'}
assert book ==expected1stBook