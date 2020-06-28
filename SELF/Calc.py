class Calc:
    def multiply(x,y):
        return x*y
    def add(x,y):
        return x+y
    def sub(x,y):

        
        return x-y
    def div(x,y):
        return x/y
    while True:
        first=int(input("Enter the number"))
        second=int(input("Enter seconf number"))
        doin=input("Enter the operation")
        if(doin=="+"):
            print(add(first,second))
