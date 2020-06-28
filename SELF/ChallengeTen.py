star=input("Enter the input")
i=0
for j in range(len(star)):
    if((star[j]=="o")|(star[j]=="O")):
        i=i+1
print(i)