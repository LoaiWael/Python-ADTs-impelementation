class Queue:
    def __init__(self,max):
        self.__maxSize=max
        self.__queue=[None]*self.__maxSize
        self.__front=0
        self.__rear=-1
        self.__numOfItems=0
        
    def __str__(self):
        return str(self.__queue)
    def __contains__(self, item):
        return item in self.__queue
    def __len__(self):
        return len(self.__queue)
    def __iter__(self):
        return iter(self.__queue)
    
    @property
    def isFull(self):
        return self.__numOfItems==self.__maxSize
    @property
    def isEmpty(self):
        return self.__numOfItems==0  
    @property
    def Get_Available_Space(self):
        return self.__maxSize - self.__numOfItems
    
    def enqueue(self,item):
        if self.isFull:
            raise Exception("Queue is full!")
        self.__rear=(self.__rear+1)%self.__maxSize
        self.__queue[self.__rear]=item
        self.__numOfItems+=1
        
    def dequeue(self):
        if self.isEmpty:
            raise Exception("Queue is empty!")
        reee=self.__queue[self.__front]
        self.__queue[self.__front]=None
        self.__front=(self.__front+1)%self.__maxSize
        self.__numOfItems-=1
        return reee
    
    def peek(self):
        return self.__queue[self.__front]
    