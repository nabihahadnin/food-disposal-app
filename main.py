import streamlit as st
import os
from streamlit_navigation_bar import st_navbar
import pages as pg

st.set_page_config(page_title = "Food Waste Disposal Centre Locator", page_icon="♻️", layout = "wide", initial_sidebar_state="collapsed")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

pages = ["About", "Food Waste Disposal Centre Locator"]
parent_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(parent_dir, "img/logo.svg")

styles = {
    "nav": {
        "background-color": "white",
        "justify-content": "left",
        "font-size": "14px",
    },
    "img": {
        "padding-right": "14px",
    },
    "span": {
        "color": "black",
        "padding": "0px",
        "transition": "color 0.3s ease",
    },
    "ul": {
        "justify-content": "left",
        "align-items": "left",
        "gap": "14px"
    },
    "active": {
        "background-color": "white",
        "color": "var(--text-color)",
        "font-weight": "normal",
    },
    "hover": {
        "color": "#28a745",
    }
}
options = {
    "show_menu": True,
    "show_sidebar": False,
    "use_padding": False,
}

page = st_navbar(
    pages,
    logo_path=logo_path,
    styles=styles,
    options=options
)

functions = {
    "About": pg.show_about,
    "Food Waste Disposal Centre Locator": pg.show_map,

}

go_to = functions.get(page, pg.show_about)
go_to()