import pandas as pd
import folium
from streamlit_folium import st_folium

def render_compost_map():
    # Sample data
    data = {
        "name": ["KLCC"],
        "latitude": [3.1579],
        "longitude": [101.7123],
        "address": ["Kuala Lumpur City Centre, 50088 Kuala Lumpur"]
    }
    df = pd.DataFrame(data)

    # Center map view
    map_center = [df["latitude"].mean(), df["longitude"].mean()]
    m = folium.Map(location=map_center, zoom_start=17)

    # Add marker
    for _, row in df.iterrows():
        folium.Marker(
            location=[row["latitude"], row["longitude"]],
            popup=f"<b>{row['name']}</b><br>{row['address']}",
            tooltip=row["name"],
            icon=folium.Icon(color="green", icon="map-marker", prefix="fa")
        ).add_to(m)

    # Display map
    return st_folium(m, width=700, height=500)
