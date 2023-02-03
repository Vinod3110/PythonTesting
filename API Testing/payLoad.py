from utilities.configurations import *

def addBookPayload(isbn):
    body ={
        "name":"Learn Appium Automation with Java",
        "isbn":isbn,
        "aisle":"22aa72",
        "author":"Vinod Pawar"
    }
    return body

def deleteBookPayload(bookId):
    body ={
        "ID": bookId
    }
    return body

def buildPayLoadFromDB(query):
    addBody = {}
    tp = getQuery(query)
    addBody['name'] = tp[0]
    addBody['isbn'] = tp[1]
    addBody['aisle'] = tp[2]
    addBody['author'] = tp[3]
    return addBody