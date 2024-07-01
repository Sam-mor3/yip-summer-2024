list1 = [0,1,2,3,4,5,6,7,8]
newlist1 = list1[1:6:2]
print (newlist1)
Sum = newlist1[0] + newlist1[1] + newlist1[2]
print (Sum)
print (newlist1.sum())

petlist = ("dog","parakeet","Hamester","cat","mouse","turtle","gecko", "fish" )
newlist2 = petlist[1:6:2]
print (newlist2)
Sum2 = newlist2[0] + newlist2[1] + newlist2[2]
print (Sum2)

txt = "I like vanilla ice cream"
txt.replace ("vanilla", "chocolate")
print(txt)