# python uses C style  string formattin to create new, formatted strings

name = "John"
print("Hello, %s!" % name)

# to use two more argument specifiers, use a tuple (parenthless)
name2 = "Kennedy"
age = 59

print("%s is %d" % (name, age))

myList = [1, 2, 3]
print("A list: %s" % myList)

myString = "Hello World!"
print(len(myString))