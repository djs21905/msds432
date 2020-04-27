# Comparing breadth first search and Dijkstras Algorithm 
# Finding shortest path for graphs. 

from collections import deque
import random
import string
import time


costs = {}

processed = []

parents = []

def findla(name,param2):
      return name == param2

# BFS
# Param2 is destination i.e Los Angeles
def search(name,param2,reverse):
    search_queue = deque()
    search_queue += graph[name]

    # Dyanmically creates 3 lists for Path 1 through 3 
    # Used to keep track of each path 
    paths = {}
    ticker = 1
    for varname in search_queue:
        paths[varname + "_Path" + str(ticker)] = ["NYC",varname]
        ticker += 1
    searched = []
    while search_queue:
        place = search_queue.popleft()
        if place not in searched:
            print(reverse[place])
            if place != "DC" and "Indianapolis" and "Pittsburg":
                if paths["DC_Path1"][-1] in reverse[place]:
                    paths["DC_Path1"].append(place)
                if paths["Pittsburg_Path2"][-1] in reverse[place]:
                    paths["Pittsburg_Path2"].append(place)
                if paths["Indianapolis_Path3"][-1] in reverse[place]:
                    paths["Indianapolis_Path3"].append(place)  
                print(paths["DC_Path1"])
                print(paths["Pittsburg_Path2"])
                print(paths["Indianapolis_Path3"])
            if findla(place,param2):
                print(place + " was located")
                for key,value in paths.items():
                      if param2 in value:
                            print("The quickest path is:")
                            for item in value: 
                                  if item == param2:
                                        print(item)
                                  else:
                                        print(item + "--->")           
                return True
            # Moves Los Angeles to front of Queue so it is chosen first if available
            else:
                if param2 in graph[place]:
                   print(graph[place])
                   a = graph[place].index(param2) 
                   graph[place][a], graph[place][0] = graph[place][0], graph[place][a]
                   print(graph[place])
                   search_queue += graph[place]   
                else:
                      search_queue += graph[place]
                searched.append(place)
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

# (Start Point, Target, Reverse graph for tracking)
search("NYC", "Los Angeles",reverse)
