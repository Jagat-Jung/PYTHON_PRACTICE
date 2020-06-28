number=int(input("Enter the number of items in list"))
lst=[]
while number>0:
    num=int(input("Enter the number"))
    lst=lst+[num]
    number=number-1

print(list(filter(lambda x:x%2==0,lst)))
