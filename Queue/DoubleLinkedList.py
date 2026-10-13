class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class DoubleLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertAtBeggining(self,data):
        temp=Node(data)
        if(self.head==None):
            self.head=temp
            self.tail=temp
            return
        temp.next=self.head
        self.head.prev=temp
        self.head=temp
    def insertAtEnd(self,data):
        temp=Node(data)
        if(self.head==None):
            self.head=temp
            self.tail=temp
            return
        self.tail.next=temp
        temp.prev=self.tail
        self.tail=temp
    def insertAfter(self,pos,value):
        curr=self.head
        if(curr==None):
            print("List is empty")
            return
        while(curr.data!=pos):
            curr=curr.next
        print(curr.data)
        newNode =Node(value)
        temp=curr.next
        if(temp==None):
            curr.next=newNode
            newNode.prev=curr
            self.tail=newNode
            return
        newNode.next=temp
        
        temp.prev=newNode
        curr.next=newNode
        newNode.prev=curr
       
    def deleteAtBeggening(self):
        if(self.head==None):
            print("List is empty")
            return
        self.head=self.head.next
        if(self.head==None):
            print("List is empty")
            self.tail=None
        else:
            self.head.prev=None
    def deleteAtEnd(self):
        if(self.head==None):
            print("List is empty")
            return
        self.tail=self.tail.prev
        if(self.tail==None):
            print("List is empty")
            self.head=None
        else:
            self.tail.next=None
    def display(self):
        curr=self.head
        while(curr!=None):
            if(curr.next==None):
                print(curr.data,end='')
            else:
                print(curr.data,"->",end='')
            curr=curr.next
        print()
dll=DoubleLinkedList()
dll.insertAtBeggining(50)
dll.insertAtBeggining(40)
dll.insertAtBeggining(30)
dll.insertAtBeggining(10)
dll.insertAtBeggining(5)
dll.insertAtEnd(60)
dll.insertAtEnd(70)
dll.insertAtEnd(80)
dll.insertAtEnd(90)
dll.insertAfter(70,75)
dll.insertAfter(80,85)
dll.display()
dll.deleteAtBeggening()
dll.deleteAtBeggening()
dll.deleteAtBeggening()
dll.deleteAtBeggening()
dll.deleteAtBeggening()
dll.deleteAtBeggening()
dll.deleteAtEnd()
dll.deleteAtEnd()
dll.deleteAtEnd()
dll.deleteAtEnd()
dll.deleteAtEnd()
print("After deleting from beginning:")
dll.display()