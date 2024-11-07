class Queue:
    def __init__(self,maxSize: int):
        while type(maxSize)!=int:
            raise Exception("invalid max size.")
        self.__maxSize=maxSize
        self.__queue=[None]*self.__maxSize
        self.__front=0
        self.__rear=-1
        self.__numOfItems=0
        
    def __str__(self):
        return str(self.__queue)
    
    def __iter__(self):
        return iter(self.__queue)
    
    def __len__(self):
        return len(self.__queue)
    
    @property
    def Get_numOfItems(self):
        return self.__numOfItems
    
    @property
    def Get_front(self):
        return self.__queue[self.__front]
    
    @property
    def Get_rear(self):
        return self.__queue[self.__rear]
    
    @property
    def Get_Available_Space(self):
        return self.__maxSize - self.__numOfItems
    
    def enqueue(self,element):
        if self.__numOfItems==self.__maxSize :
            return "The queue is full!"
        self.__rear=(self.__rear+1)%self.__maxSize
        self.__queue[self.__rear]=element
        self.__numOfItems+=1
        
    def dequeue(self):
        if self.__numOfItems==0:
            return "The queue is empty!"
        temp=self.__queue[self.__front]
        self.__queue[self.__front]=None
        self.__numOfItems-=1
        self.__front=(self.__front+1)%self.__maxSize
        return temp
    
    def isEmpty(self):
        return self.__numOfItems==0
    
    def isFull(self):
        return self.__numOfItems==self.__maxSize
    
    def clear(self):
        self.__front=0
        self.__rear=-1
        self.__numOfItems=0
        for i in range(len(self.__queue)):
            self.__queue[i]=None
    