# There are 3 methods to declare exception in pythin
# 1. raise, 2. Assert, 3. Try and except

# raise

ItemsInCartCount = 4
# if ItemsInCartCount != 2:
#     raise Exception("Condition is not matched raising exception, count is not matching")

## Assertion :-

# assert (ItemsInCartCount == 2)

# Try and Catch(Exception) method
# try:
#     assert (ItemsInCartCount == 2)
#
# except Exception as e:
#     print("condition or the execution from try block is failed so came here to print the configured exception message")
#     print(e)

try:
    with open('textfile.txt', 'r') as reader:
        reader.read()
        print("Try block run successfully ")


except Exception as e:
    print("Condition not matched test is failed and running the except statement")
    print(e)

#finally keyword - this is connected with try and except block
finally:
    print("Cleaning up resources ")
