# Write a Python program to get a single string from two given strings, 
# separated by a space and swap the first two characters of each string.

a=input("Enter First String :- ")
b=input("Enter Second String :- ")


if len(a) >= 2 and len(b) >= 2:
    c=b[:2] + a[:2] + ' ' + a[:2] + b[:2]
    print("After Swap = ",c)
else:
    print("Both String length should be greater than 2")    
    