'''
Created on Aug 12, 2017

@author: Evan Burton
'''
################################################
# We want to find a local peak if it exists.   #
################################################

################################################
#           Straightforward Approach           #
#     Compare each element to previous peak    #
################################################

# Theta(n) algorithm
def find_peak_naive(a):
    
    peak_index = 0
    
    for i in range(1, len(a)):
        if a[i] > a[peak_index]:
            peak_index = i
            
    return peak_index

################################################
"""              
Recursive Approach:

Look at list[n/2] and compare to neighbors,
    list[n/2] > list[n/2-1] => check left list
    list[n/2] < list[n/2+1] => check right list
    list[n/2] is maximal    => found peak

    Work done by algorithm: compute for subarray 
    plus the comparisons:
    
    T(n) = T(n/2) + Theta(1)
         = Theta(1) + ... + Theta(1)
           ^ log(n) times ^
         = Theta(log(n)) 
    
"""
################################################

def find_peak(a, start, end):
    if len(a[start:end]) == 1:
        return start
    elif len(a[start:end]) == 2:
        if a[start] > a[start+1]:
            return start
        else:
            return start+1
    
    k = int(len(a[start:end])/2)
    
    
    
    if a[k] < a[k-1]:
        return find_peak(a, start, k)
    if a[k] < a[k+1]:
        return find_peak(a, k, end)
    else:
        return k
    
"""
################################################
#                2D Peak Finding               #
################################################

a is a peak if a is greater than its neighbors in NSEW dirs.
   _ c _
   b a d
   _ e _
     
Greedy Ascent Algorithm: Theta(nm) complexity

    Pick a direction and exhaust it as long as a < b,
    Then pick another direction and exhaust it similarly.


    14 13 12
    15  9 11 17
    16 17 19 20

    Starting from 12: 
    
    12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 19 -> 20

################################################
Divide and Conquer: Theta(n log(m))

    Pick middle column j = m/2
    Find a 1D peak at (i, j) => log(m)
    Use (i, j) as start to find 1D peak on row i => log(n)
    
    But this doesn't work because a 2D peak may not exist
    on row i.

    Ex. 
          10
    14 13 12
    15  9 11 17
    16 17 19 20
    
    Starting from 12: 12 -> 13 -> 14

    Attempt 2:
    
    Pick middle column j = m/2
    Find global max on column j at (i, j)
    Compare (i, j-1), (i, j), (i, j+1)
    Pick left columns if (i, j-1) > (i, j)
        Similarly for right side
    If (i, j) >= (i,j-1) and (i, j+1)
        Then (i, j) is a 2D peak
################################################

"""

def find_peak_2D(a):
    if len(a) == 1:
        return (0, find_peak(a[0], 0, len(a[0])))
    
    j = int(len(a[0])/2)
    
    max_index = 0
    
    # find global max in column j, Theta(n)
    for i in range(len(a)):
        if a[i][j] > a[max_index][j]:
            max_index = i
    
    # find 1D peak in row i, Theta(log(m))
    return (max_index, find_peak(a[max_index], 0, len(a[i])))


a = [[14, 13, 12],
     [15, 99, 11],
     [1, 14, 32],
     [1, 11, 12]]

for i in range(len(a)):
    print(a[i])

print("peak at " + str(find_peak_2D(a)))

    