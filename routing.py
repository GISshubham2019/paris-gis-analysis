import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

print("---- Step 1: Downloading paris Road networks")
G= ox.graph_from_place("paris, France", network_type="drive")

#Add speed and tarvek time to every road edge
print("--- step 2: Adding speed & Travel Time ---")
G=ox.add_edge_speeds(G)
G=ox.add_edge_travel_times(G)

#Define the start and end points using lat\lon
#Eiffel tower-> Louvre Museum 

print("---- step 3: Finding the fastest Route----")
start=ox.nearest_nodes(G, X=2.2945, Y=48.8584)
end=ox.nearest_nodes(G, X=2.3376, Y=48.8606)

# Calculate the fastest route by travel time
route=nx.shortest_path(G, start,end,weight="travel_time")
print(f"Route found! Total road segments:{len(route)}")


#plot the route on the paris map

print("----step 4: plotting Route---")
fig, ax = ox.plot_graph_route(G, route,
                              bgcolor="black",
                              node_size=0,
                              edge_linewidth=0.3,
                              route_color="red",
                              route_linewidth=3)

plt.title("Fastest Route: Eiffel Tower-> Louvre\nParis,France",
          color="white",fontsize=12)

plt.show()


