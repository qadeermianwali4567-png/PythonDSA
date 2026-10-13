from logging import root


class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
class BinaryTree:
    def __init__(self):
        self.root=None
    def insert(self,root,data):
        if(root==None):
            return Node(data)
        if(data<root.data):
            root.left=self.insert(root.left,data)
        else:
            root.right=self.insert(root.right,data)
        return root
       
    def preorder(self, root):
       if root is None:
        return
       print(root.data,"->",end="")
       self.preorder(root.left)
       self.preorder(root.right)
    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data,"->",end="")
    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data,"->",end="")
        self.inorder(root.right)
            
       
        
bt=BinaryTree()
bt.root=bt.insert(bt.root,6)
bt.root=bt.insert(bt.root,4)
bt.root=bt.insert(bt.root,8)
bt.root=bt.insert(bt.root,2)
bt.root=bt.insert(bt.root,5)
bt.root=bt.insert(bt.root,7)
bt.root=bt.insert(bt.root,9)
bt.root=bt.insert(bt.root,3)
print("Preorder Traversal of Binary Tree is:",end="")
bt.preorder(bt.root)
print()
print("Postorder Traversal of Binary Tree is:",end="")
bt.postorder(bt.root)
print()
print("Inorder Traversal of Binary Tree is:",end="")
bt.inorder(bt.root)
print()