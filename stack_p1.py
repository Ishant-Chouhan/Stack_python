#parenthesis checker
class node:
    def __init__(self,data):
        self.data=data
        self.link=None
    
class stack:
    def __init__(self):
        self.top=None

    def check_parenthesis(self,newnode):
        if self.top==None:
            self.top=newnode
        else:
            newnode.link=self.top
            self.top=newnode

        while True:
            print("________________")
            print("while: ",self.top.data)
            if (self.top=="}" and self.top.link=="{" ) or (self.top=="]" and self.top.link=="[" ) or (self.top==")" and self.top.link=="(" ):
                self.top=self.top.link.link
            else:
                break
                
        # if self.top==")" or "}" or "]" and self.top.link!=None:
        # self.top=self.top.link.link
    
    def check_top(self):
        print("check_top: ",self.top)
        if self.top==None:
            print("**************---Parenthesis are correct**************")
        else:
            print("**************Parenthesis are not correct**************")

    def display(self):
        current=self.top
        while current!=None:
            print(current.data)
            current=current.link

s=stack()
string=input("Enter parenthesis: ")

if (len(list(string))==1) or (len(list(string))==2 and (string!="{}" or "()" or "[]")):
    print("**************Parenthesis are not correct**************")
elif (string=="{}" or "()" or "[]") and (len(list(string))==2):
    print("**************Parenthesis are correct**************")
else:
    for i in string:
        print(i)
        s.check_parenthesis(node(i))
    s.check_top()
s.display()