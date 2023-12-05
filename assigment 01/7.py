# Write a Python program to sum of three given integers. However, if
#two values are equal sum will be zero


num1=int(input("Enter first number : "))
num2=int(input("Enter Second number : "))
num3=int(input("Enter Third number : "))

if num1==num2 or num2==num3 or num3==num1:
    sum_result=0
    print("the sum is zero : ")
else:
    sum_result=num1+num2+num3
    print("the sum is",sum_result)