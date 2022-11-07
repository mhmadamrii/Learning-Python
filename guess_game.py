import random
import math

lower = int(input("Enter lower number: "))
upper = int(input("Enter upper number: "))

x = random.randint(lower, upper)
print("You've only ", round(math.log(upper - lower + 1, 2)), "chances to guess the number")

count = 0

while count < math.log(upper - lower + 1, 2):
      count += 1
      
      guess = int(input("Guess a number: "))
      
      if x == guess:
            print("Congrats you did it in ", count, " try")
            break
      elif x > guess:
            print("You guessed too small")
      elif x < guess:
            print("You guessed too high")
            
if count >= math.log(upper - lower + 1, 2):
      print("The number is %d" %x)
      print("Better next time")