
print("before")

try:
    4 / 0
    # print(age)
except NameError as e:
    print("this is a name issue")
    print(e)
except ZeroDivisionError as e:
    print("can't divide by 0")
    print(e)
except Exception as e:
    print("Something went wrong")
    print(e)
    
class CheeseError(Exception):
    pass
    
def upper_fun(word):
    if len(word) <= 0:
        raise CheeseError("The word has to have at least one letter!")
    return word.upper()

print(upper_fun(""))    

print("after")

# try:
#     print("1234" / 2)
# except:
#     print("You can't divide a string like that")