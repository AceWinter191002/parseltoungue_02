A = [False,True,True,None,True,None,None,False,False,None,True,False]
B = ["or","or","or","==","!=","==","and","==","!=","and","!=","and"]
C = [False,False,None,None,True,True,False,True,None,False,True,None]
count = 0
for x in range(0, len(B)):
    if B[count] == "or":
        print(A[count] or C[count])
        count = count + 1
    elif B[count] == "==":
        print(A[count] == C[count])
        count = count + 1
    elif B[count] == "!=":
        print(A[count] != C[count])
        count = count + 1
    else:
        print(A[count] and C[count])
        count = count + 1

