Numbers=input("Enter the numbers using spaces in between")
NumberList=Numbers.split(' ')
NumberSet=set(NumberList)
for i in NumberSet:
    print("The numbers of ",i," in the list is" ,NumberList.count(i))
