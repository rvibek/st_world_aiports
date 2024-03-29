# import streamlit
import pandas as pd
import folium
from folium.plugins import MarkerCluster, Fullscreen
import streamlit as st 
from streamlit_folium import st_folium


st.set_page_config(layout="wide")

# load data
@st.cache
def load_data():
	df = pd.read_csv("https://davidmegginson.github.io/ourairports-data/airports.csv")
	return df[:500]


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


def main():
    st.title('Airport around the world')
    add_sidebar = st.sidebar.markdown('some components')
    airports = load_data()
    markers = list(zip(airports['latitude_deg'], airports['longitude_deg'], airports['name']))
    marker_cluster = MarkerCluster(name="Airports").add_to(m)

	# Add the markers to the map and cluster them
    for marker in markers:
	    folium.Marker(marker[:2], popup=marker[2]).add_to(marker_cluster)
    Fullscreen().add_to(m)
    m.add_child(folium.map.LayerControl())


	# call to render Folium map in Streamlit
    st_map =  st_folium(m, width="100%")
    
    return st_map 





if __name__ == "__main__":
    main()
