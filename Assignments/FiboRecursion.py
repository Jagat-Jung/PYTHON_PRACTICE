def fibo(num):
   if num <= 1:
       return num
   else:
       return(fibo(num-1) + fibo(num-2))

number=int(input("Enter the number to find the recursion"))

if(number<0):
    print("Number is negative and negative number doesnot have fibonacci series")

else:
    print("The fibo series are")
    print(list(map(fibo,range(1,number+1))))