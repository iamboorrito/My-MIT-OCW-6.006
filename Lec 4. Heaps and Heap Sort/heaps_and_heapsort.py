"""
Created on Aug 12, 2017

@author: Evan

################################################
#            Heaps and Priority Queue          #
################################################

Priority Queue: a set of elements S with each element
                associated with a key.
           0 1 2 3 4 5 6 7 8 
    list: [9 8 7 6 5 4 3 2 1]
    As a heap:
                     9
                   8   7
                 6  5 4  3
                2 1 

Properties:
    parent(i) = i/2
    left(i) = 2*i
    right(i) = 2*i+1

The Max Heap Property: The key of a node is >=
    the keys of its children

         16
       4    10
    14  7  9  3
   2 8
   
Not a max heap because of 4 < 14. 
     
################################################
#                Heaps Sort                    #
################################################

Algorithm:

        1. build_max_heap() from unsorted array
        2. Find max element A[0]
        3. Swap A[end] and A[0]
        4. Discard A[end], decrement heap size
        5. New root may violate MHP, but children are max
           heaps. Call max_heapify(0) to  fix.
        6. GOTO 2 till heap is empty  

"""
class Heap():
    def __init__(self, list=[]):
        self.list = list
        self.size = len(list)
    def __str__(self):
        return str(self.list)
        
    # Returns the index of left child if it exists, 
    # otherwise returns -1
    def left(self, i):
        
        if 2*i+1 >= self.size:
            return -1
        
        return 2*i+1
    
    # Returns the index of right child if it exists, 
    # otherwise returns -1
    def right(self, i):
        
        if 2*i+2 >= self.size:
            return -1
        
        return 2*i+2
    
    # Assumes the trees rooted at left(i) and
    # right(i) are max heaps and corrects one
    # violation of Max Heap Property.
    def max_heapify(self, i):
        
        if self.size == 0:
            return
        
        left = self.left(i)
        right = self.right(i)
        
        # no error to fix
        if self.list[i] > self.list[left] and self.list[i] > self.list[right]:
            return
        
        max = left
        
        # At leaf
        if left == right == -1:
            return
        # Choose max key of children
        elif left != -1 and right != -1:
            if self.list[right] > self.list[left]:
                max = right
        else:
            if left == -1:
                max = right
        # swap max and i nodes
        temp = self.list[i]
        self.list[i] = self.list[max]
        self.list[max] = temp
        # Recur to fix any damages from swap
        self.max_heapify(max)
        
    # Turns self.list into a max heap
    def build_max_heap(self):
        
        mid = int(self.size/2)
            
        for i in reversed(range(mid)):
            self.max_heapify(i)
             
    # Destroys self.list and returns sorted array in 
    # descending order.
    def heap_sort(self):
        
        sorted = [0]*self.size
        
        self.build_max_heap()
        i = 0
        
        while self.size > 0:
            # swap A[0] and A[end]
            temp = self.list[0]
            self.list[0] = self.list[self.size-1]
            del self.list[self.size-1]
            sorted[i] = temp
            i+=1
            self.size -= 1
            # Correct MHP violation
            self.max_heapify(0)
        
        return sorted
        
a = [7, 3, 8, 5, 4, 1, 2, 6]

print('unsorted: '+str(a))
heap = Heap(a)
print('sorted:   '+ str(heap.heap_sort()))

