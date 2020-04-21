# Implementing a Breadth-First Search Algorithm 
from collections import deque
import random
import string

def person_is_seller(name):
      return name[-1] == 'm'

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    # This array is how you keep track of which people you've searched before.
    searched = []
    while search_queue:
        person = search_queue.popleft()
        # Only search this person if you haven't already searched them.
        if person not in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
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
    return graph,l1,totall2,totall3,totall4,totall5


random.seed(42) 
graph = createnode()

l1sample = random.sample(graph[1], 3)
l2sample = random.sample(graph[2], 3)
l3sample = random.sample(graph[3], 3)
l4sample = random.sample(graph[4], 3)
l5sample = random.sample(graph[5], 3)

