# Assignment 1 Sorting & Search Algorithms 
import numpy as np
import time
import pandas as pd


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
array_list = makearray(lengths,letters)



def binary_search(item_list,item):
	first = 0
	last = len(item_list)-1
	found = False
	while( first<=last and not found):
		mid = (first + last)//2
		if item_list[mid] == item :
			found = True
		else:
			if item < item_list[mid]:
				last = mid - 1
			else:
				first = mid + 1	
	return found

time_list = []
for item in array_list:
    start_time = time.time()
    binary_search(item,max(item))
    time_to_run = time.time()- start_time
    time_list.append(time_to_run)

table_input = {"Length of Array":lengths, "Binary Search Time (ms)": time_list}
timed_results = pd.DataFrame(table_input, index = [1,2,3,4,5])

print(timed_results)