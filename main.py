import random

computer=random.choices([1,2,3])
compint=computer[0]
youstr=input("Enter what you chose (stone: st, paper: p, scissor: sc) ")
youdict={"st":1, "p":2, "sc": 3}
you=youdict[youstr]
compdict={1:"st", 2:"p", 3:"sc"}

print(f"Computer chose {compdict[compint]} \nYou chose {compdict[you]}")


if(compint==you):
    print("Its a draw")
else:
    if(compint==1 and you==2):          
        print("You win")
    elif(compint==1 and you==3):
        print("You lose")
    elif(compint==2 and you==1):
        print("You lose")
    elif(compint==2 and you==3):
        print("You win")
    elif(compint==3 and you==1):
        print("You win")
    elif(compint==3 and you==2):
        print("You lose")
    else:
        print("Something went wrong")



