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


array_container = makearray([100000])

sorted_container = sorted(array_container)

set_container = set(array_container)


selected_names = [array_container[9999],array_container[29999],array_container[49999],array_container[69999],array_container[89999],array_container[99999]] 


#Unsorted list Linear Search

#Sorted list Binary Search 

#Set built in method Search 