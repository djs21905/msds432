# Module 5 Hashing
import string
import numpy as np
import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random

# Make list of 100k names 10 chars long no duplicates
# Takes a list as param
def makearray(array_len):
    string_len = 10
    final = []
    chars = list(string.ascii_letters + string.digits)
    for item in array_len:
        temp_store = []
        for x in range(item):
            generated_string = ''.join(random.sample(chars, k = string_len))
            temp_store.append(generated_string)
        for item2 in temp_store:
            final.append(item2)
    return final

# Binary Search
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

# Linear Search
def simplesearch(array,target):
	for item in array:
		if item == target:
			return True 
		else:
			pass

array_container = makearray([100000])

sorted_container = sorted(array_container)

set_container = set(array_container)


selected_names = [array_container[9999],array_container[29999],array_container[49999],array_container[69999],array_container[89999],array_container[99999]] 


#Unsorted list Linear Search
linear_time = []
for item in selected_names:
    start_time = time.time()
    simplesearch(array_container,item)
    time_to_run = time.time()- start_time
    linear_time.append(time_to_run)

#Sorted list Binary Search 
binary_time = []
for item in selected_names:
    start_time = time.time()
    binary_search(sorted_container,item)
    time_to_run = time.time()- start_time
    binary_time.append(time_to_run)

#Set built in method Search 
hash_time = []
for item in selected_names:
    start_time = time.time()
    set_container.remove(item)
    time_to_run = time.time()- start_time
    hash_time.append(time_to_run)

results = {"Names":selected_names,
            "Linear Search":linear_time,
            "Binary Search":binary_time,
            "Hash":hash_time
}

final_table = pd.DataFrame(results)
print(final_table)

plt.plot(final_table.index, final_table["Binary Search"],label = "Binary Search",linestyle="",marker="o")
plt.plot(final_table.index, final_table["Linear Search"],label = "Linear Search",linestyle="",marker="o")
plt.plot(final_table.index, final_table["Hash"],label = "Hash Table",linestyle="",marker="o")
plt.xlabel("Random String of Length 10")
plt.ylabel("Time (ms)")
plt.title("Binary Search Vs. Simple Search Vs. Hash Table Performance")
plt.legend()
plt.show()

"""
In this exercise we compared the search performance of several different data structure/search algorithm combinations.

1) Hash Table w/ hash search
2) Non Sorted array using linear search
3) Sorted array using binary search

Based on previous knowledge, we expect the Sorted Binary combination to be more performant than the non sorted linear
search.  This is because on average Linear Search is O(n) and binary search is O(logn).  

Hashing is the process of mapping an index value to a key/ value pair.  This occurs through the process of hashing, 
where a key is fed into a hash function which generates an index.  For instance if I have a key = "dave" and a value 
of "biology", "dave" would be fed to the hash function and it would generate and index value i.e 10.  

Now consider we have hundreds of records and we want to find "dave".  With hash search we feed the value we are looking
for to the hash function and it generates the index value (in this case 10) and we can immediately locate our desired
data ("biology").

Hash search is O(1).  

Our experimental results confirm the underlying principles discussed above.  Hash search was most performant, followed
by Binary Search and Linear Search.  
"""