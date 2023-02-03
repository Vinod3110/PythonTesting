import json

req = '{"name":"Vinod Anil Pawar","Lang":["Java", "Python"]}'

# dict_req = json.loads(req)
# print(type(dict_req))
# print(dict_req)
# print(dict_req["name"])
# # lst_lang= dict_req["Lang"]
# # print(type(lst_lang))
# # print(lst_lang[0])
# print(dict_req["Lang"][1])

#### ************** Perse content present in json file *******
# with open("C:\\Users\\VINOD\\Desktop\\practicejsonfile.json") as file:
    # data = json.load(file)
    # # print(data)
    # print(data["info"]["schema"])
    # print(data["item"][0]["item"][0]["request"]["url"]["host"])
    # print(data["item"][0]["item"][0]["request"]["url"]["query"][0]["value"])
    # print(type(data["item"][0]["item"][0]["request"]["url"]["host"]))

with open("C:\\Users\\VINOD\\Desktop\\practicejsonfile_01.json") as file:
    data = json.load(file)
    # print(data)
    # print(type(data["courses"]))
    # print(data["courses"][2]["title"])
    # print(data["dashboard"]["website"])

## Print the value of RPA course without using list index
    # print(type(data["courses"]))
    # for course in data["courses"]:
    #     # print(course)
    #     if course["title"] == "RPA" :
    #         print(course["price"])
    #         assert course['price'] == "INR449"

## Compare 2 Json files
with open("C:\\Users\\VINOD\\Desktop\\practicejsonfile_02.json") as file2:      #Opening second json file for comparison
    data1 = json.load(file2)        #loading json file into data1

assert data == data1
print("Both the files are same")