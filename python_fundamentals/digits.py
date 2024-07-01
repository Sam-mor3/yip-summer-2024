num = (input("number:"))

numofnum = 0



for n in num: 
    numofnum = numofnum + 1
    if n == ".":
        numofnum = numofnum - 1 
    else: 
        numofnum = numofnum + 0 
print (numofnum)
