def addition(a,b):
    return (a+b)

def subraction(a,b):
    return(a-b)

def multiply(a,b):
    return(a*b)

def divide(a,b):
    return(a/b)

print("Press \n1.Addiction \n2.Subtraction \n3.Multiply \n4.Divide \n5.exit")

choice=int(input())

if choice==5:
        SystemExit()


elif choice<1 or choice>5:
    print("Wrong input f choice")

else:
    first_variable=int(input("Enter the first variable"))
    second_variable=int(input("Enter the second variable"))

    if choice==1:
        print(addition(first_variable,second_variable))

    elif choice==2:
        print(subraction(first_variable,second_variable))

    elif choice==3:
        print(multiply(first_variable,second_variable))

    elif choice==4:
        print(divide(first_variable,second_variable))
