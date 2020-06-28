odd=[]
even=[]
for i in range(1,201):
    if i%2 is not 0:
        odd=odd+[i]
    else:
        even=even+[i]
print("Odd=",odd)
print("Even=",even)