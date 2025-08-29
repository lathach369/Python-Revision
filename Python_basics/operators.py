
# # conditional operators
# 10 > 3
# 10 >= 3
# 10 < 20
# 10 <= 20
# 10 == 10
# 10 == '10'


# conditional statements

# temperature = 30

# if temperature > 20:
#     print("Drink hot water")
#     print("fill up the bottle")
# print("done")


# elif, else

temperature = 15

if temperature > 30:
    print("Drink hot water")
    print("fill up the bottle")
elif temperature > 20:
    print("its nice")
else:
    print("its cold")
print("done")


# Ternary operator
# age = 22
# if age >= 18:
#     print("Eligible")
# else:
#     print("not eligible")


# age = 22
# if age >= 18:
#     message = "Eligible"
# else:
#     message = "not eligible"
# print(message)


age = 22
message = "Eligible" if age >= 18 else "not eligible"
print(message)


# logical operator:

# high_income = True
# good_credit = True
# student = True
# if high_income and good_credit:
#     print("eligible")
# else:
#     print("not eligible")


# not operator

# high_income = True
# good_credit = True
# student = True
# if not student:
#     print("eligible")
# else:
#     print("not eligible")


# high_income = True
# good_credit = True
# student = False
# if not student:
#     print("eligible")
# else:
#     print("not eligible")


# high_income = False
# good_credit = False
# student = False
# if (high_income or good_credit) and not student:
#     print("eligible")
# else:
#     print("not eligible")


high_income = True
good_credit = False
student = False
# short circuiting: evaluation stops as soon as one of thr args evaluates to false
# python intreprter sees thsi exprsn it knows that good_credit is false,
# so it doesnt  matter what comes after, the result  of this will always be false bcz one of the operands is false
if high_income and good_credit and not student:

    print("eligible")
else:
    print("not eligible")


# Chaining comparison operators

# age should be between 18 and 65
age = 22
if 18 <= age < 65:
    print("eligible ")
