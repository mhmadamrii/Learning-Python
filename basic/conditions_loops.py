# python uses boolean logic to evaluate conditions

my_numb = 4
print(my_numb == 4)
print(my_numb == 3)


# boolean operators
name = "John"
age = 20

if name == "John" and age == 20 :
    print("Your name is %s, and your age is %d" % (name, age))
    
# The "in" operator
name_two = "Doefd"
if name_two in ["John", "Doe"] :
    print("Your name is either John or Rick")
else:
    print("Your name neither John or Doe")
    
# elif statement
name_three = "Fuck"

if name_three == "Fuck" :
    print("Good")
elif name_three == "Bitch" :
    print("Umm")
else :
    print("Not a command")