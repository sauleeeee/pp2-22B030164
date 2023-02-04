# 1
thisset = {"apple", "banana", "cherry"}
print(thisset)
# 2
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
# 3
thisset = {"apple", "banana", "cherry"}

print(len(thisset))
# 4
myset = {"apple", "banana", "cherry"}
print(type(myset))
# 5
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
# access items
# 1
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
# 2
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
# add items
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
# add sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
# add any iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
#remove set items
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
# 2 discard
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
# 3
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
# 4
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
# 5
thisset = {"apple", "banana", "cherry"}

del thisset
# print(thisset)
# loop sets
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
#   join sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
# 2
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)
# 3
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)
# 4
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)
# 5
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)