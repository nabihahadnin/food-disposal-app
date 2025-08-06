import pandas as pd
import folium
from streamlit_folium import st_folium

def render_compost_map():
    # Load the dataset
    df = pd.read_csv("FWM_Facilities.csv")

    # Create the map
    map_center = [df["latitude"].mean(), df["longitude"].mean()]
    m = folium.Map(location=map_center, zoom_start=11)

    # Add all markers
    for _, row in df.iterrows():
        folium.Marker(
            location=[row["latitude"], row["longitude"]],
            popup=f"<b>{row['name']}</b><br>{row['address']}",
            tooltip=row["name"],
            icon=folium.Icon(color="green", icon="map-marker", prefix="fa")
        ).add_to(m)

    # Return the map
    return st_folium(m, width=700, height=500)
