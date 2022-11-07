# functions in python are defined using the block keyword "def", followed with the function's name as the block's name

def my_function() :
    print("Hello from my_function")
    
my_function()

# functions with arguments
def my_function_with_arguments(username, greeting) :
    print("Hello %s!, wish you %s" % (username, greeting))
    
my_function_with_arguments("mhmadamrii", "fine")

# functions with return keyword
def sum_two_numbers(a, b) :
    return print(a + b)

sum_two_numbers(5, 10)
