import random 
str='Y'
choices=['paper','scissor','rock']
numchoices=[0,1,2]
while(str=='Y'):
    print("enter 1 for paper ,2 for scissor and 3 for rock")
    a=int(input())
    b=random.choice(numchoices)
    a-=1
    print("YOU ----->",choices[a])
    print("COMPUTER------>",choices[b])
    if(b==a):
        print("TIE")
        
    if(b>a and b-a<=1 and b!=a):
        print("The Computer wins")
    else :
        if(b!=a):
            print("YOU WIN")
    print("Do you want to continue Y or N")
    str=input().upper()
    


    