
# loops - there are times that we may want to repeat a task no of times - eg we wanna send msg to user. if that msg cant be delivered
# perhaps we wann retry 3 times ..use lopops to create repitition


# for loop:

# for number in range(3):
#     print("Attempt", number + 1, (number+1) * ".")


# passing args to start from 1 to 4 , 4 is excluded

# for number in range(1, 4):
#     print("Attempt", number, number * ".")


# passing 3rd arg step

# for number in range(1, 10, 2):
#     print("Attempt", number, number * ".")


# for else

# successful = True
# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("Successful")
#         break


# if we never break put of this loop then the else stmnt will be executed
# successful = False
# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("Successful")
#         break
# else:
#     print("Attempeted 3 times & failed")


# if we break out of loop , else stmnt will not be executed
# bcz we terminate the loop with break, what we hve inside the else block will not be executed
successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempeted 3 times & failed")


# Nested loops - we can put one loop inside another loop

# prints co-ordinates

# for x in range(5):  # outer loop
#     for y in range(3):  # inner loop
#         print(f"({x}, {y})")


# Iterables :

# print(type(5))

# print(type(range(5)))


# range is one of the complex types
# for x in range(5):
#     print(x)


# strings are also iterables  - primitive type
# for x in "Python":
#     print(x)


# Lists are also iterbales  - it is complex type

# for x in [1, 2, 3, 4]:
#     print(x)


# While loop: to repeat something as long as the condition is true

# number = 100
# while number > 0:
#     print(number)
#     number //= 2


# while loop - real world example

# command = ""
# while command != "quit":
#     command = input(">")
#     print("ECHO", command)


# no matter how the user types, the word quit will always terminate the program.
# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)


# Infinite loops

# while True:
#     command = input(">")
#     print("ECHO", command)
#     if command.lower() == "quit":
#         break


# Exercise  -pront even no from 1 -10

count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"we have {count} even numbers")
