'''
0 is for Rock
1 is for Paper
2 is for Scissors 
 '''
import random
computer=random.choice([0,1,2])
younum=input("Enter your option:")
youdict={"rock":0,"paper":1,"scissors":2}
you=youdict[younum]# your inputed value(like 0,1,2) store in to the younum
revdict={0:"rock",1:"paper",2:"scissors"}
print(f"you choose {younum}")
print(f"computer choose {revdict[computer]}")
if(computer==you):
    print("it is draw")
else:
    if((computer-you)==-1 and (computer-you)==2):
        print("you win !")
    else:
        print("computer Win !")
    # if(computer==0 and you==1):
    #     print("you win !")
    # elif(computer==0 and you==2):
    #     print("computer win !")
    # elif(computer==1 and you==0):
    #     print("computer win !")
    # elif(computer==1 and you==2):
    #     print("you win !")
    # elif(computer==2 and you==0):
    #     print("you win !")
    # elif(computer==2 and you==1):
    #     print("computer win !")
    # else:
    #     print("Somthing Error !")