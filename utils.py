"""importing necessary packages"""
import streamlit as st
import requests

def main_heading_text():
    st.markdown("""

        <style>
        .big-font {
            text-align: center;
            padding-top: 0.5px;
            font-size: calc(0.70em + 4.5vmin);
            font-family: sans-serif;
            font-weight: bold;
        }
        </style>
        """, unsafe_allow_html = True)

    st.markdown('<p class="big-font">WAFIAPPS CATEGORY VIEWER</p>', unsafe_allow_html = True)

#if False:

#   def intro_lottie(filepath: str):
#        with open(filepath, "r") as f:
#            return json.load(f)

@st.cache(show_spinner = False)
def intro_lottie(url: str):
    """defining function for lottie"""
    r = requests.get(url)
    if r.status_code != 200:
        return None

    return r.json()