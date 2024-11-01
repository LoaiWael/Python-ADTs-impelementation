class Set:
    def __init__(self):
        self.__set=["init"]
        self.__index=-1
    def __str__(self):
        return str(self.__set)

    def __len__(self) :
        return len(self.__set)
    
    def __iter__(self):
        return iter(self.__set)

    def add(self,element):
        for n in self.__set:
            if n is element:
               return "Element is already exists"
        if self.__index==-1 and self.__set[0]=="init" :
            self.__index+=1
            self.__set[self.__index]=element
        else:
            self.__set.append(element)

    def remove(self,element):
        for n in self.__set:
            if n is element:
                self.__set.remove(element)
                self.__index-=1
                return
        if self.__set[0]=="init" and self.__index==-1:
            return "The set is empty!"
        else:
            return "This element is not included"
            
    def contains(self,element):
        for n in self.__set:
            if n==element:
                return True
        return False
            
    def equals(self,otherSet):
        if type(otherSet)!=Set:
            return "Invalid data type."
        elif len(self.__set)!=len(otherSet):
            return False
        else:
            for i in self.__set:
                if i not in otherSet:
                    return False
            return True
    def subset_of(self,otherSet):
        if type(otherSet)!=Set:
            return "Invalid data type."
        else:
            for i in self.__set:
                if i not in otherSet:
                    return False
            return True

    def union(self,otherSet):
        if type(otherSet)!=Set:
            return "Invalid data type."
        
        unionSet=self.__set.copy()
        for i in otherSet:
            if i in self.__set:
                continue
            else:
                unionSet.append(i)
        return unionSet
    
    def intersect(self,otherSet):
        if type(otherSet)!=Set:
            return "Invalid data type."
        
        intersectSet=[]
        for i in self.__set:
            if i in otherSet:
                intersectSet.append(i)
        return intersectSet
    
    def difference(self, otherSet):
        if type(otherSet)!=Set:
            return "Invalid data type."
        
        differenceSet=self.__set.copy()
        for i in self.__set:
            if i in otherSet:
                differenceSet.remove(i)
        return differenceSet
    
