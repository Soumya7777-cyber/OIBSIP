todo=[]
print("-----------Welcome to your to-do list------------")
A=int(input("How many no. of task you want to add in todo list:"))
for i in range(1,A+1):
    task_name=input(f"Enter the {i} task:")
    todo.append(task_name)
print(todo)
while(True):
    operation=int(input("Enter \n1:for Add\n2:for Remove\n3:for Update\n4:for View\n5:for Exit"))
    if(operation==1):
        B=input("Enter the task:")
        todo.append(B)
        print("Your task is add successfully")
    
    elif(operation==2):
        C=input("Enter the task you want to remove from to-do list:")
        if C in todo:
            ind=todo.index(C)
            del todo[ind]
        else:
            print("Your entered task is not present in this to-do list !")
    elif(operation==3):
        D=input("Enter the task which one you want to change:")
        if D in todo:
            N=input("Enter the new task:")
            ind=todo.index(D) 
            todo[ind]=N
    elif(operation==4):
        print(f"Your to-do list is{todo}")
    elif(operation==5):
        print("Thank you !")
        break
    else:
        print("you enter wrong input !")