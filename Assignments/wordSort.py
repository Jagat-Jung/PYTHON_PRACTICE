NumberOfWords=int(input("Enter the number of words to sort"))
NameList=[]
for i in range(NumberOfWords):
    word=str(input("Enter the word"))
    NameList=NameList+[word]
NameList.sort()
print(NameList)