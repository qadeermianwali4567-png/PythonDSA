class Node:
    def __init__(self,data):
        self.data =data
        self.next=None
class SingleLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert_at_begenning(self,data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode
        if self.tail is None:
            self.tail=newNode
    def insert_at_end(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
    def display(self):
        current=self.head
        while current!=None:
            if(current.next!=None):
                print(current.data,end="->")
            else:
                print(current.data)
            current=current.next
    def delete_at_begenning(self):
        if self.head is None:
            print("List is empty")
            return
        self.head=self.head.next
        if self.head is None:
            self.tail=None
    
sll=SingleLinkedList()
sll.insert_at_begenning(40)
sll.insert_at_begenning(30)
sll.insert_at_begenning(20)
sll.insert_at_begenning(10)
sll.insert_at_end(50)
sll.insert_at_end(60)
sll.insert_at_end(70)
sll.delete_at_begenning()
sll.delete_at_begenning()
sll.delete_at_begenning()   
sll.delete_at_begenning()
sll.delete_at_begenning()   
sll.delete_at_begenning()   
sll.delete_at_begenning()
sll.delete_at_begenning()   
sll.display()
