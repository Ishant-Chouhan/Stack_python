#stack
l=[]
while True:
    print("""press 1 to perform push operation
press 2 to pop the element
press 3 to peek 
press to 4 to display
press a other key to exit.""")
    #giving options to the user to perform different operations
    choice = int(input("Enter your choice: "))
    if choice==1:
        #PUSH
        l.append(int(input("Enter element: ")))
        print("Successfully inserted...!!")
    elif choice==2:
        #POP
        if l==[]:#checking stack underflow condition
            print("stack is already empty...!!")
        else:
            l.pop()
            print("Successfully deleted...!!")
    elif choice==3:
        #peek
        print(l[len(l)-1])
    elif choice==4:
        #displaying stack
        print("____________STACK____________")
        print(l)
    else:
        break