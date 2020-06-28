star=input("Enter the string")
lst=star.split(" ")
temp=" "
for i in lst:
    if(len(temp)<len(i)):
        temp=i
        print(temp)
print(temp)
    

