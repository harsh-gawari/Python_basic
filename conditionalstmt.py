# conditional statement  -> condition base 

# 1] if-else
# syntax:
# if(condition):
#     statement 
#     .........
# elif(condition):
#     statement
# else:
#     statement

# note :indentionerror avoid : after 4 spaces write statement start with if near 

# example:Write a Python program to check whether a number is positive or negative.

num =int(input("Enter the number :"))
if(num > 0):
    print(num,"is Positive")
elif(num < 0):
    print(num,"is Negative")
else:
    print(num,"no Positive nor Negative")

# example:Check whether a person is eligible to vote or not.

age =int(input("Enter the age :"))

if(age > 18):
    print("person can able to  vote")
else:
    print("person can not able to vote")

#example :Take marks from the user and print:

# 90+ → Grade A
# 60–89 → Grade B
# 40–59 → Grade C
# Below 40 → Fail 

marks = int(input("Eneter the marks :"))

if(marks >= 90  and marks < 100 ):
    print("Grade A")
elif(marks >= 60 and marks <=89 ):
    print("Grade B")
elif(marks >= 40 and marks <=59 ):
    print("Grade c")
else:
    print("fail")
    