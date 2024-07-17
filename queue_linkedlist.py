# queue implimentation using linked list
#defining class node
class node:
    def __init__(self,data):
        self.data=data
        self.link=None

#defining class queue
class queue:
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self,data):#defining enqueue operation 
        if self.front==None and self.rear==None:
            self.front=data
            self.rear=data
        else:
            self.rear.link=data
            self.rear=self.rear.link
        return "Element Successfully Inserted...!!"
        
    def dequeue(self):#defining dequeue operation
        if self.front==None:
            return "Queue Underflow...!!"
        else:
            self.front=self.front.link
            return "Element is successfully deleted...!!"
        
    def frontend(self):#defining front operation to display front element
        if self.front==None:
            return "Queue Is Empty...!!"
        else:
            return self.front.data
        
    def rearend(self):#defining rearend operation to display last element
        if self.front==None:
            return "Queue Is Empty...!!"
        else:
            return self.rear.data
        
    def display(self):#defining display operation to print queue
        if self.front==None:
            print("Queue Is Empty...!!")
        else:
            temp=self.front
            while temp!=None:
                print(temp.data)
                temp=temp.link

q=queue()#creating object for class queue
while True:
    print("""press 1 perform enqueue operation
press 2 to perform dequeue operation
press 3 to display front element
press 4 to display last element
press 5 to display queue
press any other key to exit""")
    choice=int(input("Enter your choice: "))
    if choice==1:
        print(q.enqueue(node(int(input("Enter: ")))))
    elif choice==2:
        print(q.dequeue())
    elif choice==3:
        print(q.frontend())
    elif choice==4:
        print(q.rearend())
    elif choice==5:
        q.display()
    else:
        print("Exit...")
        break