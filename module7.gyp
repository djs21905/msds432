# Comparing breadth first search and Dijkstras Algorithm 
# Finding shortest path for graphs. 

from collections import deque
import random
import string
import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def findla(name,param2):
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
            if findla(person,param2):
                print(person + " was located")
                return True
            else:
                search_queue += graph[person]
                # Marks this person as searched
                searched.append(person)
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
        "DC":["Atlana"],
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
        "St Louis": "Oklahoma City",
        "Oklahoma City": ["Albuquerque"]

        # Point of Convergence on Vegas
        "Las Vegas":["San Diego", "Los Angeles"],
        "San Diego": ["Los Angeles"],

}