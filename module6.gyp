# Implementing a Breadth-First Search Algorithm 
from collections import deque
import random
import string
import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def person_is_seller(name,param2):
      return name == param2

def search(name,param2):
    search_queue = deque()
    search_queue += graph[name]
    # This array is how you keep track of which people you've searched before.
    searched = []
    while search_queue:
        person = search_queue.popleft()
        # Only search this person if you haven't already searched them.
        if person not in searched:
            if person_is_seller(person,param2):
                print(person + " was located")
                return True
            else:
                search_queue += graph[person]
                # Marks this person as searched
                searched.append(person)
    return False

def makearray(item):
    final = []
    chars = list(string.ascii_letters)
    for item in range(item):
        length = random.randint(3,15)
        generated_string = ''.join(random.sample(chars, k = length))
        final.append(generated_string)
    return final
 

# TO DO: Look into doing this recursively
def createnode():
    graph = {}
    #Level 1 
    l1 = makearray(5)
    #Level 2
    totall2 = []
    totall3 = []
    totall4 = []
    totall5 = []
    graph["start"] = l1
    for item in l1:
        level2 = makearray(5)
        graph[item] = level2
        for item in level2:
            totall2.append(item)
        #Level 3 
        for item2 in level2:
            level3 = makearray(5)
            graph[item2] = level3
            for item in level3:
                totall3.append(item)
            # Level 4 
            for item3 in level3:
                level4 = makearray(5)
                graph[item3] = level4
                for item in level4:
                    totall4.append(item)
            # Level 5 
                for item4 in level4:
                    level5 = makearray(5)
                    graph[item4] = level5
                    for item in level5: 
                        totall5.append(item)
            # Level 6
                    for item5 in level5:
                        level6 = makearray(5)
                        graph[item5] = level6
    return graph,l1,totall2,totall3,totall4,totall5


random.seed(30) 
graph = createnode()

l1sample = random.sample(graph[1], 3)
l2sample = random.sample(graph[2], 3)
l3sample = random.sample(graph[3], 3)
l4sample = random.sample(graph[4], 3)
l5sample = random.sample(graph[5], 3)

graph = graph[0]


# Level 1 search
l1times = []
for item in l1sample:
    start_time = time.time()
    search("start",item)
    time_to_run = time.time()- start_time
    l1times.append(time_to_run)

l2times = []
for item in l2sample:
    start_time = time.time()
    search("start",item)
    time_to_run = time.time()- start_time
    l2times.append(time_to_run)

l3times = []
for item in l3sample:
    start_time = time.time()
    search("start",item)
    time_to_run = time.time()- start_time
    l3times.append(time_to_run)

l4times = []
for item in l4sample:
    start_time = time.time()
    search("start",item)
    time_to_run = time.time()- start_time
    l4times.append(time_to_run)

# Error here 
l5times = []
for item in l5sample:
    start_time = time.time()
    search("start",item)
    time_to_run = time.time()- start_time
    l5times.append(time_to_run)


results = {"Level 1 Time": l1times,
            "Level 2 Time": l2times,
            "Level 3 Time": l3times,
            "Level 4 Time": l4times,
            "Level 5 Time":l5times, 
            }

level = ["L1","L1","L1","L2","L2","L2","L3","L3","L3","L4","L4","L4","L5","L5","L5"]
name = []
time = []
for item in l1sample:
    name.append(item)
for item in l2sample:
    name.append(item)
for item in l3sample:
    name.append(item)
for item in l4sample:
    name.append(item)
for item in l5sample:
    name.append(item)
arrays = [level,name]

for item in l1times:
    time.append(item)
for item in l2times:
    time.append(item)
for item in l3times:
    time.append(item)
for item in l4times:
    time.append(item)
for item in l5times:
    time.append(item)
arrays = [level,name]

index = pd.MultiIndex.from_arrays(arrays,names=("Level","Name To Search"))
test = pd.DataFrame({"Time (ms)":time},index = index)

avg = test.groupby(["Level"]).mean()

avg.plot(kind="bar")
plt.title("Breadth First Search")
plt.ylabel("Time (ms)")

plt.show()
