class LinkedList:
    
    def __init__(self):
        # initialize empty LinkedList
        self.arr = []
        self.size = 0
    
    def get(self, index: int) -> int:
        # return value of LinkedList[index]
        #if index is == size or < 0 
            #return -1
        if(index >= self.size or 
            index < 0):
            return -1
        return self.arr[index]
        

    def insertHead(self, val: int) -> None:
        #insert LinkedList[0] = val
        self.arr = [val] + self.arr
        self.size += 1

    def insertTail(self, val: int) -> None:
        #insert LinkedList[size] = val
        self.arr = self.arr + [val]
        self.size += 1

    def remove(self, index: int) -> bool:
        #if index is == size or < 0 
            #return false
        #remove at LinkedList[index]
        #return true
        if(index >= self.size or
            index < 0):
            return False

        firstHalf = self.arr[0:index]
        self.arr = firstHalf + self.arr[index+1:self.size]
        self.size -= 1

        return True

    def getValues(self) -> List[int]:
        return self.arr
