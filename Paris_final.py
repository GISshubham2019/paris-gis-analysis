import osmnx as ox
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

#Download paris
G=ox.graph_from_place("paris, France",network_type="drive")
edges=ox.graph_to_gdfs(G, nodes=False)

#speed color function 
def get_speed_color(Speed):
    if Speed is None:
        return "gray"
    Speed_str=str(Speed)
    if "130" in Speed_str or "110" in Speed_str:
        return "red"
    elif "80" in Speed_str or "70" in Speed_str:
        return "orange"
    elif "50" in Speed_str:
        return "yellow"
    elif "30" in Speed_str:
        return "green"
    elif "20" in Speed_str:
        return "cyan"
    else:
        return"gray"
    
# Apply colors

edge_colors=[get_speed_color(s)for s in edges["maxspeed"]]

#plot map

fig, ax=ox.plot_graph(G,
                      bgcolor="black",
                      edge_color=edge_colors,
                      edge_linewidth=0.8,
                      node_size=0,
                      show=False)

#Add legends

legend_items=[
    mpatches.Patch(color="red", label="110-130 km/h motorway"),
    mpatches.Patch(color="orange", label="70-80 km/h Fast Road"),
    mpatches.Patch(color="Yellow", label="50 km/h Urban main"),
    mpatches.Patch(color="green", label="30 km/h slow zone"),
    mpatches.Patch(color="cyan", label="20 km/h Residential"),
    mpatches.Patch(color="gray", label="unknown speed"),

]

ax.legend(handles=legend_items,
          loc="lower left",
          fontsize=8,
          facecolor="black",
          labelcolor="white",
          framealpha=0.8)

#add titile

ax.set_title("Paris Road Network - speed zone Classification\nData: OpenStreeMap | Built with OSMnx= Geopandas",
             color="white", fontsize=12, pad=10)

#save as image file
plt.savefig("paris_speed_zone.png",
            dpi=300,
            bbox_inches="tight",
            facecolor="black")

print("Map saved as paris_speed_zones.png")
plt.show()


