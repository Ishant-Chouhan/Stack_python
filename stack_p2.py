#How to Reverse a String using Stack
class node:
    def __init__(self,data):
        self.data=data
        self.link=None

class stack:
    def __init__(self):
        self.top=None

    def push(self,newnode):
        if self.top==None:
            self.top=node(i)
        else:
            node(i).link=self.top
            self.top=node(i)
        print(self.top.data)


    
    def reverse(self):
        current=self.top
        s=""
        while current!=None:
            s=current.data+s
            current=current.link
        print(s)
    
s=stack()
str="ishant"
for i in str:
    s.push(node(i))

s.reverse()