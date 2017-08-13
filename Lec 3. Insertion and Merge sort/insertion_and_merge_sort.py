"""
Created on Aug 12, 2017

@author: Evan Burton

################################################
#            Sorting problem:                  #
#      Want to sort a list efficiently.        #
################################################

Sorting:

    Ex. Want to find a median for unsorted data.
        If we can get a fast sorting algorithm,
        then this problem would be solved in
        sorting time + constant time.
        
    Ex. Binary search: Quck searching if the
        list is sorted.

    Other applications:
        - Computer graphics
        - Compression
        
        
################################################
#              Insertion Sort                  #
################################################


For i = 1, 2, ... n
    insert A[i] into sorted array A[0:i-1]
    
    by pairwise swaps down to correct position.
    
Ex. [5, 2, 4, 6, 1, 3]
        ^
    swap 5,2
    
    [2, 5, 4, 6, 1, 3]
           ^
    swap 5,4
    
    [2, 4, 5, 6, 1, 3]
              ^
    no swap
    
    [2, 4, 5, 6, 1, 3]
                 ^
    swap 6,1
    swap 5,1
    swap 4,1
    swap 2,1
    
    [1, 2, 4, 5, 6, 3]
                    ^
    swap 6,3
    swap 5,3
    swap 4,3
    
    [1, 2, 3, 4, 5, 6]
    
"""

# Runs in Theta(n^2) time at worst case
def insertion_sort(A):
    if len(A) <= 1:
        return A

    # i is position ptr of array, Theta(n)
    for i in range(0, len(A)-1):
        
        j = i+1
        
        # bubble back least elements, Theta(n)
        while A[j] < A[j-1] and j > 0:
            
            # swap
            temp = A[j]
            A[j] = A[j-1]
            A[j-1] = temp
            
            j-=1
    
A = [5, 2, 4, 6, 1, 3]

print(A)
insertion_sort(A)
print(A)