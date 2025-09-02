
# Functions

# def greet():
#     print("Hi there")
#     print("Hello world")


# greet()


# Arguments
# this function is reusable and we can call it with differen arguments
# by default , params that we pass are required , else iwe get type error -missing positional argument
def greet(first_name, last_name):
    print(f"hi {first_name} {last_name}")
    print("Welcome aboard")


greet("John", "Smith")
greet("Bob", "Baker")

# greet("Chris") -pylint is complaining ,saying there is no argument for last name, we get type error


# Type of functions
# 1. Functions that carry out/perform a task --type1
# 2.functions that calculate and return a  --type 2

def greet1(name):
    print(f"hi {name}")  # this func just prints on the terminal


greet1("Anna")


def greet2(name):
    return f"Hi {name}"


message = greet2("Chris")
print(message)
file = open("content.txt", "w")  # creating file to write a message
file.write(message)  # writing message to a file


# what if we put greet call inside of print func.
def greet3(name):
    print(f"Hi {name}")


# returns None value -- even it returns None it is classified as type 1 func..
print(greet3("Lily"))


# Keyword Arguments

# def increment(number, by):
#     return number+by


# result = increment(2, 1)
# print(result)

# print(increment(2, 1))

# print(increment(2, by=1))  # by is a key word argument


# Default argument
def increment(number, by=1):
    return number + by


print(increment(5))
print(increment(2, 6))


# *args

def multiply(*numbers):
    total = 1
    for number in numbers:
        total = total * number
    return total


print(multiply(2, 3, 4, 5))
