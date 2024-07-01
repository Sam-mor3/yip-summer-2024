best_colors = ["blue", "green", "purple", "red"]
index1 = 1
index2 = 2

oldcolor = best_colors[index1]
print (oldcolor)
#swap the object at index1 and the object at index2 try to make it general
#for any index and lst so for example ["blue", "green", "purple", "red"]
#becomes ["red", "green", "purple", "blue"]
best_colors[1] = best_colors[index2]
best_colors[2] = oldcolor
print(best_colors)

num = [1,5,7,6,8,11,12]

index_1=2
index_2=4

oldnum = num[index_1]

num[2] = num[index_2]
num[4] = oldnum
print(num)



