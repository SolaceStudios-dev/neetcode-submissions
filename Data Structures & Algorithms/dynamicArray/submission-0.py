class DynamicArray:
    
    def __init__(self, capacity: int):
        #if capacity > 0
            #logic
        #else
            #reject
        if capacity > 0:
            self.capacity = capacity
            self.size = 0
            self.arr = [0] * self.capacity
        else:
            print("please enter capacity greater than 0\n")


    def get(self, i: int) -> int:
        #we want get an element at index i from DynamicArray
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        #we want set an element at index i in DynamicArray
        self.arr[i] = n
        return None

    def pushback(self, n: int) -> None:
        #we insert element n at the end of DynamicArray
        #if DynamicArray is full
        #  we resize the array
        if(self.size == self.capacity):
            self.resize()

        self.arr[self.size] = n
        self.size += 1
        



    def popback(self) -> int:
        #we want delete the element at the end of DynamicArray and return it
        retValue = self.arr[self.size - 1]
        self.arr[self.size - 1] = 0
        self.size -= 1
        return retValue
 

    def resize(self) -> None:
        #double capacity of DynamicArray
        self.capacity *= 2
        self.arr = self.arr + [0] * (self.capacity // 2)


    def getSize(self) -> int:
        #return number of elements of DynamicArray
        return self.size
        
    
    def getCapacity(self) -> int:
        #get capacity of DynamicArray
        return self.capacity
