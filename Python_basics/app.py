# variables
import math
student_count = 100
rating = 4.99
is_published = True
course_name = "Python programming"
print(student_count)

# strings
course = "Python programming"

# len methods
print(len(course))

# to get access to specific element/character - strings in python are zero index based
print(course[0])

# negative index -returns first char from the end of string
print(course[-1])

# slicing a string - to extract grp of characters - below is starting from zero index to index 2, char at index 3 is not included
print(course[0:3])

# starts from zero and goes all the way to end of string -returns new string i.e exactly same as original string
print(course[0:])

# python puts 0 by default as starting index in the below case
print(course[: 3])

# makes a copy of original string
print(course[:])


# escape sequences are - e.g.to put double quotes in the middle of string
# \", \', \\, \n -escapes the char after backslash

course1 = "Python \"programmer"
print(course1)

course2 = 'Python \'programmer'
print(course2)

course3 = "Python \\programmer"
print(course3)

course4 = "Python \nprogrammer"
print(course4)


# Formatted strings

first = "Latha"
last = "Ch"

# using concat operator  +
full = first + " " + last
print(full)

# using formatted string

full1 = f"{first} {last}"
print(full1)

full1_len = f"{len(first)} {2 + 2}"
print(full1_len)


# String Methods

course2 = "python programmer"

print(course2.upper())
print(course2.lower())

# title() - convert first letter of every word to upper case
print(course2.title())


course3 = "   python programmer   "

print(course3)
print(course3.strip())
print(course3.lstrip())


# find()- to get index of a char or a sequence of chars in your string

print(course3.find("pro"))

# Python is case sensitive
# returns  -1 if the string is not found in original string
print(course3.find("Pro"))


# replace()- to replce a char or seq. of chars with something else

print(course3.replace("p", "j"))


# in operator - checks for the existence of a char / sequence of chars in string
print("pro" in course3)

# not in operator - checks to see if our string doestno contain a char or sequence of chars in string
print("swift" not in course3)

# numbers

print(10-3)  # 7
print(10+3)  # 13
print(10*3)  # 30
print(10/3)  # 3.333333333
print(10//3)  # 3
print(10 % 3)  # 1
print(10**3)  # 1000

# augmented assignment operator

x = 10
x = x+3
x += 3  # augmented assignment operator


# working with numbers

print(round(2.9))  # 3
print(round(2.3))  # 2
print(abs(-2.9))  # 2.9


print(math.ceil(2.2))  # 3


# type covnversion

# input() - to get input frm the user, as a arg we pass  string this will be label that will be displayed in the terminal.
# x = input("x: ")

# print(type(x))
# y = x+1
# print(y)

# to solve this prob, we need to convert string 1 to number

y = int(x) + 1
print(f"x:{x}, y:{y}")


# FALSY VALUES : "", 0, None - any values other than these are truthy values

bool(0)  # false
bool(-1)  # true
bool(3)  # true
bool("")  # false
bool("false")  # true


# primitive types in python  -  string, numbers - it can be (integer, float,complex) boolean

fruit = "Apple"
print(fruit[1])

print(fruit[1:-1])
