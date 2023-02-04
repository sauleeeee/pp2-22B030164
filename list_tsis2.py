# 1
thislist = ["apple", "banana", "cherry"]
print(thislist)
# 2
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
# 3
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
# 4
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
# 5
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
# 6
# access list items
# 1
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
# 2
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
# 3
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
# 4
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
# 5
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
# 6
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
# change item value
# 1
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
# 2
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
# 3
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) 
# 4
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
# 5
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
# add list items
# 1
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
# 2
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
# 3
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
# 4
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
# remove items
# 1
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
# 2
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
# 3
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
# 4
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
# loop lists
# 1
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
# 2
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
# 3
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  # 4
  thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
# comprehension
# 1
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
# 2
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
# sort list
# 1
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
# 2
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
# 3
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
# 4
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
# 5
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
# 6
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
# copy list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
# 2
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
# join lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
# 2
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
# 3
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
# 
