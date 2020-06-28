str='python'
print(str[1])
abb=''
for i in range(1,len(str)+1):
    abb=abb+str[i*-1]
print(abb)
#another metho
print(str[::-1])