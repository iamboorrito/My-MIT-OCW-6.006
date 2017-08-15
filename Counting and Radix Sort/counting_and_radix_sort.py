"""
Created on Aug 13, 2017

@author: Evan Burton

################################################
#             Comparison Model                 #
################################################

Restrict operations to comparisons:
    - All input items are black boxes
    - Only allowed <, >, ==, etc
    - Time cost = # of comparisons

Decision tree: Comparison algorithms can be viewed
as a tree of all possible comparisons and their 
outcomes.

Ex. Binary Search, n = 3

                A[1] < x?
            NO            YES
       A[0] < x ?        A[2] < x?
    NO         YES
 x <= A[0]  A[0] < x <= A[1]
 
---------------------------------------------------- 
Decision Tree      |      Algorithm                |
----------------------------------------------------
internal node   <---->    binary decision (compare)|
leaf            <---->    found answer             |
root->leaf      <---->    algorithm execution      |
path length     <---->    running time             |
height of tree  <---->    worst case runtime       |
----------------------------------------------------

################################################
#            Search Lower Bound                #
################################################

For n preprocessed items, finding a given item
among them in cmp model requires Omega( log(n) )
in worst case.

Proof.
    A decision tree is binary and must have at least
    n leaves: one for each answer. Therefore the
    height >= log(n).

=> Binary search is optimal in this model.
    
################################################
#            Sorting Lower Bound               #
################################################

        A[i] < A[j] ?
    NO                YES
    ...     ...       ...
    
leaf:  A[5] < A[7] < A[1] < ...< A[n]
    
- Decision tree is binary
- # of leaves >= # possible outcomes = n!
=> height >= log(n!)
           = log(n(n-1)...1)
           = log(n)+log(n-1)+...+log(2)
           = sum log(i) for i = 1 -> n
          >= sum log(i) for i = n/2 -> n
          >= sum log(n/2) for i = n/2 -> n
           = sum [log(n)-1] for i = n/2 -> n
           = (n/2)log(n) - n/2
           = Omega( nlog(n) )

################################################
#              Integer Sorting                 #
################################################

- Assume n keys are integers in {0, 1, ..., k-1} and
  each fits in a word.
- Comparisons aren't the only thing we can do in O(1)
  with integers.
- For small k, you can sort in O(n) time.

Counting sort O(n):

Want to sort
    3 5 7 5 5 3 6
    
Have n items, each with a key.

Let L = array of k empty lists

# For each item, key(x) is in {0, ..., k-1}
for j in range(n):
    L[ key(A[j]) ].append(A[j])
    
output = []

for i in range(k):
    output.extend(L[i])

################################################
#               Counting Sort                  #
################################################

Want to sort
    3 5 7 5 5 3 6
    
We will place our integers into k buckets, since
we know 0 <= key(x) <= k-1. Then we can just iterate
through the buckets at the end.

How L is populated:
------------------------------
j=0  |  3   |        |   |   |
j=1  |  3   |  5     |   |   |
j=2  |  3   |  5     |   | 7 |
j=3  |  3   |  5 5   |   | 7 |
j=4  |  3   |  5 5 5 |   | 7 |
j=5  |  3 3 |  5 5 5 |   | 7 |
j=6  |  3 3 |  5 5 5 | 6 | 7 |  
------------------------------

Then output is just the last row in order:
    [3, 3, 5, 5, 5, 6, 7]
    

"""
from operator import __getitem__



# Counting sort: Works as a lookup table where we append
# elements to a table by their keys then merge the table
# in order from index 0 to end.
def counting_sort(A, key, k):

    L = [[] for i in range(k)]

    # For each item, key(x) is in {0, ..., k-1}
    for j in range( len(A) ):
        index = key(A[j])
        L[ index ].append(A[j])
        
    output = []
    
    for i in range(k):
        output.extend(L[i])
        
    return output

"""
def key(x):
    return int(x)


A = [3, 5, 7, 5, 5, 3, 6]
output = counting_sort(A, key, 8)
print('Counting sort:\nunsorted: ' + str(A))
print('sorted:   ' + str(output))
"""

################################################
#                 Radix Sort                   #
################################################
"""

- Imagine each integer in some base B.
=> # digits = d = log_b(k)+1

- Then sort ints by significant digits
    - Sort by least sig. -> most sig.
    - Sort by digit using counting sort.

If b = k <= n^c, then radix sort is O(n*c)


Sorts strings of integers.
Args: List A
      digits_range, base ten = 10
      num_digits = string length of nums (must >= equal)
"""
def radix_sort(A, digits_range, num_digits):
    
    output = A
    
    # Sort from least sig. digit to most sig. digit
    for i in reversed(range(num_digits)):
        output = counting_sort(output, lambda x: int(x[i]), digits_range)
    
    return output
    
    
B = ['4002341', '2301432', '5552413', '0041243', '0712143', '7481234']
print('Radix Sort:\nunsorted: ' + str(B))
output = radix_sort(B, 9, 7)
print('sorted:   ' + str(output))