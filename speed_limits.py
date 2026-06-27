import osmnx as ox
import matplotlib.pyplot as plt
print("--- step 1: Dowloading paris Roads----")
G=ox.graph_from_place("Paris, France", network_type="drive")

print("---step 2: Converting to GeoDataframe---")
edges=ox.graph_to_gdfs(G, nodes=False)

print("--- step3: checking speed limit column---")
print(edges["maxspeed"].value_counts())

#====================================================================================================
# Step 4: Color paris roads by real speed limits
# Author:Shubham
# Date : June 25
#=====================================================================================================

def get_speed_color(speed):
    """
    Assigns a color to each road based on its speed limit.
    This mirros the speed zone classification used in 
    proedessional GIS mapping systems like TomTom/

    Args:
    speed: maxspeed value from openstreetmaps
    returs:
    color string for map Visualixation
    """

    # Handle the missing speed data- common in real OSM database
    if speed is None:
     return "gray"
    
    #converts to string to hadle both int and list values

    speed_str=str(speed)
    # classification by the speed Zone
    if "130" in speed_str or "110" in speed_str:
       return "red"
    elif "80" in speed_str or "70" in speed_str:
       return "orange"
    elif "50" in speed_str:
       return "yellow"
    elif "30" in speed_str:
       return "green"
    elif "20" in speed_str:
       return "cyan"
    else:
       return"white"
    
    #this creates one color to the each segment

edge_color=[get_speed_color(s) for s in edges["maxspeed"]]

    #step5: final speed zone map


fig, ax=ox.plot_graph(G,
                          bgcolor="black",
                          edge_color=edge_color,
                          edge_linewidth=0.8,
                          node_size=0
                          )

plt.title("Paris Road network - speed zone classification",
          color="white",fontsize=14)
plt.show()

print("---speed Zone Map compelte---")
