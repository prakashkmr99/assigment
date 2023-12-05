#Write a Python program to count occurrences of a substring in a string.

main=input("Enter Main String :- ")
sub=input("Enter Sub String :- ")


count=main.count(sub)

print(" {} occurs {} times in the string".format(sub,count))