#STACK USING LINKEDLIST
#defining a class node
class node:
    def __init__(self,data):
        self.data=data
        self.link=None

class stack:#defining class for stack
    def __init__(self):
        self.top=None

    def push(self,data):#adding puch operation
        if self.top==None:
            self.top=data
        else:
            temp=self.top
            while temp.link!=None:
                temp=temp.link
            temp.link=data
    
    def pop(self):#adding pop operation
        if self.top==None:
            return "Stack underflow"
        else:
            self.top=self.top.link
            return "successfully deleted...!!"

    def peek(self):#adding peek operation
        if self.top==None:
            return "Stack is empty...!!"
        else:
            return self.top.data
    
    def display(self):#adding operation to print the stack
        if self.top==None:
            print("stack is empty...!!")
        else:
            temp=self.top
            while temp!=None:
                print(temp.data)
                temp=temp.link
s=stack()#creating object of class stack        
while True:
    print("""press 1 to peform push operation
press 2 to perform pop operation
press 3 to perform peek operation
press 4 to display the stack
press any other key to exit""")
    choice=int(input("Enter your choice: "))
    if choice==1:
        s.push(node(int(input("Enter number: "))))
    elif choice==2:
        print(s.pop())
    elif choice==3:
        print(s.peek())
    elif choice==4:
        s.display()
    else:
        print("Exit...")
        break