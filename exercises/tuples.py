# Tuple: ordered, immutable, allows duplicate elements.
# Tuples are similar to lists, but they are immutable, meaning that once they are created, their elements cannot be changed.
# Tuples can be more efficient than lists in terms of memory usage and performance, especially when dealing with large amounts of data.

# Basics of Tuples
mytuple = ("Gytis", "Eric", "Kevin")
print(mytuple)

item = mytuple[0]
print(item)

for i in mytuple:
    print(i)

 # Count the number of times "p" appears in the tuple
mytuple2 = ("a","p","p","l","e")
print(mytuple2.count("p"))

# Check if an item is in the tuple and print its index
print(mytuple2.index("p"))

# Convert a tuple to a list, can do vice versa
my_list = list(mytuple2)

# Unpack a tuple
# Unpacking is the process of assigning the elements of a tuple to variables.
# The number of variables must match the number of elements in the tuple.
mytuple3 = "Max", 28, "Boston"
name, age, city = mytuple3
print(name)
print(age)
print(city)

# Unpacking with asterisk
# The asterisk (*) operator can be used to unpack a tuple into one variable with multiple elements converted into a list.
mytuple4 = (0, 1, 2, 3, 4)
i1, *i2, i3 = mytuple4
print(i1)  # 0
print(i2)  # [1, 2, 3]
print(i3)  # 4