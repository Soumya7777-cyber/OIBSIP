A=int(input("A = "))
B=input("Enter the operator: ")
C=int(input("B = "))
print(f"The answer of {A} {B} {C} = ",end="")
if(B=="+"):
    print(A+C)
elif(B=="-"):
    print(A-C)
elif(B=="/"):
    print(A/C)
elif(B=="*"):
    print(A*C)
else:
    print("your input operator is wrong!")