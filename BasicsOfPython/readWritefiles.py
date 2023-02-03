file = open("textfile.txt")
## Read the whole file with read method
#print(file.read())

#Read the n number charaters from the file with parameter passing
#print(file.read(50))

# Read the file line by line
# print(file.readline())
# print(file.readline())
# print(file.readline())

#Read the file whole file using readline method
# line = file.readline()
# while line != "":
#     print(line)
#     line=file.readline()

#Read the whole file using readlines method
for line in file.readlines():
    print(line)
print(file.readlines())
file.close()

## Read the file and reverse the file content and write the file content on same location.

with open("textfile.txt", 'r') as reader:
    content = reader.readlines()
    # rev_cont = reversed(content)
    # for i in rev_cont:
    #     print(i)
    with open("textfile.txt", 'w') as writer:
        for line in reversed(content):
            writer.write(line)




