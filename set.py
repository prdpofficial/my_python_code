'''
all set methods

Python has a set of built-in methods that you can use on sets.

Method	                      Description
add()	                Adds an element to the set
clear()	                Removes all the elements from the set
copy()	                Returns a copy of the set
difference()	        Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	        Remove the specified item
intersection()    	Returns a set, that is the intersection of two or more sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	        Returns whether two sets have a intersection or not
issubset()	        Returns whether another set contains this set or not
issuperset()	        Returns whether this set contains another set or not
pop()                 	Removes an element from the set
remove()        	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	                Return a set containing the union of sets
update()	        Update the set with another set, or any other iterable

'''

#1.add()

fruits = {"apple", "banana", "cherry"}

fruits.add("orange")

print(fruits)

#2.clear()

fruits = {"apple", "banana", "cherry"}

fruits.clear()

print(fruits)

#3. copy()


fruits = {"apple", "banana", "cherry"}

x = fruits.copy()

print(x)

#4. difference()

#The difference() method returns a set that contains the difference between two sets.
#Meaning: The returned set contains items that exist only in the first set, and not in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)

print(z)

#5. difference_update()

#he difference_update() method removes the items that exist in both sets.
#The difference_update() method is different from the difference() method, because the
#difference() method returns a new set, without the unwanted items, and the difference_update() method
#removes the unwanted items from the original set.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y)

print(x)

#6. discard()

fruits = {"apple", "banana", "cherry"}

fruits.discard("banana")

print(fruits)

#7.intersection()

#The intersection() method returns a set that contains the similarity between two or more sets.
#Meaning: The returned set contains only items that exist in both sets, or in all sets if
#the comparison is done with more than two sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

#8. intersection_update()

#The intersection_update() method removes the items that is not present in both sets
#(or in all sets if the comparison is done between more than two sets).

#The intersection_update() method is different from the intersection() method, because the
#intersection() method returns a new set, without the unwanted items, and the intersection_update() 
#method removes the unwanted items from the original set

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

#when 3 set are present
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

x.intersection_update(y, z)

print(x)

#9. isdisjoint()

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)

print(z)

#10. issubset()

#Return True if all items in set x are present in set y:

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)

#11. issuperset()

#Return True if all items set y are present in set x:

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y)

print(z)

#12. pop()

#Remove a random item from the set:

fruits = {"apple", "banana", "cherry"}

fruits.pop()

print(fruits)

#13. remove()

#Remove "banana" from the set:
fruits = {"apple", "banana", "cherry"}

fruits.remove("banana")

print(fruits)

#14. symmetric_difference()

#The symmetric_difference() method returns a set that contains all items from both set,
#but not the items that are present in both sets.

#Meaning: The returned set contains a mix of items that are not present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

#15. symmetric_difference_update()

#The symmetric_difference_update() method updates the original set by
#removing items that are present in both sets, and inserting the other items.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

#16. union()

#The union() method returns a set that contains all items from the original set,
#and all items from the specified set(s).

#You can specify as many sets you want, separated by commas.

#It does not have to be a set, it can be any iterable object.

#If an item is present in more than one set, the result will contain only one appearance of this item.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y)

print(z)

#if more then 2 sets

x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}

result = x.union(y, z)

print(result)

#17. update()

#The update() method updates the current set, by adding items from another set (or any other iterable).

#If an item is present in both sets, only one appearance of this item will be present
#in the updated set.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y)

print(x)


#these are all set built-in methods...




