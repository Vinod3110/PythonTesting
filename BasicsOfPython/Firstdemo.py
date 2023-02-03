# print("Hello")
a, b, c = 5, 6.34, "World"
# print(a, b, c)
# print("{}{}".format("value is ", b))
# print("{}{}".format("Value is : ", a))

# lists examples
values = [1, 2, "Test", 3, 5]
# print(values[2:5])
values.insert(2, "Vinod")
# print(values)
# print(values[2:5])
values.append("END")
# print(values)
values[2] = "VINOD"
print(values)
del values[0]
print(values)
# Tuple tyep
t1 = (1, 2, "vinod", 4.5, 5)
print(t1[1])
#t1[2] = "VINOD"

# dictionary
dic = {"val1": "Vinod", "last_name": "Pawar", "city": "Sangli"}
print(dic["val1"])
print(dic["last_name"])