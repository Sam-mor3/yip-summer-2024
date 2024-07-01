# index=3
# neighborhood = [5,7,-3,2,8,9]
index = 3
neighborhood = [True, False, False, False, True, False]

before = index -1 
after = index +1 
middle = neighborhood[index]

numofT = 0
numofF = 0 
if index == 5:
    if neighborhood[before] == False:
        # Line 13 checks whether the left neighborhood is either True or False 
        numofF = numofF + 1 
    else:
        numofT = numofT + 1

    if neighborhood[middle] == False:
        numofF = numofF + 1 
    else: 
        numofT = numofT + 1

elif index == 0:
    if neighborhood [after] == False:
        numofF =  numofF + 1 
    else: 
        numofT = numofT + 1 
    if neighborhood[middle] == False:
        numofF = numofF + 1 
    else: 
        numofT = numofT + 1    
else: 
    

    if neighborhood[before] == False:
        numofF = numofF + 1 
    else:
        numofT = numofT + 1

    if neighborhood[middle] == False:
        numofF = numofF + 1 
    else: 
        numofT = numofT + 1

    if neighborhood[after] == False:
        numofF = numofF + 1 
    else: 
        numofT = numofT + 1



# if index == 5:
#     left = neighborhood[before]
#     f = left and middle
# elif index == 0:
#     right = neighborhood[after]
#     f = middle and right
# else: 
#     left = neighborhood[before]
#     right = neighborhood[after] 
#     f =left and middle and right


print(f"The number of False is {numofF} and the number of Truths is {numofT}")






# if middle >= left and middle >= right: 
#     print (f"The greatest number in this neighborhood is {middle}")
# elif left >= middle and left >= right:
#     print (f"The greatest number in this neighborhood is {left}"  )
# else: print (f"The greatest number in this neighborhood is {right}")