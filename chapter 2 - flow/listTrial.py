import random

myList = ["green", "yellow", "blue"]
print(random.choices(myList, weights = [10,1,1], k=10))