import time
print(".............PLEASE INSERT YOUR CARD..............")
time.sleep(4)
password=2580
balance=60000
l=[]
i=1
while (i<4):
    if(i==3):
            print("it is your final try,so please put your password very carefully. Otherwise you block for today !")
    A=int(input("ENTER YOUR 4 DIGIT PIN: "))

    if (password==A):
        while True:
            print('''
                 ********* MAIN MENU ************
               *     Enter 1 : Balance Inquiry    *
             *       Enter 2 : Withdrawl            *
           *         Enter 3 : Deposit                *
         *           Enter 4 : Pin Change               *
       *             Enter 5 : Transuction History         *
    *                Enter 6 : Exit or Goto the Main Menu    *
   ************************************************************
                    ''')

            option=int(input("Please enter Your choice:"))
            if (option==1 or option==2 or option==3 or option==4 or option==5 or option==6):
                    # for balance inquiry
                    if(option==1):
                        print("Your current balance is:")
                        print(balance)
                    # for withdrawl money
                    elif(option==2):
                        X=int(input("Enter the amount:"))
                        if(balance>X):
                            print("Your current balance is :")
                            balance=balance-X
                            print(balance)
                        else:
                             print("Insufficient balance !")
                        l.append(f"{X} rs debited from your account")
                    # for add money 
                    elif(option==3):
                        Y=int(input("Enter the amount:"))
                        print("Please insert your cash in ATM machine")
                        balance=balance+Y
                        print(f"{Y} rupee successfully add in your account !")
                        print("Your current balance is :")
                        print(balance)
                        l.append(f"{Y} rs credited in your account ")
                    # for pin change
                    elif(option==4):
                         Z=int(input("Enter your previous 4 Digit Pin:"))
                         if(password==Z):
                              V=int(input("Please Enter the new 4 Digit Pin:"))
                              password=V

                         else:
                              print("Your entered pin is wrong !")
                    elif(option==5):
                         print("**********Your last Transuctions are: *********** ")
                         L=len(l)
                         i=0
                         while(i<L):
                              print(l[i])
                              i=i+1
                    elif(option==6):
                        break
        

            else:
                 print(" Please enter the valid option !")
            
    else:
        print("Your entered pin is wrong please try again !")
        print(" ")
        if(i==3):
             print("Try after 24 hours ")
        i=i+1