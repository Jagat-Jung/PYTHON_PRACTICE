from random import randint
while True:
    star=input("1. Scissors \n2. Pappers \n3. Rocks \nEnter your choice ")
    here=["Scissors","Pappers","Rocks"]
    ran=here[(randint(0,2))]
    print("The computer's choice",ran)
    if(star==ran):
        print("Draw")
    elif(star=="Scissors" and ran=="Pappers"):
        print("you won")
    elif(star=="Rocks" and ran=="Scissors"):
        print("you won")
    elif(star=="Papers" and ran=="Rocks"):
        print("you won")
    else:
        print("you losed")