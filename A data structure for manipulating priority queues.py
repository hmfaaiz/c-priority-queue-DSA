
# # Project : A data structure for manipulating priority queues (3rd Semester) 


class PriorityQueue:
    def __init__(self,size):
        self.size = size
        self.data = [0 for i in range(size)]
        self.rear = 0
                  
    def IsEmpty(self):
        if self.rear<1:
            return True
        else:
            return False
        
    def IsFull(self):
        if self.rear>=self.size:
            return True
        else:
            return False
        
    def Enqueue(self,v):
        if self.IsFull()==True:
            return "Overflow"
        else:
            self.data[self.rear]=v
            self.rear=self.rear+1
        
        
    def DequeueWithHighetPriority(self):
        if self.IsEmpty()==True:
            return "Underflow"
        else:
            a = self.max_heap()
            b = self.data[0]
            self.data[0] = self.data[self.rear-1]
            self.data[self.rear-1] = 0
            self.rear=self.rear-1
            return b

    def DequeueWithLowestPriority(self):
        if self.IsEmpty()==True:
            return "Underflow"
        else:
            self.min_heap()
            r = self.data[0]
            self.data[0] = self.data[self.rear-1]
            self.rear = self.rear-1
            return r
        
    def max_heap(self):
        self.length=self.rear
        c=int(self.length/2)-1
        for i in range(c,-1,-1):
            z = self.__heapify(i)
            
    def min_heap(self):
        self.length = self.rear
        size = int(self.length//2)
        for i in range(size,-1,-1):
             self.__minheapify(i)
    
    def __heapify(self,i):
        l=2*i+1
        r=2*i+2
        if(l<=self.rear and self.data[l]>=self.data[i]):
            largest=l
        else:
            largest=i
         
        if r<self.rear:
            if(r<=self.rear and self.data[r]>=self.data[largest]):
                largest=r
    
        if self.data[largest]!=self.data[i]:
            self.data[i],self.data[largest]=self.data[largest],self.data[i]
            self.__heapify(i)
    
    def __minheapify(self,i):
        l=2*i
        r=2*i+1
        if (l<=self.rear and self.data[l]<=self.data[i]):
            smallest = l
        else:
            smallest = i
        
        if r<self.rear:
            if (r<=self.rear and self.data[r]<=self.data[smallest]):
                smallest = r
        if self.data[smallest] != self.data[i]:
            self.data[i],self.data[smallest] = self.data[smallest],self.data[i]
            self.__minheapify(i)
            
    def Print(self):
        for i in range(self.rear):
            print(self.data[i])

#Driver Code
obj=PriorityQueue(5)
obj.Enqueue(55)
obj.Enqueue(2)
obj.Enqueue(45)
obj.Enqueue(100)
obj.Enqueue(35)

print("\t\tPriority Queue")
print("Before Deletion")
obj.Print()
print("\nDequeue With Lowest Priority Queue:")

print(obj.DequeueWithLowestPriority())
print(obj.DequeueWithLowestPriority())

print("\nDequeue With Highest Priority Queue")
print(obj.DequeueWithHighetPriority())
print(obj.DequeueWithHighetPriority())
print("After deletion")
obj.Print()









