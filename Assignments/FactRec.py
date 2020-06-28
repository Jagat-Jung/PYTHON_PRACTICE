def recursion(num):
    if(num==0 or num==1):
        return 1

    else:
        return num*recursion(num-1)

number=int(input("Enter the number to find its recursion"))

print("the factorial is ",recursion(number))
    