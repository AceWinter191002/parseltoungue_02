import sys
import re
if len(sys.argv) >= 3:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(sys.argv[1] + " divided by " + sys.argv[2] + " equals " + str(a//b) + " remainder " + str(a % b))
    X=len(sys.argv)
    count = 1
    for z in range(1, X):
        if re.findall("\d+\.\d", str(sys.argv[count])):
            print("Variable {} contains : {} which is of type: Float".format(count, sys.argv[count]))
            count = count + 1
        elif re.findall("\d[^i]"", str(sys.argv[count])):
            print("Variable {} contains : {} which is of type: Integer".format(count, sys.argv[count]))
            count = count + 1
        else: 
            print("Variable {} contains : {} which is of type: Complex".format(count, sys.argv[count]))
            count = count + 1

