#stack
l=[]
while True:
    print("""press 1 to perform push operation
press 2 to pop the element
press 3 to peek 
press to 4 to display
press a other key to exit.""")
    choice = int(input("Enter your choice: "))
    if choice==1:
        l.append(int(input("Enter element: ")))
        print("Successfully inserted...!!")
    elif choice==2:
        if l==[]:
            print("stack is already empty...!!")
        else:
            l.pop()
            print("Successfully deleted...!!")
    elif choice==3:
        print(l[len(l)-1])
    elif choice==4:
        print("____________STACK____________")
        print(l)
    else:
        break