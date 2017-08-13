"""
Created on Aug 13, 2017

@author: Evan Burton

################################################
#               Binary Trees                   #
################################################

For unsorted array:
    We want insert in O(1) without check
        check costs O(n)

For sorted array:
    Find insertion point in log(n)
        - Use binary search to find the minimum
          index i such that R[i] >= t
    Compare in O(1)
        - Compare R[i] and R[i-1] against t in O(1)
    Want fast insert 
        - Insertion requires shifting which is O(n)
        
With a sorted list we get:

    [a] -> [b] -> [c] -> [d]
    
    but no random access guaranteed
    
The BST:

        30
     17    40
  14  20  
  
Determined by Nodes, keys, and pointers to next nodes.

################################################
#                BST Invariant                 #
################################################

For all nodes x, 
    - if y is in the left subtree of x
     then key(y) <= key(x)
    - if y is in the right subtree of x
     then key(y) >= key(x)

Insertion:

    Insert 49         49
    Insert 79       46  79
    Insert 46     41 55
    Insert 41
    
If h is the height of the tree, then insertion with check
is done in O(h) time.

"""

class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
    def __str__(self):
        return str(self.key)

# A binary search tree which keeps track of children and its parent.
class BST():
    def __init__(self, key):
        self.root = Node(key)
    
    # Create a new node with given key and put into BST.        
    def add(self, key):
        node = Node(key)
        self.insert(node)
                    
    # Insert a node into tree
    def insert(self, other):
        
        node = self.root
        
        while node != None:
            if other.key <= node.key:
                if node.left is None:
                    node.left = other
                    node.left.parent = node
                    return
                else:
                    node = node.left
            else:
                if node.right is None:
                    node.right = other
                    node.right.parent = node
                    return
                else:
                    node = node.right
    
    # Returns the node with specified key or None if it
    # does not exist
    def find(self, key):
        
        node = self.root
        
        while node != None:
            
            if key == node.key:
                return node
            elif key < node.key:
                if node.left is None:
                    return None
                else:
                    node = node.left
            else:
                if node.right is None:
                    return None
                else:
                    node = node.right       
    
    # Deletes a node with given key if it exists    
    def delete(self, key):
        
        # Look for value
        node = self.find(key)
        
        # Key isn't in tree
        if node is None:
            return
        else:
            
            if node.left and node.right:
            
                min = node.right
                    
                # Find min replacement
                while min.left != None:
                    min = min.left
                    
                # Swap keys and delete
                node.key = min.key
                parent = min.parent
                parent.left = None
            else:
                parent = node.parent
                # Find which node this is and delete + relink
                if parent.right is node:
                    parent.right = node.right or node.left
                    (node.right or node.left ).parent = parent
                else: 
                    parent.left = node.right or node.left
                    (node.right or node.left ).parent = parent
                    
    # Adds the elements of the list to the BST
    def extend(self, list):
        
        for x in list:
            self.add(x)

bst = BST(5)
bst.extend([2, 18, -4, 3, 21, 19, 25])
bst.delete(18)
