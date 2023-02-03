import csv

##-- Read from CSV file
# with open ('utilities/loanStatus.csv') as csvFile:
#     file_reader = csv.reader(csvFile)
#     # print(list(file_reader))
#     names = []
#     status = []
#     for row in file_reader:
#         # print(row)
#         names.append(row[0])
#         status.append(row[1])
#     print(names)
#     print(status)
#     index = names.index('Ram')
#     loanStatus = status[index]
#     print("Loan Status is "+loanStatus)

##-- Write into existing csv file

with open('utilities/loanStatus.csv', 'a') as wFile:
    write = csv.writer(wFile)
    write.writerow(["Vins","Approved",])