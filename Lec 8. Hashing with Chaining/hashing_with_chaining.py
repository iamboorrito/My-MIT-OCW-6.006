"""
Created on Aug 13, 2017

@author: Evan Burton

################################################
#                Dictionary                    #
################################################

Maintain set of items, where each item has a key
    - can insert items: overwrite given existing keys
    - delete items
    - search for keys: return item with given key
      or report that it doesn't exist

Want to search faster than O( log(n) )

In Python: dict = {}

    D[key] ~ search
    D[key] = val ~ insert
    del D[key] ~ delete
    
    item = (key, value)

Motivation:
    - document distance
    - database
    - compilers and interpreters
    - network router/server

Simple Approach:

    - Direct access table
    - Store items in array indexed by key
    
    0 [     ]
    1 [     ]
        .
        .
      [     ] 

Badness:
    1. Keys may not be nonneg. integers
    2. Significant memory use

Solution to (1):
    - Prehash: map keys to nonneg. integers
    - In theory keys are finite and discrete
    - In Python, hash(x) is the prehash of x
        * hash('\0B') == hash('\0\0C') == 64

################################################        
#     Ideally, hash(x) = hash(y) iff x = y     #
################################################

You can implement your own hash by overriding __hash__()
    - don't use mutable objects as keys!

Solution to (2):
    - Reduce space of all possible keys down to
      reasonable size m for table.
      
Hash Table:

    0 [  item1   ]
    1 [          ]
      [  item2   ]
        .
        .
  m-1 [          ] 
  
  hash(k1) = 0
  hash(k2) = 2

But by the pidgeonhole principle, there will be two
keys such that h(ki) = h(kj) and ki != kj. 

################################################        
#                  Chaining                    #
################################################

Store linked list of colliding elements in each slot
of your hash table.

    0 [  ptr     ] -----> [ ptr2, item1 ] --------> [ptr3, item2]
    1 [          ]
      [  item2   ]
        .
        .
  m-1 [          ] 

################################################ 
#      Assumption: Simple uniform hashing      #
################################################ 

Each key is equally likely to be hashed to any slot
of the table independent of where other keys were
hashed.

Want to know expected length of a chain
    - Given n keys and m slots = n/m = load factor
    - Constant if m = Theta(n)
    
=> Insert/Delete/Search are O(1 + |chain|)

################################################ 
#                 Hash Functions               #
################################################ 

1. Division method: 

        h(k) = k mod p for prime p
        
2. Multiplication method:

        h(k) = [a*k mod 2**w] >> w-r
        
   where w is # of bits in k and a and 0 < r < w.
   Then let m = 2**r.
   
3. Universal Hashing:

        h(k) = ( (a*k+b) mod p ) mod m
        
        a and b are random in {0, ..., p-1} and
        p is very large. Then P(h(a) = h(b)) = 1/m
"""

def mult_hash(k):
    return (1234567*k % 2**32) >> 13

def univ_hash(k):
    
    m = 123456789
    a = 17
    b = 2342445
    p = 48112959837082048697
    
    return ( (a*k+b) % p ) % m

print(mult_hash(2))
print(univ_hash(2))