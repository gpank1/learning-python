# Lists are used to store multiple items in a single variable.
# Lists: ordered, mutable, allows duplicate elements.

# Create a list
mylist = ["Gytis", "Eric", "Kevin"]
print(mylist)

# Print the first item in the list
item = mylist[0]
print(item)

# Print each item in the list
for i in mylist:
    print(i)

# Check if an item is in the list
if "Gytis" in mylist:
    print("Yes")
else:
    print("No")

# How many items in the list
print(len(mylist))

# Add an item to the list
mylist.append("Kent")
print(mylist)

# Insert an item at a specific position
mylist.insert(1, "Bella")
print(mylist)

# Remove an item from the list but be able to use it later
pop_item = mylist.pop()
print(pop_item)
print(mylist)

# Remove an item from the list and do not use it later
remove_item = mylist.remove("Gytis")
print(remove_item)

# clear the list
mylist.clear()
print(mylist)

# reverse the list
mylist = ["Gytis", "Eric", "Kevin"]
mylist.reverse()
print(mylist)

# sort the list
mylist.sort()
print(mylist)

# sort the list but do not change the original list
new_list = sorted(mylist)
print(new_list)

# create a list with the same elements multiple times
mylist = [0] * 5
print(mylist)

# concatenate two lists
mylist2 = [1, 2, 3, 4, 5]
new_list = mylist + mylist2
print(new_list)

# slicing a list
# syntax: list[start:stop:step]
# can use negative step index to reverse the list
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = mylist[1:5]
print(a)

# copy a list, but do not change the original list
list_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_copy = list_original.copy() # if not copy() then it will change the original list
# can also use list_original[:] to copy the list
# or list(list_original) to copy the list
print(list_copy)

# list comprehension
# syntax: [expression for item in iterable]
mylist = [1, 2, 3, 4, 5, 6]
b = [i*i for i in mylist]
print(mylist)
print(b)