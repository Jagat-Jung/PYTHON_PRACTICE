import string
wwe=list(string.ascii_lowercase)
star=input()
star=star.casefold()
temp=""
for i in range(len(star)):
    if(star[i]==" "):
        temp=temp+star[i]
    else:
        temp=temp+wwe[(25-wwe.index(star[i]))]
      
print(temp)

