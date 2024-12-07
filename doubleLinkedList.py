class Node:
    def __init__(self,item):
        self.__data=item
        self.__next=None
        self.__previous=None
        
    @property
    def getData(self):
        return self.__data
    def setData(self,item):
        self.__data=item
        
    @property
    def getNext(self):
        return self.__next
    def setNext(self,newNext):
        self.__next=newNext
        
    @property
    def getPrevious(self):
        return self.__previous
    def setPrevious(self,newPrev):
        self.__previous=newPrev
        
class DlinkedList:
    def __init__(self):
        self.__head=None
        self.__last=None
        
    def __str__(self):
        current=self.__head
        list=[]
        while current != None:
            list.append(current.getData)
            current=current.getNext
        return str(list)
    
    def __iter__(self):
        current=self.__head
        list=[]
        while current != None:
            list.append(current.getData)
            current=current.getNext
        return iter(list)
    
    def __len__(self):
        current=self.__head
        count=0
        while current != None:
            current=current.getNext
            count+=1
        return count

    @property
    def getFirst(self):
        return self.__head.getData
    @property
    def getLast(self):
        return self.__last.getData
    @property
    def isEmpty(self):
        if self.__last ==None and self.__head==None:
            return True
        return False
    
    def insertAtBeggin(self,data):
        item=Node(data)
        if self.isEmpty:
            self.__head=item
            self.__last=item
            return
        current=self.__head
        item.setNext(current)
        current.setPrevious(item)
        self.__head=item
        
    def insertAtEnd(self,data):
        item=Node(data)
        if self.isEmpty:
            self.__head=item
            self.__last=item
            return
        current=self.__last
        item.setPrevious(current)
        current.setNext(item)
        self.__last=item
        
    def insert(self,data,pos:int):
        if pos<0 or pos > len(self):
            return "Invalid position"
        elif pos==0:
            self.insertAtBeggin(data)
            return
        elif pos == len(self):
            self.insertAtEnd(data)
            return
            
        item=Node(data)
        current=self.__head
        count=0
        while count < pos-1:
            current=current.getNext
            count+=1
        item.setNext(current.getNext)
        item.setPrevious(current)
        temp:Node=current.getNext
        temp.setPrevious(item)
        current.setNext(item)
        
    def deleteLast(self):
        if self.isEmpty:
            return "The list is empty!"
        elif len(self)==1 and self.__head==self.__last:
            self.__head=None
            self.__last=None
            return
        current=self.__last
        prev:Node=current.getPrevious
        prev.setNext(None)
        self.__last=prev
        
    def deleteFirst(self):
        if self.isEmpty:
            return"The list is empty!"
        elif len(self)==1 and self.__head ==self.__last:
            self.__head=None
            self.__last=None
            return
        current=self.__head
        next:Node=current.getNext
        next.setPrevious(None)
        self.__head=next
        
    def deleteData(self,data):
        if self.isEmpty:
            return "The list is empty!"
        current=self.__head
        while current.getData !=data:
            current=current.getNext
        if current==self.__head:
            self.deleteFirst()
            return
        elif current==self.__last:
            self.deleteLast()
            return
        next:Node=current.getNext
        prev:Node=current.getPrevious
        next.setPrevious(prev)
        prev.setNext(next)
        