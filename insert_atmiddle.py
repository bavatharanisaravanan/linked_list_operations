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
    def inbetween(self,middle_node,newnodeval):
        newnode=node(newnodeval)
        if middle_node is None:
            print("the mentioned node is already present ")
            return
        newnode=node(newnodeval)
        newnode.nextval=middle_node.nextval
        middle_node.nextval=newnode
list1=linked_list()
list1.headval=node(10)
e2=node(12)
e3=node(1999)
list1.headval.nextval=e2
e2.nextval=e3
list1.inbetween(list1.headval.nextval,"friday")
list1.listprint()



