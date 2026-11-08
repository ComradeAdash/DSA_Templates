# DSA Templates & Tricky Problem Solutions

Practice for interviews and 307 :D

## Problem Types and Assumed Inputs

| Problem Type | Assumed Input |
|---|---|
| Graphs | Adjacency list |
| Trees | Root Node |
| Linked Lists | Head Node |
| Heaps / Priority Queues | List or Array |

# Time Complexity Analysis
- understanding commonly used data structures and ADTs in Python

## Doubly Linked List

- contains next and prev pointers in each node
- head ptr
- tail ptr


| Operation | Big O |
|---|---|
| Insert at front / append | O(1) |
| Traversal | O(N) |
| Insert at position / delete at position | O(N) |
| Deletion at front / end | O(1) |
| Delete Given Node | O(1) |

```python
from collections import deque
```

```python
list = dequeue[start]
```

### .methods

```python
list.append(x),
list.appendleft(x),
list.extend(iterable), # ex) adding lists to lists 
list.extendleft(iterable),
list.insert(i,x),
list.pop(),
list.popleft(),
list.remove(x), # removes first occurence of x
list.clear(), # removes all elements from the list
list.count(x), # counts num of elements equal to x
list.index(x, [start, [stop]]), # returns first occurence of x, at or after start, and before stop
list.rotate(n=1), # rotate the list 1-right, -1-left
list.reverse()
```
