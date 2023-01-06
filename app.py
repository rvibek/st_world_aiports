# import streamlit
import pandas as pd
import folium
from folium.plugins import MarkerCluster, Fullscreen
import streamlit as st 
from streamlit_folium import st_folium



# load data
@st.cache
def load_data():
	df = pd.read_csv("https://davidmegginson.github.io/ourairports-data/airports.csv")
	return df


airports = load_data()



m = folium.Map(location=[0, 0], zoom_start=3)
# Add custom base maps to folium
basemaps = {
    'Google Maps': folium.TileLayer(
        tiles = 'https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
        attr = 'Google',
        name = 'Google Maps',
        overlay = True,
        control = True
    ),
    'Google Satellite': folium.TileLayer(
        tiles = 'https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
        attr = 'Google',
        name = 'Google Satellite',
        overlay = True,
        control = True
    ),
    'Google Terrain': folium.TileLayer(
        tiles = 'https://mt1.google.com/vt/lyrs=p&x={x}&y={y}&z={z}',
        attr = 'Google',
        name = 'Google Terrain',
        overlay = True,
        control = True
    ),
    'Google Satellite Hybrid': folium.TileLayer(
        tiles = 'https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
        attr = 'Google',
        name = 'Google Satellite',
        overlay = True,
        control = True
    ),
    'Esri Satellite': folium.TileLayer(
        tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr = 'Esri',
        name = 'Esri Satellite',
        overlay = True,
        control = True
    )
}

# Add custom basemaps
# Add custom basemaps
basemaps['Esri Satellite'].add_to(m)
basemaps['Google Terrain'].add_to(m)
basemaps['Google Maps'].add_to(m)
basemaps['Google Satellite Hybrid'].add_to(m)





# markers = list(zip(airports['latitude_deg'], airports['longitude_deg'], airports['name']))

# marker_cluster = MarkerCluster(name="Airports").add_to(m)

# # Add the markers to the map and cluster them
# for marker in markers[:200]:
#     folium.Marker(marker[:2], popup=marker[2]).add_to(marker_cluster)


Fullscreen().add_to(m)

m.add_child(folium.map.LayerControl())

# # marker_cluster.save("airports.html")

# # call to render Folium map in Streamlit


c1, c2 = st.columns(2)
with c1:
	output = st_folium(m, width=725)

with c2:
	st.write(output)
