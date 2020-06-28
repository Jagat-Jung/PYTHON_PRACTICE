Number=str(input("Enter your birthdate in yyyy/mm/dd form"))
Number=Number.replace('/','')
lst=str(22/7)
lst=lst.replace('.','')
print(lst)
if (lst.find(Number))==0:    
    print("There is birthdate in pi")

else:
    print("There is no birthday in pi")