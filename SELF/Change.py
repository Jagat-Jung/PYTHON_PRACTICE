data=input("Enter the string")
temp=""
change=""
print("String before change",data)
for i in range(len(data)):
    temp=data[i]
    if (temp.islower()):
        temp=data[i].capitalize()   
    else:
        temp=data[i].casefold()     
    change=change+temp
print(change)