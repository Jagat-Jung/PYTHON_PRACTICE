Number=int(input("Enter the number to find factorial"))
fact=1
if Number==0:
    print("Factorial of the number is 1")

elif Number<0:
    print("We cannot find factorial of negative value")
    
for i in range(1,Number+1):
    fact=fact*i
print("factorial of the number is", fact)



