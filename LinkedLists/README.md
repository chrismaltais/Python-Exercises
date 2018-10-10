# Linked Lists
## Advantages
- **Can live anywhere in memory**: Array requires sequence of memory to be initiated, each linked list node can be flexibly moved to a diff address
- **Saves memory**: Linked Lists only allocate moemory required for values stored. Arrays must set array size before filling with values which can potentially waste memory
## Disadvantages
- **Linear Lookup Time**: When looking for a value, you must begin at the start of the chain. and check one element at a time.

## Implementation
```python
class Node:
    def __init__(self, val):
      self.val = val
      self.next = None # the pointer literally points to nothing
```
```python
node1 = Node(12) 
node2 = Node(99) 
node3 = Node(37) 
node1.next = node2 # 12->99
node2.next = node3 # 99->37
# the entire linked list now looks like: 12->99->37
```

## Traversing Values
```python 
class Node:
    ...
    
    def traverse(self):
        node = self # start from the head node
        while node != None:
            print node.val # access the node value
            node = node.next # move on to the next node
 ```
