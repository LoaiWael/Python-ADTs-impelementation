class Node:
    def __init__(self,datum):
        self.__datum=datum
        self.__next=None
    
    @property
    def getData(self):
        return self.__datum
    
    def setData(self,newDatum):
        self.__datum=newDatum
        
    @property
    def getNext(self):
        return self.__next
    
    def setNext(self,newNext):
        if newNext==None or isinstance(newNext,Node):
            self.__next=newNext
        else:
            raise Exception("Invalid next input, next must be node or none")
        
class LinkedList:
    def __init__(self):
        self.__head=None
        
    def __str__(self):
        strList=[]
        current=self.__head
        if self.__head is None:
            return str(strList)
        while current.getNext != None:
            strList.append(current.getData)
            current=current.getNext
        strList.append(current.getData)
        return str(strList)
    
    def __iter__(self):
        iterList=[]
        current=self.__head
        if self.__head is None:
            return str(iterList)
        while current.getNext != None:
            iterList.append(current.getData)
            current=current.getNext
        iterList.append(current.getData)
        return iter(iterList)
        
    
    def insertAtBegginnig(self,item):
        temp=Node(item)
        temp.setNext(self.__head)
        self.__head=temp
    
    def remove(self,item):
        current=self.__head
        previous=None
        found =False
        while not found:
            if current.getData==item:
                found=True
            previous=current
            current=current.getNext
        if previous==None:
            self.__head=current.getNext
        else:
            previous.setNext(current.getNext)
            
    def append(self,item):
        newNode=Node(item)
        current=self.__head
        if self.__head ==None:
            self.insertAtBegginnig(item)
            return
        while current.getNext != None:
            current=current.getNext
        current.setNext(newNode)
        
    def insert(self,item,pos:int):
        if pos>self.getSize or pos<0:
            return "invalid position"
        elif pos == 0:
            self.insertAtBegginnig(item)
            return
        
        current=self.__head
        count=0
        while count < pos-1:
            current=current.getNext
            count+=1
        
        newNode=Node(item)
        newNode.setNext(current.getNext)
        current.setNext(newNode)
        
    
    def search(self,item):
        current=self.__head
        found=False
        while current is not None and not found:
            if current.getData==item:
                found=True
            else:
                current=current.getNext
        return found
    
    def clear(self):
        self.__head=None
    
    @property
    def isEmpty(self):
        return self.__head==None
    
    @property
    def getSize(self):
        current=self.__head
        count=0
        while current != None:
            count+=1
            current=current.getNext
        return count
