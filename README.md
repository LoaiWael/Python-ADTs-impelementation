<div>
<h1 align="center">Python-ADTs-impelementation</h1>
<p align="center">Python data structures implemented and tested by me ;D</p>
</div>

***

## Binary search
## Stack
<ul>
<li>len(object) => stack object lenght</li>
<li>Iterator => loop on the stack</li>
<li>peek() => get the last element</li>
<li>push(element) => add element</li>
<li>pop(element) => remove and return the last element added</li>
</ul>

## Set
<ul>
  <li>len(object) => Set object lenght</li>
  <li>Itrator => loop on the set</li>
  <li>add(element) => add element</li>
  <li>remove(element) => remove element</li>
  <li>contains(element) => returns True if it have the element and False if not</li>
  <li>equals(object: Set) => compare 2 sets and returns True if equal and False if not</li>
  <li>subset_of(object: Set) => returns True if subset and False if not</li>
  <li>union(object: Set) => returns a new set</li>
  <li>intersect(object: Set) => returns a new set</li>
  <li>difference(object: Set) => returns a new set</li>
</ul>

## Map  -> using BinarySearch.py
<ul>
  <li>len(object) => Map object lenght</li>
  <li>Itrator => loop on the map</li>
  <li>add(key: int, *values) => if key is found it will overwrite it and its values, if not it will creat new one</li>
  <li>append(key: int, *values) => if key is found it will append the values to it, if not it will creat one</li>
  <li>remove_Key(key: int) => remove a key and its values</li>
  <li>remove_Values(key: int, *values) => remove the key values included at the method only</li>
  <li>values_Of(key: int) => return list of the key values</li>
</ul>

## Queue
<ul>
<li>len(object) => Queue object lenght</li>
<li>Iterator => Loop over the queue</li>
<li>enqueue(element) => add element to the queue</li>
<li>dequeue() => Removes the front element</li>
<li>isEmpty() => Returns True if empty and False if not</li>
<li>isFull() => Returns True if it's full and False if not</li>
<li>clear() => Clears the queue || deletes all the elements</li>
<li>object.Get_numOfItems => property returns number of elements in the queue</li>
<li>object.Get_front => property returns the front element</li>
<li>object.Get_rear => property returns the rear element</li>
<li>object.Get_Available_Space => property returns the available space in the queue</li>
</ul>

## Deque
<ul>
<li>len(object) => queue object lenght</li>
<li>Iterator => loop over the queue</li>
<li>insert_Left(element) => add element from the left side</li>
<li>insert_Right(element) => add element from the right side</li>
<li>remove_Left() => removes element from the left of queue</li>
<li>remove_Right() => removes element from the right of the queue</li>
<li>isEmpty() => Returns True if empty and False if not</li>
<li>isFull() => Returns True if it's full and False if not</li>
<li>clear() => Clears the deque || deletes all the elements in the queue</li>
<li>object.Get_numOfItems => property returns number of elements in the queue</li>
<li>object.Get_front => property returns the front element</li>
<li>object.Get_rear => property returns the rear element</li>
<li>object.Get_Available_Space => property returns the available space in the queue</li>
</ul>