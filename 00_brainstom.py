import random
L = ["Video Games", "School Subjects", "Sports", "Drinks", "Food"]
input("SCATTEGORIES: Type 'GO!' to start ")
var = 1
print(random.choice(L))
print("List 10 things from this category: ")
Answer = []
counter = 1
while counter <11:
    inputs = input("New Answer:")
    counter = counter + 1
    Answer.append(inputs)
else:
    print(Answer)
