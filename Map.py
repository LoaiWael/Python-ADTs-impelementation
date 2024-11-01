from BinarySearch import binarySearch

class Map:

     def __init__(self):
        self.__key=['init']
        self.__value=['init']
        self.__mapIndex=-1

     def __len__(self):
        return len(self.__value)
    
     def __str__(self):
         di={}
         for n in range(len(self.__key)):
              UPDdi={self.__key[n]:self.__value[n]}
              di.update(UPDdi)
         return str(di)
     
     def __iter__(self):
          li=[]
          for n in range(len(self.__key)):
               li.append(f"{self.__key[n]}: {self.__value[n]}")
          return iter(li)
    
     def add(self,key: int,*values):
        while type(key) != int:
             return "invalid key. Please enter an int number"
        
        liValues=list(values)
        if len(self.__key)==1 and self.__key[0]=='init':
                self.__mapIndex+=1
                self.__key[self.__mapIndex]=key
                self.__value[self.__mapIndex]=liValues
        elif key in self.__key :
             self.__mapIndex=binarySearch(self.__key,key)
             self.__value[self.__mapIndex]=liValues
        else:
            self.__key.append(key)
            self.__value.append(liValues)

     def append(self,key: int,*values):
        while type(key) != int:
             return "invalid key. Please enter an int number"
        
        liValues=list(values)
        if len(self.__key)==1 and self.__key[0]=='init':
                self.__mapIndex+=1
                self.__key[self.__mapIndex]=key
                self.__value[self.__mapIndex]=liValues
        elif key in self.__key :
             self.__mapIndex=binarySearch(self.__key,key)
             innerlist=self.__value[self.__mapIndex]
             for n in liValues:
                innerlist.append(n)
        else:
            self.__key.append(key)
            self.__value.append(liValues)

     def remove_Key(self,key: int):
          while type(key) != int:
             return "invalid key. Please enter an int number"
          if key not in self.__key:
               return "Key is not included."
          elif len(self.__key)==1 and self.__key[0]=='init':
               return "The map is empty"
          elif key in self.__key:
               self.__mapIndex=binarySearch(self.__key,key)
               self.__key.remove(self.__key[self.__mapIndex])
               self.__value.remove(self.__value[self.__mapIndex])

     def remove_Values(self,key: int,*values):
          while type(key) != int:
             return "invalid key. Please enter an int number"

          liValues=list(values)
          if key not in self.__key:
               return "Key is not included."
          elif len(self.__key)==1 and self.__key[0]=='init':
               return "The map is empty"
          elif key in self.__key:
               self.__mapIndex=binarySearch(self.__key,key)
               innerlist=self.__value[self.__mapIndex]
               for n in liValues:
                    if n not in innerlist:
                         print(f"The value {n} is not included")
                         continue 
                    else:
                         innerlist.remove(n)

     def values_Of(self,key: int):
          while type(key) != int:
             return "invalid key. Please enter an int number"
          if key not in self.__key:
               return "Key is not included."
          elif len(self.__key)==1 and self.__key[0]=='init':
               return "The map is empty"
          else:
               self.__mapIndex=binarySearch(self.__key,key)
               return self.__value[self.__mapIndex]

