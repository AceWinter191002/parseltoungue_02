inputs = input("")
inputs = inputs.split()
count = 0
while count <len(inputs):
    print("Argv of {} is {}".format(count, inputs[count]))
    count = count+1
X=sorted(inputs, key = len, reverse=True)
i=0
for z in range(0, len(X)):
    print(X[z])
