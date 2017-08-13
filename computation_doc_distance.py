'''
Created on Aug 12, 2017

@author: Evan
'''

################################################
#    Document distance problem:                #
#    Calculate d(D1, D2) which determines      #
#    how different two documents are.          #
################################################

"""

Here we will define distance to be amount of shared
words/chars. We will think of a document D as a vector:

    D[w] = # of occurrences of w in D
    
Ex. D1 = 'the cat'
    D2 = 'the dog'
    
    Define d'(D1, D2) = D1 * D2
    = sum(D1[w]*D2[w]) over all w
    
    Bad scaling, long documents give large distances.
    
    Try d''(D1, D2) = D1 * D2 / (|D1| * |D2|)
    
    Then d(D1, D2) = arccos(^)

################################################    
Algorithm:
    1. Split doc into words
    2. Compute word frequencies (compute D[w])
    3. Inner product
    
    Runtime for 1Mb in seconds:
        1. 228.1
        2. 164.7
        3. 123.1
        4. 71.7
        5. 18.3
        6. 11.5
        7. 1.8
        8. 0.2
    
################################################

"""

from math import acos, sqrt

# Straightforward algorithm
def doc_dist(d1, d2):
    
    dict1 = {}
    dict2 = {}
    
    # Split and populate dicts
    for str in d1.split():
        if dict1.__contains__(str):
            dict1[str] += 1
        else:
            dict1.update({str:1})
            
    for str in d2.split():
        if dict2.__contains__(str):
            dict2[str] += 1
        else:
            dict2.update({str:1})
    
    # Compute inner product
    prod_sum = 0.0
    
    for w in dict1:
        if dict2.__contains__(w):
            prod_sum += dict1[w]*dict2[w]
    
    # Return their angle, 0 => no difference and pi/2 => nothing shared
    return acos(prod_sum / sqrt(len(dict1)*len(dict2)))

# Test equality
D1 = 'my dog has fleas'
D2 = 'my dog has fleas'


print(doc_dist(D1, D2))