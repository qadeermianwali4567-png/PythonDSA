
class HashTable:
    def __init__(self,size):
       
        self.size=size
        self.table=[[] for i in range(size)]
    def insert(self,value):
        index=self.Hashfunction(value)
        # if(self.table[index] is not None):
        #     print("Collision Occured")
        #     return
        self.table[index].append(value)
    def Hashfunction(self,value):
            return hash(value)%self.size
    def display(self):
        for i in range(self.size):
            print(i,":",self.table[i])
hashtable=HashTable(10)
hashtable.insert(23)
hashtable.insert(600)
hashtable.insert(142)
hashtable.insert(100)
hashtable.insert(23)
hashtable.insert(600)
hashtable.insert(142)   
hashtable.insert(100)
hashtable.insert(26)
hashtable.insert(23)
hashtable.insert(670)
hashtable.insert(189)
hashtable.insert(107)
hashtable.insert(29)
hashtable.insert(603)
hashtable.insert(142)   
hashtable.insert(101)
hashtable.insert(27)
hashtable.insert(25)
hashtable.insert(606)
hashtable.insert(147)
hashtable.insert(108)
hashtable.insert(29)
hashtable.insert(603)
hashtable.insert(145)   
hashtable.insert(107)
hashtable.insert(23)
hashtable.insert(231)
hashtable.insert(602)
hashtable.insert(149)
hashtable.insert(104)
hashtable.insert(25)
hashtable.insert(600)
hashtable.insert(142)   
hashtable.insert(100)
hashtable.insert(26)
hashtable.display()