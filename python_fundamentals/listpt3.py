sam = ["orange", "black", "blue"]
Red = ["red", "black", "yellow"]
oumy = ["purple", "green", "pink"]
ethan = ["blue", "red", "green"]
aiden = ["blue", "red", "green"]

person_1 = aiden
person_2 = oumy 

print(person_1)
print(person_2)

Numofsim = 0

if (person_2[0] in person_1):
    Numofsim = Numofsim + 1
    print(f"They both like the color {person_2[0]}")
if (person_2[1]in person_1):
    Numofsim = Numofsim + 1
    print(f"They both like the color {person_2[1]}")
if (person_2[2] in person_1):
    Numofsim = Numofsim + 1 
    print(f"They both like the color {person_2[2]}")

# if (person_2[0] in person_1) and (person_2[1]in person_1) and (person_2[2] in person_1):
#     print(f"They both like {person_2[0]},{person_2[1]}, {person_2[2]}")
# elif (person_2[0] in person_1) and (person_2[1]in person_1):
#     print(f"They both like {person_2[0]} ,and {person_2[1]}")
# elif (person_2[0] in person_1) and (person_2[2] in person_1):
#     print(f"They both like {person_2[0]} ,and {person_2[2]}")
# elif(person_2[1] in person_1) and (person_2[2]in person_1):
#      print(f"They both like {person_2[1]} ,and {person_2[2]}")
# else: print("They do not like similar colors")

print (f"There are {Numofsim} same amount of colors in both lists")