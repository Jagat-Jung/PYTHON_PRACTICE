
def fac(i):
	if(i<2):
		return i
	else:
		return i*fac(i-1)
r=fac(5)
print(r)
