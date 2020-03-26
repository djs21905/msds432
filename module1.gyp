# Assignment 1 Sorting & Search Algorithms 
import numpy as np

# creates arrays of size n
# input is a list of array sizes
def makearray(array_length,letters):
    final = []
    for item,letter in zip(array_length,letters):
        letter = np.random.uniform(1,1000,size = item)
        final.append(np.sort(letter))
    return final


lengths = [512,1024,2048,4096,8192]
letters = ["a","b","c","d","e"]
b = makearray(lengths,letters)
print(b[1])


