with open("../../BasicsOfPython/textfile.txt", 'r') as reader:
    content = reader.readlines()
    # rev_cont = reversed(content)
    # for i in rev_cont:
    #     print(i)
    with open("../../BasicsOfPython/textfile.txt", 'w') as writer:
        for line in reversed(content):
            writer.write(line)
