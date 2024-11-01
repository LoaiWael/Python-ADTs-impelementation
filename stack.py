class Stack:

    def __init__(self,max):
        while type(max)!=int:
            return "Invalid size or input type. Please enter the size of the stack correctly."
        self.__stack=[0]*max
        self.__top=-1

    def __str__(self):
        return str(self.__stack)
    
    def __len__(self):
        return len(self.__stack)
    
    def __iter__(self):
        return iter(self.__stack)
    
    def peek(self):
        return self.__stack[self.__top]
    
    def push(self,num):
        if self.__top == len(self.__stack)-1:
            return "The stack is full!"
        else:
            self.__top+=1
            self.__stack[self.__top]=num

    def pop(self):
        if self.__top == -1:
            return "The stack is empty!"
        else:
            temp=self.__stack[self.__top]
            self.__stack[self.__top]=0
            self.__top-=1
            return temp
    