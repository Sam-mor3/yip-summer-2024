while True:
    Var = (input("word:"))
    ans = True
    for i, char in enumerate(Var):
        if Var[i] != Var[-i-1]:
            ans = False
            print ("false") 
            break
    if ans:
        print("true")   

