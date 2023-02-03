l1 = ['Name', 'Surname', 'Location', 'Gender', 'Age']
l2 = ['Vinod', 'Pawar', 'Pune', 'Male', 27]
dict ={}
# Printing original keys-value lists
print("Original key list is : " + str(l1))
print("Original value list is : " + str(l2))
for i in l1:
    for j in l2:
        dict[i] = j
        l2.remove(j)
        break
print("Resultant dictionary is : " + str(dict))