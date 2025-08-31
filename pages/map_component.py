import pandas as pd
import folium
from streamlit_folium import st_folium
import streamlit as st
from math import radians, sin, cos, asin, sqrt

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Haversine distance (km) – used for filtering
def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0088
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
    return 2 * R * asin((a**0.5))

def show_map():
    st.markdown("#### Find Food Waste Disposal Centres Near You")

    # Load data
    sheet_name = 'Food%20Waste%20Management%20Centers'
    sheet_id = '1eOm00zBQOpfz9TnOQkIcmDWzUe-oJ-iBltIOJEF16vs'
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    df = pd.read_csv(url)
    df.columns = df.columns.str.strip()
    df["latitude"]  = pd.to_numeric(df["latitude"])
    df["longitude"] = pd.to_numeric(df["longitude"])
    df = df.dropna(subset=["latitude","longitude"])

    # Session state for persistence
    if "search_active" not in st.session_state:
        st.session_state.search_active = False
        st.session_state.postcode = None
        st.session_state.radius_km = 5

    # stores values in session_state
    with st.form("location_form", clear_on_submit=False):
        c1, c2, c3 = st.columns([2,1,1])
        with c1:
            postcode = st.selectbox(
                "Postcode",
                sorted(df["postcode"].dropna().unique().tolist()),
                index=None,
                key="postcode_input",
                placeholder="Select your postcode",
            )
        with c2:
            radius_km = st.number_input(
                "Radius (km)", min_value=1, max_value=50,
                value=st.session_state.radius_km, step=1, key="radius_input"
            )
        with c3:
            clear = st.form_submit_button("Clear")
        submit = st.form_submit_button("Find Centres")

    # Handle buttons
    if clear:
        st.session_state.search_active = False
        st.session_state.postcode = None
        st.session_state.radius_km = 5

    if submit and st.session_state.postcode_input is not None:
        st.session_state.search_active = True
        st.session_state.postcode = st.session_state.postcode_input
        st.session_state.radius_km = st.session_state.radius_input

    # Decide which map to render
    if st.session_state.search_active and st.session_state.postcode is not None:
        postcode = st.session_state.postcode
        radius_km = st.session_state.radius_km

        center_rows = df[df["postcode"] == postcode]
        user_lat = center_rows["latitude"].mean()
        user_lon = center_rows["longitude"].mean()

        df = df.copy()
        df["distance_km"] = df.apply(
            lambda r: haversine(user_lat, user_lon, r["latitude"], r["longitude"]), axis=1
        )
        within = df[df["distance_km"] <= radius_km].sort_values("distance_km")
        if within.empty:
            within = df.sort_values("distance_km").head(3)
            st.info(f"No centres within {radius_km} km of {postcode}. Showing nearest {len(within)}.")

        # Focused map (postcode centroid + radius)
        m = folium.Map(location=[user_lat, user_lon], zoom_start=12)

        # Postcode marker
        folium.Marker(
            [user_lat, user_lon],
            popup=f"<b>Your area</b><br>Postcode: {postcode}",
            tooltip="Selected postcode",
            icon=folium.Icon(color="blue", icon="user", prefix="fa")
        ).add_to(m)

        # Radius circle
        folium.Circle(
            [user_lat, user_lon],
            radius=radius_km * 1000,
            color="#3388ff",
            fill=True,
            fill_opacity=0.08
        ).add_to(m)

        # Facility markers
        for _, r in within.iterrows():
            folium.Marker(
                [r["latitude"], r["longitude"]],
                popup=(f"<b>{r['name']}</b><br>{r['address']}<br>"
                       f"Postcode: {r.get('postcode','')}"),
                tooltip=r["name"],
                icon=folium.Icon(color="green", icon="leaf", prefix="fa")
            ).add_to(m)

        # Fit bounds around postcode + results
        bounds = [[user_lat, user_lon]] + within[["latitude","longitude"]].values.tolist()
        m.fit_bounds(bounds, padding=(30,30))
        st_folium(m, width=1200, height=500)

    else:
        # Default map (no active search)
        default_center = [df["latitude"].mean(), df["longitude"].mean()]
        m = folium.Map(location=default_center, zoom_start=11)
        for _, row in df.iterrows():
            folium.Marker(
                [row["latitude"], row["longitude"]],
                popup=f"<b>{row['name']}</b><br>{row['address']}",
                tooltip=row["name"],
                icon=folium.Icon(color="green", icon="map-marker", prefix="fa")
            ).add_to(m)
        st_folium(m, width=1200, height=400)
