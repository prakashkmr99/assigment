#Write a python program to sum of the first n positive integers

n=int(input("Enter Number Upto which you want to calculate Sum of positive integers :- "))
sum=0
for i in range(1,n+1):
    print(i)
    
    if i>0:
        sum+=i
print()        
print("Sum of positive integers = ",sum)  