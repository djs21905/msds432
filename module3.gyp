# Daniel Smith Module 3 Comparing performance of Recursion and Iteration

# Factorial Function Using Recursion 
import numpy as np
import random
import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def fact(x):
  if x == 1:
    return 1
  else:
    return x * fact(x-1)

random.seed(42)
arr = np.random.randint(100,500,size = 10)

#Iteration
iteration_times = [] 

iter_result = []
for item in arr:
    factorial = 1 
    start_time = time.time()
    for i in range(1,int(item)+1):
        factorial = factorial * i 
    iter_result.append(factorial)
    time_to_run = time.time()- start_time
    iteration_times.append(time_to_run)

# Recursion
recursive_times = []
recursive_result = []
for item in arr:
    start_time = time.time()
    rec = fact(item)
    recursive_result.append(rec)   
    time_to_run = time.time()- start_time
    recursive_times.append(time_to_run)

data = {"Number": arr, "Iteration": iteration_times,"Recursion":recursive_times}
timed_results = pd.DataFrame(data)
timed_results["Time Diff"] = timed_results["Recursion"] - timed_results["Iteration"]
#timed_results["Recursion Result"] = pd.Series(recursive_result,dtype=object)
timed_results["Factorial Result"] = pd.Series(iter_result,dtype=object)

plt.plot(timed_results["Number"], timed_results["Iteration"],label = "Iteration (ms)",linestyle="",marker="o")
plt.plot(timed_results["Number"], timed_results["Recursion"],label = "Recursion (ms)",linestyle="",marker="o")
plt.xlabel("Number")
plt.ylabel("Time (ms)")
plt.title("Recursion Vs Iteration")
plt.legend()
plt.show()



"""
Recursion and standard iteration can be used to accomplish similar goals.   However, there are pros and cons to each 
methodology.   Recursion is a function that calls itself.  Recursion typically requires less code than
Iteration does but from a performance standpoint it is less effective.  Conversely Iteration requires more code
but is more efficient and requires less time to execute.  

Iteration O(1)
Recursion O(n)
"""
