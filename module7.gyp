# Comparing breadth first search and Dijkstras Algorithm 
# Finding shortest path for graphs. 

from collections import deque
import random
import string
import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

costs = {}

processed = []

parents = []

# Backtrace 
# def backtrace(parent, start, end):
#     path = [end]
#     while path[-1] != start:
#         path.append(parent[path[-1]])
#     path.reverse()
#     return path

def findla(name,param2):
      return name == param2

# BFS
# Param2 is destination i.e Los Angeles
def search(name,param2):
    search_queue = deque()
    search_queue += graph[name]

    # Dyanmically creates 3 lists for Path 1 through 3 
    # Used to keep track of each path 
    paths = {}
    ticker = 1
    for varname in search_queue:
        paths[varname + "Path" + str(ticker)] = ["NYC",varname]
        ticker += 1
    print(paths)

    # This array is how you keep track of which people you've searched before.
    searched = []
    level = 1
    while search_queue:
        place = search_queue.popleft()
        print(place , level)
        # Only search this person if you haven't already searched them.
        if place not in searched:
            if findla(place,param2):
                print(place + " was located")
                return True
            else:
                search_queue += graph[place]
                # Marks this person as searched
                searched.append((place,level))
                level += 1

            # If place is not one of the 3 starting cities
            # use "place" as the key in the reverse_graph
            # if the popped item in the recorded path is equal
            # to one of the items in the reverse graph we append place
            # to the path
        # if place not "DC" or "Indianapolis" or "Pittsburg":
        #         if DC_Path1.pop in reverse_graph[place]:
        #             DC_Path1.append[place]
        #         elif Pittsburg_Path2.pop in reverse_graph[place]:
        #             Pittsburg_Path2.append[place]
        #         elif Indianapolis_Path3.pop in reverse_graph[place]:
        #             Indianapolis_Path3.append[place]  
    return False


# Function for Dijkstras Algo.
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    # Go through each node.
    for node in costs:
        cost = costs[node]
        # If it's the lowest cost so far and hasn't been processed yet...
        if cost < lowest_cost and node not in processed:
            # ... set it as the new lowest-cost node.
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# Find the lowest-cost node that you haven't processed yet.
node = find_lowest_cost_node(costs)
# If you've processed all the nodes, this while loop is done.
while node is not None:
    cost = costs[node]
    # Go through all the neighbors of this node.
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # If it's cheaper to get to this neighbor by going through this node...
        if costs[n] > new_cost:
            # ... update the cost for this node.
            costs[n] = new_cost
            # This node becomes the new parent for this neighbor.
            parents[n] = node
    # Mark the node as processed.
    processed.append(node)
    # Find the next node to process, and loop.
    node = find_lowest_cost_node(costs)



graph = { # DC Pathway
        "NYC":["DC","Pittsburg","Indianapolis"],
        "DC":["Atlanta"],
        "Atlanta":["New Orleans"],
        "New Orleans": ["Dallas"],
        "Dallas":["Albuquerque"],
        "Albuquerque":["Pheonix"],
        "Pheonix": ["Las Vegas", "San Diego"],
        
        # Indianapolis Pathway
        "Indianapolis": ["Kansas City"],
        "Kansas City": ["Denver"],
        "Denver": ["Salt Lake City"],
        "Salt Lake City": ["Las Vegas"],

        # Pittsburg Pathway
        "Pittsburg": ["Cincinnati"],
        "Cincinnati": ["St Louis"],
        "St Louis": ["Oklahoma City"],
        "Oklahoma City": ["Albuquerque"],

        # Point of Convergence on Vegas
        "Las Vegas":["San Diego", "Los Angeles"],
        "San Diego": ["Los Angeles"]

}


# Creates a Reverse Graph
reverse = {}
for key, val in graph.items():
    for item in val: 
        if item in reverse: 
            reverse[item].append(key)
        else:
            reverse[item] = [key]


search("NYC", "Los Angeles")
