#Queue
l=[]
while True:
    print("""press 1 to perform Enqueue operation
press 2 to Dequeue the element
press 3 to display Frontend
press 4 to display Rearend 
press 5 to display
press any other key to exit.""")
    #giving options to the user to perform different operations
    choice = int(input("Enter your choice: "))
    if choice==1:
        #Enqueue
        l.append(int(input("Enter element: ")))
        print("Successfully inserted...!!")
    elif choice==2:
        #Dequeue
        if l==[]:#checking queue underflow condition
            print("stack is already empty...!!")
        else:
            l.pop(0)
            print("l.pop(0) is Successfully deleted...!!")
    elif choice==3:
        #display front
        print(l[0])
    elif choice==4:
        #display last element
        print(l[len(l)-1])
    elif choice==5:
        #displaying stack
        print("____________QUEUE____________")
        print(l)
    else:
        break