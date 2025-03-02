# Chapter - Weak References
In this chapter, we will sho how wek references work.

----

## Weak References

Weak reference is a way to tweak the reference count of an object. When 
a weak reference is assigned to an object it doesn't increased its reference
count. This is of importance because in CPython, memory management directly relies on
it.

In CPython, the garbage collector automatically delete an object when there is 
no more references to it.

### Example
Using weak reference can be useful when creating a memory cache for example,
to avoid the memory to grow. 

Suppose you want to store data in a dictionary:
````py
class MyObject:
    
    def __init__(self, _id):
        self._id = _id
    

a = MyObject(1)     # ref count 1
_cache = {'1': a}   # ref count 2

b = _cache['1']     # ref count 3
````
Now, if you delete a, and b there were still be a reference to the object
in the dictionary, so the object won't be deleted.

However, if we use weak references:
````py
import weakref
class MyObject:
    
    def __init__(self, _id):
        self._id = _id
    

a = MyObject(1)     # ref count 1
_cache = {'1': a}   # ref count 1

b = _cache['1']     # ref count 1
````
In the `_cache` we only store a weak reference to the object which let the object die.
If you delete a and b, the reference count to the object will drop to zero and the cache will be cleared.
