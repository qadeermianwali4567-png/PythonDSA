class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class FloydAlgorithm:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
            self.tail = temp
            self.tail.next = self.head
        else:
            self.tail.next = temp
            self.tail = temp
            self.tail.next = self.head.next.next

    def display(self):
        curr = self.head
        if curr is None:
            print("List is empty")
            return
        while curr!=None:
            print(curr.data, end="->")
            curr = curr.next
            # if curr == self.head:
            #     break

    def isCircleExist(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    def findMeetingPoint(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
        return None
    def findStartOfLoop(self):
        meeting_point = self.findMeetingPoint()
        if meeting_point is None:
            return None
        start = self.head
        while start != meeting_point:
            start = start.next
            meeting_point = meeting_point.next
        return start
    def findEndOfLoop(self):
        meeting_point = self.findMeetingPoint()
        if meeting_point is None:
            return None
        startofloop = self.findStartOfLoop()
        if startofloop is None:
            return None
        end = startofloop
        while end.next != startofloop:
            end = end.next
        return end
    def removeLoop(self):
        endofloop = self.findEndOfLoop()
        if endofloop is not None:
            endofloop.next = None
floyd=FloydAlgorithm()
floyd.insert(10)
floyd.insert(20)
floyd.insert(30)
floyd.insert(50)
floyd.insert(60)
floyd.insert(70)

print(floyd.isCircleExist())
print(floyd.findMeetingPoint().data)
print(floyd.findStartOfLoop().data)
print(floyd.findEndOfLoop().data)
floyd.removeLoop()
floyd.display()