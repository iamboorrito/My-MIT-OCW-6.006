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

"""

################################################
#                 Merge Sort                   #
################################################

         [       A       ]
         [       ][      ]
         [  ][  ] [  ][  ]
         [ ] [ ]  [ ] [ ]
         []  []   []  []
         
         Merge singletons and empty lists
         
         [    sorted A    ]
         
         20 12
         13 11
          7  9
          2  1    take 1, keep finger on 2
                  take 2, keep finger on 9
                  take 7, keep finger on 9
                  take 9, keep finger on 13
                  take 11, ... 13
                  
                  1 2 7 9 11 13
        
"""

def merge_sort(A):

    if len(A) <= 1:
        return A
    elif len(A) == 2:
        if A[0] > A[1]:
            temp = A[0]
            A[0] = A[1]
            A[1] = temp
        return A
    else:
        
        mid = int((len(A))/2)
        left = merge_sort(A[0:mid])
        right = merge_sort(A[mid:len(A)])
        
        return merge(left, right)

def merge(A, B):
    
    left = right = 0
    length_A = len(A)
    length_B = len(B)
    result = [0]*(length_A+length_B)
    i = 0

    # Two finger method
    while i < length_A+length_B:
        if A[left] <= B[right]:
            result[i] = A[left]
            left+=1
            i+=1
            
        else:
            result[i] = B[right]
            right+=1
            i+=1
        if left == length_A or right == length_B:
            for j in range(left, length_A):
                result[i] = A[j]
                i+=1
            for j in range(right, length_B):
                result[i] = B[j]
                i+=1
            break
        
    return result