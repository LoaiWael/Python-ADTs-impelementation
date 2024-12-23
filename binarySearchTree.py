class BST:
    
    # The case of making the node inside the main class itself for making it private
    class __Node:
        def __init__(self,data):
            self.data=data
            self.rightChild=None
            self.leftChild=None
        def __str__(self):
            return str(self.data)
        
    def __init__(self):
        self.__root=None
    
    @property
    def isEmpty(self):
        return self.__root==None
    @property
    def getRoot(self):
        if self.isEmpty:
            raise Exception("Tree is empty!")
        return self.__root.data
    @property
    def getMin(self):
        if self.isEmpty:
            raise Exception("Tree is empty!")
        current=self.__root
        while current.leftChild:
            current=current.leftChild
        return current.data
    @property
    def getMax(self):
        if self.isEmpty:
            raise Exception("Tree is empty!")
        current=self.__root
        while current.rightChild:
            current=current.rightChild
        return current.data
    
    def __find(self,item):
        current=self.__root
        parent=None
        while current and item !=current.data:
            parent=current
            current=current.rightChild if item>current.data else current.leftChild
        return(current,parent)
    
    def insert(self,item):
        node,parent=self.__find(item)
        if node:
            return False
        node=self.__Node(item)
        if parent == None:
            self.__root=node
        elif parent.data >item :
            parent.leftChild=node
        elif parent.data<item:
            parent.rightChild=node
    
    def inOrderT(self,function=print):
        if self.isEmpty:
            raise Exception("Tree is empty!")
        self.__inOrderT(node=self.__root,function=function)
        
    def __inOrderT(self,node,function):
        if node:
            self.__inOrderT(node.leftChild,function)
            function(node)
            self.__inOrderT(node.rightChild,function)
            
    def preOrderT(self,function=print):
        if self.isEmpty:
            raise Exception("Tree is empty!")
        self.__preOrderT(node=self.__root,function=function)
        
    def __preOrderT(self,node,function):
        if node:
            function(node)
            self.__preOrderT(node.leftChild,function)
            self.__preOrderT(node.rightChild,function)
            
    def postOrderT(self,function=print):
        if self.isEmpty:
            raise Exception("Tree is empty!")
        self.__postOrderT(node=self.__root,function=function)
        
    def __postOrderT(self,node,function):
        if node:
            self.__postOrderT(node.leftChild,function)
            self.__postOrderT(node.rightChild,function)
            function(node)