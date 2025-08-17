import pandas as pd
import folium
from streamlit_folium import st_folium
import streamlit as st

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def show_map():
    st.markdown("#### Find Food Waste Disposal Centres Near You")

    #Added by FA - retrieved data directly
    sheet_name = 'Food%20Waste%20Management%20Centers'
    sheet_id = '1eOm00zBQOpfz9TnOQkIcmDWzUe-oJ-iBltIOJEF16vs'
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    df = pd.read_csv(url)

    # Create the map
    map_center = [df["latitude"].mean(), df["longitude"].mean()]
    m = folium.Map(location=map_center, zoom_start=11)

    # Add all markers
    for _, row in df.iterrows():
        folium.Marker(
            location=[row["latitude"], row["longitude"]],
            popup=f"<b>{row['name']}</b><br>{row['address']}",
            tooltip=row["name"], # add more info in pop up in map
            icon=folium.Icon(color="green", icon="map-marker", prefix="fa")
        ).add_to(m)

    # Display map
    print(st_folium(m, width=1200, height=400))

    # Form for user input
    with st.form("location_form"):
        location = st.selectbox(
            "Postcode",
            df["postcode"].unique(),
            index=None,
            placeholder="Enter/Select your postcode",
        )
        submit = st.form_submit_button("Find Centres")

    if submit:
        if location:
            # Find and display centres based on the location
            st.write(f"Finding centres near: {location}")
            # Pending: function to find the centres based on user input and also apply data validation (success if found, error if none found)
        else:
            st.warning("Please enter a location.")
