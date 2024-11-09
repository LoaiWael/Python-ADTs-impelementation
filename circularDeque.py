class Deque:
    def __init__(self,maxSize: int):
        while type(maxSize)!=int:
            raise Exception("invalid max size.")
        self.__maxSize=maxSize
        self.__deque=[]*self.__maxSize
        self.__front=0
        self.__rear=-1
        self.__numOfItems=0
        
    def __str__(self):
        return str(self.__deque)
    
    def __iter__(self):
        return iter(self.__deque)
    
    def __len__(self):
        return len(self.__deque)
    
    @property
    def Get_numOfItems(self):
        return self.__numOfItems
    
    @property
    def Get_front(self):
        return self.__deque[self.__front]
    
    @property
    def Get_rear(self):
        return self.__deque[self.__rear]
    
    @property
    def Get_Available_Space(self):
        return self.__maxSize - self.__numOfItems
    
    def insert_Left(self,element):
        if self.__numOfItems==self.__maxSize :
            return "The Deque is full!"
        elif self.__front!=0:
            self.__front+=1
        self.__rear=(self.__rear+1)%self.__maxSize
        self.__deque.insert(self.__front,element)
        self.__numOfItems+=1
        
    def insert_Right(self,element):
        if self.__numOfItems==self.__maxSize :
            return "The Deque is full!"
        self.__rear=(self.__rear+1)%self.__maxSize
        self.__deque.insert(self.__rear,element)
        self.__numOfItems+=1
        
    def remove_Left(self):
        if self.__numOfItems==0:
            return "The Deque is empty!"
        elif self.__front==-1:
            self.__front+=1
        self.__deque.remove(self.__deque[self.__front])
        self.__rear=(self.__rear-1)%self.__maxSize
        self.__numOfItems-=1
        
    def remove_Right(self):
        if self.__numOfItems==0:
            return "The Deque is empty!"
        elif self.__rear==-1:
            self.__rear+=1
        self.__deque.remove(self.__deque[self.__rear])
        self.__rear=(self.__rear-1)%self.__maxSize
        self.__numOfItems-=1
        
    def isEmpty(self):
        return self.__numOfItems==0
    
    def isFull(self):
        return self.__numOfItems==self.__maxSize
    
    def clear(self):
        self.__front=0
        self.__rear=-1
        self.__numOfItems=0
        for i in range(len(self.__deque)):
            self.__deque[i]=None 
            