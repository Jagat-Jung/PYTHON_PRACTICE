Number=input("Enter the numbers of list with space in between")
NumberList=(Number.split(' '))
OddNumbers=[ ]
EvenNumbers=[ ]
for i in NumberList:
    if(int(i)%2)==0:
        EvenNumbers.append(i)
    
    else:
        OddNumbers.append(i)

print("Odd Numbers in the list are: ", OddNumbers)

print("Even Numbers in the list are: ", EvenNumbers)
