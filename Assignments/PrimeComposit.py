Number=int(input("Enter the number to find if it is prime or composit"))
flag=0
if Number== (0 or 1):
    print("Number is neither prime nor composit")  

for i in range(2,int(Number/2)):
    if(Number%i)==0:
        flag=flag+1;

if(flag==0):
    print("The number is prime")
else:
    print("The number is composit")


   
           
        







    
