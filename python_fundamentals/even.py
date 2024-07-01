listnum = [1,2,3,4,5,6,7,8,9,10]

evenslist = []
for n in listnum:
    if n % 2 == 0:
       evenslist.append(n)

print(evenslist)

String="This is a string"
split_lst = String.split()
print(split_lst)

lst = ["apple","banana","peer"]
lst2 = []
var = "cat"
for n in lst:
    lst2.append(n)
    lst2.append(var)

    
print(lst2)


one= ["Apple", "Banana", "Orange"]
two = ["cat", "dog"]

three = []
for n in one:
   three.append(n)
   for a in two:
   three.append(a)
print(three)