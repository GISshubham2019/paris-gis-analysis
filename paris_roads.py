import osmnx as ox
import matplotlib.pyplot as plt
print("----STEP 1 : DOWNLOADING THE PARIS ROAD MAPS ----")
G=ox.graph_from_place("Paris , France", network_type="drive")
print("Download Completed !")

print("--- step 2: Basic Network Stats---")
print(ox.basic_stats(G))

print("---- step 3: Plotting paris Roads----")
fig, ax =ox.plot_graph(G,
                       bgcolor="black",
                       edge_color="white",
                       edge_linewidth=0.5,
                       node_size=0)

#Convert to GeoDataFrame and see the road types
edges=ox.graph_to_gdfs(G,nodes=False)
print(edges["highway"].value_counts())
print("road types")
plt.title("paris Road Network")
#color roads by type- speed zone style
def get_color(highway):
    if highway == "motorway" or highway =="trunk":
        return "red"
    elif highway=="primary":
        return"orange"
    elif highway=="secondary":
        return"yellow"
    else:
        return"white"
    
edge_colors=[get_color(h) for h in edges["highway"]]
fig,ax=ox.plot_graph(G,
                     bgcolor="black",
                     edge_color=edge_colors,
                     edge_linewidth=0.8,
                     node_size=0)

plt.title("paris roads by types")
plt.show()