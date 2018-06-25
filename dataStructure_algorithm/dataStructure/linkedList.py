# Node is the basic element of a linked list. It have two information in a node. 
# One is the value we want to store, the other is to point to the next node we want to link to. 
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None