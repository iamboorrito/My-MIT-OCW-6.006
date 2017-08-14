"""
Created on Aug 13, 2017

@author: Evan

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
    
"""

def key(x):
    return int(x)

# Counting sort: Works as a lookup table where we append
# elements to a table by their keys then merge the table
# in order from index 0 to end.
def counting_sort(A, key, k):

    L = [[] for i in range(k)]

    # For each item, key(x) is in {0, ..., k-1}
    for j in range( len(A) ):
        L[ key(A[j]) ].append(A[j])
        
    output = []
    
    for i in range(k):
        output.extend(L[i])
        
    return output

A = [3, 5, 7, 5, 5, 3, 6]
output = counting_sort(A, key, 8)   
print(output)

################################################
#                 Radix Sort                   #
################################################
"""

- Imagine each integer in some base B.
=> # digits = d = log_b(k)+1

- Then sort ints by significant digits
    - Sort by least sig. -> most sig.
    - Sort by digit using counting sort.

If k <= n^c, then radix sort is O(n*c)

"""
