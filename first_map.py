import geopandas as gpd
import matplotlib.pyplot as plt
from geodatasets import get_path

print("--- Step 1: Loading Spatial Data ---")
# Get the built-in system path for the New York City Borough boundaries
path_to_data = get_path("nybb")
# Read the spatial file (GeoPandas handles shapefiles/geojson under the hood)
nybb = gpd.read_file(path_to_data)

print("\n--- Step 2: Inspecting Data Structure ---")
# A GeoDataFrame looks exactly like a Pandas DataFrame, but it has a 'geometry' column
print(nybb[["BoroName", "Shape_Area", "geometry"]].head(2))

print("\n--- Step 3: Checking the CRS ---")
# Inspect the Coordinate Reference System (Crucial for GIS architecture)
print(f"Dataset CRS: {nybb.crs}")

print("\n--- Step 4: Generating Static Plot ---")
# Plotting using the geometry column attributes
nybb.plot(column="Shape_Area", legend=True, cmap="viridis")
plt.title("New York City Boroughs by Area Size")
print("This is day 2 ")
print(nybb.columns)
print(nybb.shape)
print(nybb.crs)
print(nybb.head())
#select only Manhattan 
manhanttan=nybb[nybb["BoroName"]== "Manhattan"]
manhanttan.plot(color="green")
plt.title("Manhattan Only")
nybb_wgs=nybb.to_crs("EPSG:4326")
print(nybb_wgs.crs)
nybb_wgs.plot()
plt.title("NYC in Latitute longitude")
plt.show()

