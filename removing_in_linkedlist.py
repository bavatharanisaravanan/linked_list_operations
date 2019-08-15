class node:
    def __init__(self,data):
        self.dataval=data
        self.nextval=None
class linked_list:
    def __init__(self):
        self.head=None
    def removenode(self,removekey):
        headval=self.head
        if self.head is None:
            return
        while self.head is not None:
            if self.head.dataval==removekey:
                 self.head=self.head.nextval
                 headval=None
                 return
            prev=headval.nextval
            if prev.dataval==removekey:
                prev=self.head.nextval
                self.head.nextval=prev.nextval
                self.head.nextval=None
                self.head=headval
    def printt(self):
        while self.head is not None:
            print(self.head.dataval)
            self.head=self.head.nextval
list1=linked_list()
list1.head=node(12)
e2=node(14)
e3=node(1999)
list1.head.nextval=e2
e2.nextval=e3
list1.removenode(14)
list1.printt()

