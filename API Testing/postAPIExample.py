import requests
from utilities.configurations import *
from payLoad import *
from utilities.resources import *
##-- Add Book
# url = getConfig()['API']['qa_endpoint'] + apiResources.addBook
delete_url = getConfig()['API']['qa_endpoint'] + apiResources.deleteBook
# headers = {'Content-Type': 'application/json'}
response = requests.post(url, json=addBookPayload("33anc13"), headers=headers,)
# print(response.status_code)
# json_res = response.json()
# print(json_res)
# bookID = json_res['ID']
# print(bookID)
# ##-- Delete Book API
# deleteBook_response = requests.post(delete_url, json=deleteBookPayload(bookID), headers=headers,)
# jsonResponse_delete = deleteBook_response.json()
# print(jsonResponse_delete)
# print(jsonResponse_delete["msg"])
# print(deleteBook_response.status_code)
# try:
#     assert deleteBook_response.status_code == 200
#     print("Status code != 200")
# except Exception as e:
#     print(e)
#     print("{}{}".format('Status code is ', deleteBook_response.status_code))
# try:
#     assert jsonResponse_delete["msg"] == "book is successfully deleted"
#     print("didn't get correct success message")
# except Exception as e:
#     print(e)
#     print("{}{}".format('Current response message is :- ',jsonResponse_delete["msg"]))

##-- Authentication
se = requests.session()        #- Created seesion mannager for passing authentication single time in all API calls
se.auth = auth=('pawarv40@gmail.com', getPassword())


git_url = "https://api.github.com/user"
github_response = requests.get(git_url, verify=False, auth=('pawarv40@gmail.com', getPassword()))
# git_resp = se.get(git_url, verify=False)
print(github_response.status_code)
print(github_response.text)
# print(git_resp.json())

#-Repo list API
repo_lst_url = "https://api.github.com/user/repos"
lst_resp = se.get(repo_lst_url)
print(lst_resp.status_code)
print(lst_resp.text)
# print(lst_resp.json())

## ------------------------------------------------ Ruff Wor -------------
#
# # try:
# #     response_json = json.loads(addBook_response)
# #     print(response_json)
# # except Exception as e:
# #     print(e)
# #     print("Execption occurs")
#
# # json_response = addBook_response.json()
# # print(json_response)
