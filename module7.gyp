# Comparing breadth first search and Dijkstras Algorithm 
# Finding shortest path for graphs. 

from collections import deque
import random
import string
import time
import pandas as pd


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
            #(reverse[place])
            if place != "DC" and "Indianapolis" and "Pittsburg":
                if paths["DC_Path1"][-1] in reverse[place]:
                    paths["DC_Path1"].append(place)
                if paths["Pittsburg_Path2"][-1] in reverse[place]:
                    paths["Pittsburg_Path2"].append(place)
                if paths["Indianapolis_Path3"][-1] in reverse[place]:
                    paths["Indianapolis_Path3"].append(place)  
                #print(paths["DC_Path1"])
                #print(paths["Pittsburg_Path2"])
                #print(paths["Indianapolis_Path3"])
            if findla(place,param2):
                result = []
                #print(place + " was located")
                for key,value in paths.items():
                      if param2 in value:
                            #print("The quickest path is:")
                            for item in value: 
                                  result.append(item)
                                  #if item == param2:
                                        #print(item)
                                  #else:
                                        #print(item + "--->")           
                return result
            # Moves Los Angeles to front of Queue so it is chosen first if available
            else:
                if param2 in graph[place]:
                   #print(graph[place])
                   a = graph[place].index(param2) 
                   graph[place][a], graph[place][0] = graph[place][0], graph[place][a]
                   #print(graph[place])
                   search_queue += graph[place]   
                else:
                      search_queue += graph[place]
                searched.append(place)
    return False




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
start_time = time.time()
bfs_path = search("NYC", "Los Angeles",reverse)
bfs_time_to_run = time.time()- start_time
print(bfs_path)

dij_graph = {# DC Pathway
        "NYC":{"DC":2,"Pittsburg":7,"Indianapolis":11},
        "DC":{"Atlanta":2},
        "Atlanta":{"New Orleans":2},
        "New Orleans": {"Dallas":2},
        "Dallas":{"Albuquerque":2},
        "Albuquerque":{"Pheonix":2},
        "Pheonix": {"Las Vegas":2, "San Diego":5},
        
        # Indianapolis Pathway
        "Indianapolis": {"Kansas City":8},
        "Kansas City": {"Denver":7},
        "Denver": {"Salt Lake City":6},
        "Salt Lake City": {"Las Vegas":9},

        # Pittsburg Pathway
        "Pittsburg": {"Cincinnati":6},
        "Cincinnati": {"St Louis":8},
        "St Louis": {"Oklahoma City":7},
        "Oklahoma City": {"Albuquerque":9},

        # Point of Convergence on Vegas
        "Las Vegas":{"San Diego":2, "Los Angeles":5},
        "San Diego": {"Los Angeles":2},
        "Los Angeles": {}


}

infinity = float("inf")
costs = {}
cumulative_distance = [0,2,4,6,8,infinity,12,11,19,26,32,7,13,21,28,infinity,infinity]
for item,value in zip(dij_graph.keys(),cumulative_distance):
    costs[item] = value
costs["Los Angeles"] = infinity

processed = []


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

# Timer here
start_time = time.time()
# Find the lowest-cost node that you haven't processed yet.
node = find_lowest_cost_node(costs)
# If you've processed all the nodes, this while loop is done.
while node is not None:
    cost = costs[node]
    # Go through all the neighbors of this node.
    neighbors = dij_graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # If it's cheaper to get to this neighbor by going through this node...
        if costs[n] > new_cost:
            # ... update the cost for this node.
            costs[n] = new_cost
            # This node becomes the new parent for this neighbor.
            reverse[n] = node
    # Mark the node as processed.
    processed.append(node)
    # Find the next node to process, and loop.
    node = find_lowest_cost_node(costs)

#start is los angeles end is NYC
def findquick(endpoint,reversegraph,start,costs):
    travel_path = [start]
    var = reversegraph[start]
    travel_path.append(var)
    var = reversegraph[start]
    while endpoint not in travel_path:
        #print(travel_path)
        if type(var) is str:
            travel_path.append(reversegraph[var])
            var = reversegraph[var]
        else:
            val = 100
            for item in var:
                city = item
                if costs[item] < val:
                    city = item
                    val = costs[item]
            if city == "NYC":
                break
            else:
                if type(reversegraph[city]) is list:
                    for item in reversegraph[city]:
                        #print(item)
                        travel_path.append(item)
                else:
                   travel_path.append(reversegraph[city]) 
                var = reversegraph[city]
    final = []
    for item in travel_path:
        if type(item) is list:
            for x in item:
                final.append(x)
        else:
            final.append(item)
    return list(reversed(final))
                
        
    
dij_path = findquick("NYC",reverse,"Los Angeles",costs)
dij_time_to_run = time.time()- start_time
print(dij_path)



dij_total_cost = 0
for index, item in zip(range(len(dij_path)),dij_path):
   if index == 9:
       pass
   else:
       dij_total_cost = dij_graph[item][dij_path[index+1]] + dij_total_cost

#print(dij_total_cost)

bfs_total_cost = 0
for index, item in zip(range(len(bfs_path)),bfs_path):
   if index == len(bfs_path)-1:
       pass
   else:
       bfs_total_cost = dij_graph[item][bfs_path[index+1]] + bfs_total_cost

#print(bfs_total_cost)

bfs_stops = len(bfs_path)

dij_stops = len(dij_path)

#print(bfs_stops,dij_stops)


results = {"BFS Stops": [bfs_stops], 
            "DIJ Stops": [dij_stops],
            "BFS Total Cost": [bfs_total_cost],
            "DIJ Total Cost": [dij_total_cost],
            "BFS Computation Time (ms)": [bfs_time_to_run],
            "DIJ Computation Time (ms)": [dij_time_to_run]
}

#print(results)

final_results = pd.DataFrame(results)

print(final_results)