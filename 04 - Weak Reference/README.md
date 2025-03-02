# Chapter - Weak References
In this chapter, we will show how weak references work and how they can be useful.

----

## Weak References

Weak reference is a way to tweak the reference count of an object. When 
a weak reference is assigned to an object it doesn't increase its reference
count. This is of importance because in CPython, memory management directly relies on
it.

In CPython, the garbage collector automatically deletes an object when there is 
no more reference to it.

### Example
Using weak references can be useful when creating a memory cache,
to prevent the memory space used from growing unnecessarily large.

Suppose you want to store data in a dictionary:
````py
class MyObject:
    
    def __init__(self, _id):
        self._id = _id
    

a = MyObject(1)     # ref count 1
_cache = {'1': a}   # ref count 2

b = _cache['1']     # ref count 3
````
When `a` is added to the cache dictionary it increases the reference count by 1.
Now, if `a` and `b` are deleted, there were still be a reference to the object living
in the dictionary. Therefore, teh object won't be deleted and the cache won't be cleared.

However, if weak reference is used as storage in the cache, it will be cleared when `a` 
and `b` are deleted.
````py
import weakref
class MyObject:
    
    def __init__(self, _id):
        self._id = _id
    

a = MyObject(1)                  # ref count 1
_cache = {'1': weakref.ref(a)}   # ref count 1

b = _cache['1']                  # ref count 2
````
Only a weak reference of the object is stored in the cache which allow the object to die when the reference count
drops to zero. When `a` and `b` are deleted, the reference will drop to 
and the cache will be cleared.
