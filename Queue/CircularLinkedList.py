class Node:
    def __init__(self,data):
      self.data=data 
      self.next=None
class CircularLinkedList:
    def __init__(self):
      self.head=None
      self.tail=None
    def insert(self,data):
      temp=Node(data)
      if(self.head==None):
        self.head=temp
        self.tail=temp
        self.tail.next=self.head
      else:
        self.tail.next=temp
        self.tail=temp
        self.tail.next=self.head
    def display(self):
        curr=self.head
        if(curr==None):
              print("List is empty")
              return
        while(True):
            print(curr.data,end="->")
            curr=curr.next
            if(curr==self.head):
                break
    def isCircleExist(self):
        slow=self.head
        fast=self.head
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
            if(slow==fast):
                return True
        return False
cll=CircularLinkedList()
cll.insert(10)
cll.insert(20)
cll.insert(30)
cll.insert(50)
cll.insert(60)
cll.insert(70)
cll.display()
print()
print(cll.isCircleExist())