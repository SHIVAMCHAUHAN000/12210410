
import random
s=0
while True:
    x=int(input("Enter intial range: "))
    y=int(input("Enter final range: "))
    if x ==0 and y==0:
        print("Game Over!!!")
        break
    z=random.randint(x,y+1)
    n=int(input("Enter the Number: "))
    c=0
    i=1
    while i<=3:
        if n>z and i<3:
            print("HAVE ONE MORE TRY AND YOUR CHOICE WAS TOO HIGH.")
            n=int(input("Enter the number again:"))
        elif n<z and i<3:
            print("HAVE ONE MORE TRY AND YOUR CHOICE WAS TOO LOW.")
            n=int(input("Enter the number again: "))
        elif i==3 and n!=z:
            print("Better luck next time!!!")
        else:
            print("!!!CONGRATS!!!")
            c+=1
            s+=1
        i+=1
    print("SCORE:",c)
    print("Final Score: ",s              )
