# 1
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
# 2
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
# 3
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
# 4
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
# 5thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
# access tuple items
# 1
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
# 2
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
# 3
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
# 4
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
#update tuple
# 1
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
# 2
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
# 3
# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists
# unpack tuple
# 1
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
# 2
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
# 3
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
#loop tuples
# 1
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
  # 2
  thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
# 3
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
  # join tuples
  # 1
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
# 2
fruits = ("apple", "banana", "cherry")
mytuple1 = fruits * 2
print(mytuple1)
# 

