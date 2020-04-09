import numpy as np
import time
import pandas as pd
import seaborn as sns
import random
import matplotlib.pyplot as plt

# creates arrays of size n
# input is a list of array sizes
def makearray(array_length,letters):
    final = []
    random.seed(42)
    for item,letter in zip(array_length,letters):
        letter = np.random.uniform(1,1000,size = item)
        final.append(np.sort(letter))
    return final


# Finds the smallest value in an array
def findSmallest(arr):
  # Stores the smallest value
  smallest = arr[0]
  # Stores the index of the smallest value
  smallest_index = 0
  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest_index = i
      smallest = arr[i]      
  return smallest_index

# Sort array
def selectionSort(arr):
  newArr = []
  for i in range(len(arr)):
      # Finds the smallest element in the array and adds it to the new array
      smallest = findSmallest(arr)
      newArr.append(arr.pop(smallest))
  return newArr


array_sizes = [5000,10000,15000,20000,25000]
vars = ["a","b","c","d","e"]
random_data = makearray(array_sizes,vars)

times = []
for item in random_data:
    start_time = time.time()
    findSmallest(item)
    time_to_run = time.time()- start_time
    times.append(time_to_run)

table_input = {"Size of Array":array_sizes, "Selection Sort (ms)": times}
results_table = pd.DataFrame(table_input, index = [1,2,3,4,5])

plt.plot(results_table["Size of Array"], results_table["Selection Sort (ms)"])
plt.xlabel("Size of Array")
plt.ylabel("Time (ms)")
plt.title("Selection Sort Performance With Increasing Array Size")
plt.show()



"""
Selection Sort is an algorithm used to sort values within an array.  It is Big O(n^2) which makes it increasingly less
appropriate as the input size increases (See Figure).  As the input size increased from 5000-25000 the time taken also increases
in what appears to be a linear fashion.  This is likely due to the few datapoints used in the experiment.  I suspect that
as the sample size increases the curve will approximate O(n^2) more than a straight line. 

Selection sort splits the array into two lists, a sorted and unsorted list.  To begin, the sorted list is empty. 
The algorithm iterates through each item in the unsorted list and moves the smallest/largest value to the sorted list.
This pattern continues until the unsorted list is empty. 

"""
    