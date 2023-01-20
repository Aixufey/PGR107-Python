# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
    Variables
"""

# One value to multiple variables
x = y = z = "My Variable"

print(x)
print(y)
print(z)

# Many values to multiple variables
a, b, c = "apple", "orange", "banana"
print(a)
print(b)
print(c)


# destructuring / unpacking
fruits = ["apple", "orange", "banana"]
apple, orange, banana = fruits

print(apple)
print(orange)
print(banana)


# print text with variable is used with comma
name = "John"
age = 18
print(name, age)



# Global and Scope variables
arg = "John Doe"

def myFunc():
    print(arg)
    
myFunc()

# Scoped
def myFunc2():
    arg = "John Snow"
    print(arg)
    
myFunc2()

"""
    String repeat
    
"""
repeatThis = "Hello "
print(repeatThis * 10)


"""
    Parametric functions
    One asterix = arbitrary arguments
    Two asterix = arbitrary Keyword arguments
"""

def myTodos(*args):
    print("To-do: ", args)
    print("To-do on list index 1: ", args[1])
    
    x, y, z = args
    print("unpacking and print index 1: ", y)

myTodos("Pay bill", "Clean house", "Do homework")


def myEnhancedTodos(**Kwargs):
    print("To-do: ", Kwargs["hiPrio"])
    
myEnhancedTodos(hiPrio = "Learn Python", lowPrio = None)

# arbitrary conditional fun
def myProFun(*args):
    if (len(args) > 0): 
        print("This argument: ", *args)
myProFun()


"""
    Strings
"""
greet = "Hello World"
print(greet[0:5])
print(greet[6:11])

# Negative index -3 is from right to left, r[-3] l[-2] d[-1] H[0] e[1] ...
print(greet[-3]) 
hello = greet[0:5].upper()
world = greet[6:11].lower()

print("%s-%s" %(hello, world))
print("{}-{}".format(hello, world))

# Interpolation String
itemName = "Monster White"
price = 19
quantity = 1
myPurchase = "I am buying {} quantity of item {} for {} ,-"
print(myPurchase.format(quantity,itemName, price))


"""
    Booleans
"""

isNumber = "100"

if(isinstance(isNumber, int)):        
    print("Yes")
else:
    print("No")


"""
    Collections in Python
    List = [] mutable list, duplicates OK, ordered, indexed
    Tuple = (, , ,) immutable, duplicates OK, ordered, indexed
    Set =  {} immutable(can remove and add), unique only, unordered, no index
    Dictionaries = {k,v} mutable, unique only, ordered if Python == 3.7
"""
thisList = ["iPhone", "Android", "Android", 100, 100, False]
thisList[0] = "IPHONE"
print(type(thisList), thisList)

thisTuple = ("iPhone", "Android", "Android", 100, 100, False)
#thisTuple[0] = "IPHONE" immutable object
print(type(thisTuple), thisTuple[0])

thisSet = {"iPhone", "Android", "Android", 100, 100, False}
# thisSet[0] = "IPHONE" immutable object
# discard will not cause exception while remove will if item does not exist
thisSet.discard("iPhone")
thisSet.add("IPHONE") 
print(type(thisSet), thisSet)

thisDictionaries = {
    "iPhone" : "13",
    "Android" : "Google Pixel 7",
    "Android" : "Google Pixel 7",
    "Price" : [100, 1000, 10000]
}
print(type(thisDictionaries), type(thisDictionaries["Price"]), thisDictionaries)
print("iPhone 13 costs more than %s dollars." % thisDictionaries["Price"][0])

"""
    import Array libarry
"""
import numpy as np
print(np.array([1,2,3,4,5]))


"""
    Class
    All classes has __init__() function when instantiated
    The first parameter in this case 'this' can be named anything
    Essentially it means, it belongs to this class
"""
class Motherboard:
    
    def __init__(this, brand, model, ramSlots, cardSlots):
        this.brand = brand
        this.model = model
        this.ramslots = ramSlots
        this.cardSlots = cardSlots
    
    def startUp(this):
        print("Booting..")
        
   
mobo = Motherboard("Asus", "P6T", "4", "2")
mobo.startUp()


"""
    user input
"""
#userName = input("Enter username: ")
#print("Username: %s" % userName)





