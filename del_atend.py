class node:
    def __init__(self,dataval):
        self.dataval=dataval
        self.nextval=None
class linked_list:
    def __init__(self):
        self.headval=None
    def delatend(self):
        prev=self.headval
        while prev.nextval is not None:
            end=prev
            prev=prev.nextval
        end.nextval=None
    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval
list1=linked_list()
list1.headval=node(10)
e2=node(12)
e3=node(1999)
list1.headval.nextval=e2
e2.nextval=e3
list1.delatend()
list1.listprint()


