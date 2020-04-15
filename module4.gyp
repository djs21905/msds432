# Module 4 Mini Programming Quicksort Daniel Smith
import string
import numpy as np
import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random

def makearray(array_len):
    string_len = 50
    final = []
    chars = list(string.ascii_letters + string.digits)
    for item in array_len:
        temp_store = []
        for x in range(item):
            generated_string = ''.join(random.sample(chars, k = string_len))
            temp_store.append(generated_string)
        final.append(temp_store)
    return final

# QUICKSORT
def quicksort(array):
  if len(array) < 2:
    # base case, arrays with 0 or 1 element are already "sorted"
    return array
  else:
    # recursive case
    pivot = array[0]
    # sub-array of all the elements less than the pivot
    less = [i for i in array[1:] if i <= pivot]
    # sub-array of all the elements greater than the pivot
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

# SELECTION SORT From Module 2 
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

#MERGESORT

def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 
  
    # create temp arrays 
    L = [0] * (n1) 
    R = [0] * (n2) 
  
    # Copy data to temp arrays L[] and R[] 
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
  
    # Merge the temp arrays back into arr[l..r] 
    i = 0     # Initial index of first subarray 
    j = 0     # Initial index of second subarray 
    k = l     # Initial index of merged subarray 
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
  
    # Copy the remaining elements of L[], if there 
    # are any 
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
  
    # Copy the remaining elements of R[], if there 
    # are any 
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
  
# l is for left index and r is right index of the 
# sub-array of arr to be sorted 
def mergeSort(arr,l,r): 
    if l < r: 
  
        # Same as (l+r)//2, but avoids overflow for 
        # large l and h 
        m = (l+(r-1))//2
  
        # Sort first and second halves 
        mergeSort(arr, l, m) 
        mergeSort(arr, m+1, r) 
        merge(arr, l, m, r) 


lengths = [200,400,600,800]
random_lists = makearray(lengths)

quicksort_times = []
for item in random_lists:
    start_time = time.time()
    quicksort(item)
    time_to_run = time.time()- start_time
    quicksort_times.append(time_to_run)

selectionsort_times = []
for item in random_lists:
    start_time = time.time()
    selectionSort(item)
    time_to_run = time.time()- start_time
    selectionsort_times.append(time_to_run)

mergesort_times = []
for item in random_lists:
    start_time = time.time()
    mergeSort(item,0,len(item)-1)
    time_to_run = time.time()- start_time
    mergesort_times.append(time_to_run)

results = {"Array Size":lengths,"Quick Sort":quicksort_times,"Merge Sort":mergesort_times,"Selection Sort":selectionsort_times}

table = pd.DataFrame(results)

print(table)

plt.plot(results["Array Size"], results["Quick Sort"],label = "Quick Sort")
plt.plot(results["Array Size"], results["Merge Sort"],label = "Merge Sort")
plt.plot(results["Array Size"], results["Selection Sort"],label = "Selection Sort")
plt.xlabel("Size of Array")
plt.ylabel("Time (ms)")
plt.title("Performance of Quick Sort vs Merge Sort vs Selection Sort")
plt.legend()
plt.show()

"""
In this exercise we compare the efficiency of several Sorting algorithms, namely Quick Sort, Merge Sort and Selection 
Sort.  Each algorithm attacks the problem of sorting a list of items differently.  

Selection Sort - Selection sort splits the array into two lists, a sorted and unsorted list.  To begin, the sorted list is empty. 
The algorithm iterates through each item in the unsorted list and moves the smallest/largest value to the sorted list.
This pattern continues until the unsorted list is empty. Selection Sort is O(n^2)

Merge Sort- A divide and conquer algorithm that splits the input array into two halves.  The algorithm calls itself to 
sort the two halves and then the two sorted halves are merged, resulting in a fully sorted array. Merge Sort is 
O(nlogn)

Quick Sort- Also a divide and conquer algorithm that picks a pivot point and partitions the array around the selected pivot.
Quicksort is then called on each partition recursively.  Quick sorts average run time case is as good as merge sort
O(nlogn)

The results of this experiment are clear.  Selection sort is the worst performer at O(n^2).  Quick Sort and Merge Sort
are both very close in perfomance, however Merge Sort consistantly performs slightly better especially as the input size n
increases.  This makes Merge Sort a clear choice when working with large datasets. Conversely Quick Sort performance decreases
as input size increases. 

"""