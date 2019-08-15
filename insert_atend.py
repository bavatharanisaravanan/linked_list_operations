class node:
    def __init__(self,dataval):
        self.dataval=dataval
        self.nextval=None
class linked_list:
    def __init__(self):
        self.headval=None
    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval,end=" ")
            printval=printval.nextval
    def atend(self,newnodeval):
        newnode=node(newnodeval)
        if self.headval is None:
            self.headval=newnode
            return
        last=self.headval
        while(last.nextval):
            last=last.nextval
        last.nextval=newnode    
list1=linked_list()
list1.headval=node(10)
e2=node(12)
e3=node(1999)
list1.headval.nextval=e2
e2.nextval=e3
list1.atend("friday")
list1.listprint()


