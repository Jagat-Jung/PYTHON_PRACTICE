def fact(x):
    sum=1
    for i in range(1,x+1):
        sum=sum*i
    return sum
x=int(input("Enter the number to find the factorial "))
x=fact(x)
print(x)
        
