
# printing syntax of python

print("hello world")

print(3+10)
# print("51"+13) -->  type error


# variable declaration 
 
name = "harsh"
age = 25 
salary = 26000.00

# checking the variable type 

print(type(name))
print(type(age))
print(type(salary))


# Data types
 
# Integer 
# String 
# Float 
# Boolean
# None

# types of tokens 
# ()
# {}
# @
# #

# types of language
# 1] Implicit --> python ---> no need to  write datatype
# 2] Explicit ---> java c++  ---> need to  write  return type


# Expresion Excution
#1] String and numeric value operate together with *

A,B = 2,3
C = "txt"
print(A*C*B)
# output :txttxttxttxttxttxt  <==   2*text == txttxt   3*txt ==txttxttxt

# 2] String & String operate with + 
X,Y = "2",4
Z = "@"
print((X+Z)*Y)
# output:2@2@2@2@   (X+Z) --> 2@   & (2@)*Y -->2@2@2@2@ 
# + -->concat with 2 String  

# 3] Numeric value can return with all  arthmatic opertors 
# +,-,/,* 
p,q,r = 2,4,3
add = p+q*r
print(add)

# 4] Arithmatic expresion with integer and  float  with result float
PQ,RS = 6.5,3
print(PQ+RS)   
# int + float  = float

# 5] Result of two  division operator is float
k,l = 1,2
m = k/l 
print(m)

# 6] Integer Division with float  and int will give int displayed as float (//)
h,g = 3.5,2
s =h//g
print(s)

# floor(Integer Division) // gives nearest integer
# 2.4 --> 2
# 3.7 --> 4
#-2.4 -->-3


