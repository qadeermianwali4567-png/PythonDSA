class HashTable:
    def __init__(self,size):
        self.size=size
        self.table=[None]*size
    def insert(self,key,value):
        index=self.Hashfunction(key)
        if(self.table[index] is not None):
            print("Collision Occurs!")
            return
        self.table[index]=(key,value)
    def get(self,key):
        index=self.Hashfunction(key)
        print(self.table[index])
    def Hashfunction(self,value):
         return hash(value)%self.size
    def delete(self,key):
        index=self.Hashfunction(key)
        self.table[index]=None
hashtable=HashTable(10)
hashtable.insert("age",23)

hashtable.insert("marks",600)
hashtable.insert("address","mianwali")
hashtable.insert("name","Aslam")
print(hashtable.table)
hashtable.delete("name")
hashtable.get("age")
hashtable.get("name")
hashtable.delete("name")
print(hashtable.table)