star=input()
lst=star.split(" ")
word=star
temp=0
lst1=["zero","one","two","three","four","five","six","seven","eight","nine","ten"]
for i in range(0,10):
    for j in lst:
        if(j==str(i)):
            print(j) 
            word=word.replace(j,lst1[i])
print(word)



