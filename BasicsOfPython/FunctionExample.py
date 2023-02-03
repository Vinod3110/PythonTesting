# Functions

# def Reverse(s):
#  rev_str = ""
# for i in s:
#      rev_str = i + rev_str
#   return rev_str

# my_string = "My Name is Vinod Pawar"

# def addition(a, b):
# print(a+ b)
#   return a + b


# print(addition(1,6))


def sumation(a, b):
    c = 0
    c = a + b
    return c


addition = sumation(3, 5)
print("{}{}".format("Addition is :- ", addition))


def fibno(nth):
    n1, n2 = 0, 1
    term = 0
    if nth < 0:
        print("Please enter Positive input")
    elif nth == 1:
        print("fibonacci Sequence is :- ")
        return n1
    else:
        while (nth > 0):
            print(n1)
            term = n1 + n2
            # Update values
            n1 = n2
            n2 = term
            nth = nth - 1
    #return term


print(fibno(5))
