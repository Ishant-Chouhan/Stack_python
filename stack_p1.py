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
            newnode=self.top
            self.top=newnode

        if self.top==")" or "}" or "]" and self.top.link!=None:
            self.top=self.top.link
    
    def check_top(self):
        if self.top==None:
            print("**************---Parenthesis are correct**************")
        else:
            print("**************Parenthesis are not correct**************")

s=stack()
string=input("Enter parenthesis: ")
if (len(list(string))==1) or (len(list(string))==2 and (string!="{}" or "()" or "[]")):
    print("**************Parenthesis are not correct**************")
elif (string=="{}" or "()" or "[]") and (len(list(string))==2):
    print("**************Parenthesis are correct**************")
for i in string:
    print(i)
    s.check_parenthesis(node(i))

s.check_top()