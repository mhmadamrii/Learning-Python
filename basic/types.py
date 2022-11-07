# this file contains types, output, and arithmatic  operators

# numbers
myInt = 10
print(myInt)

# strings
myString = 'Hello'
print(myString)

# lists(array)
myList = []
myList.append(1)
myList.append(4)

print(myList[0])
print("my lists =>", myList)

# reminder/modulus
remainder = 11 % 3
print(remainder)

squared = 7 ** 2
print(squared)

lotSayHellos = "Hello" * 10
print(lotSayHellos)

# using operators with lists
even_numbers = [1, 2, 3, 4]
odd_numbers = [6, 7, 8, 9]

all_numbers = even_numbers + odd_numbers

print(all_numbers)

# python supports forming new lists with repeating sequence using the multiplication operator
print([1, 2, 3] *  3)