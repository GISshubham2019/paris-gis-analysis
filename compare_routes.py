import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

print("--- Step 1: downloading Paris---")
G=ox.graph_from_place("Paris, France", network_type="drive")

print("--- step 2: Adding speed & Travel Time---")
G=ox.add_edge_speeds(G)
G=ox.add_edge_travel_times(G)

print("---Step 3: Finding Both Routes----")
#Eiffel Tower --> Louvre 
start=ox.nearest_nodes(G, X=2.2945, Y=48.8584)
end=ox.nearest_nodes(G, X=2.3376, Y=48.8606)

#Route 1 - shorest Distance

route_Distance=nx.shortest_path(G, start,end, weight="length")

#Route 2 : Fatstest travel time 
route_Time=nx.shortest_path(G, start, end, weight="travel_time")

print("--- Step 4: Plotting Both Routes---")

fig, ax=ox.plot_graph_routes(G,
                             
    routes=[route_Distance,route_Time],
    route_colors=["blue","red"],
    route_linewidths=[4,4],
    node_size=0,
    bgcolor="black",
    edge_linewidth=0.3)

plt.title("Paris: Blue=shorest Distance Red=Fastest Time\nEiffel Tower --> Louvre",
          color="white", fontsize=11)
#Calulate Actual travel time diffrence 
time_fast=nx.shortest_path_length(G,start,end,weight="travel_time")
dist_short=nx.shortest_path_length(G,start,end,weight="length")

print(f"Shortest Distance:{dist_short:0f} meters")
print(f"Fastest time: {time_fast/60:.1f} minutes")

plt.show()