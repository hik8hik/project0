# NOTE: SETS - Sets are different from lists and tuples in that they are unordered.
# They are also different because while you can have two or more of the same elements
# within a list/tuple, a set will only store each value once. We can define an empty set
# using the set function. We can then use add and remove to add and remove elements from
# that set, and the len function to find the set’s size. Note that the len function works on
# all sequences in python. Also note that despite adding 4 and 3 to the set twice, each item
# can only appear once in a set.

# CREATE AN EMPTY SET

s = set()

# ADDING VALUES TO THE SET

s.add(1)
s.add(2)
s.add(3)
s.add(4)

# PRINT THE SET
print(s)  # {1, 2, 3, 4}

# REMOVING ONE ITEM IN SET
s.remove(3)

# PRINT AFTER REMOVAL
print(s)
