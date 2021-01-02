# Notes

So fast lookups are easily taken care of using a dictionary but how do you keep order whilst still accounting for O(1) insertions and deletions.

We can store the cache values in both a dictionary and a linked list. Effectively creating an OrderedDict.

However we should use a Doubly Linked List over a regular Linked List, the reason being is that when evicting the tail (least used cache item) on a `LRUCache.put` operation, we need a reference to the tail's previous node in order to assign it as the new tail. This keeps the `.put` operation as O(1) and saves us traversing the linked list in order to remove the tail.