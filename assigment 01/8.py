
# Write a Python program that will return true if the two given integer 
# values are equal or their sum or difference is 5.


a=int(input("enter the first number : "))
b=int(input("enter the second number : "))

if a==b or abs(a-b)==5 or a+b==5:
    result=True
    print(result)

else:
    result=False
    print(result)