"""importing necessary packages"""
import streamlit as st
import requests

def main_heading_text_cat():
    st.markdown("""

        <style>
        .big-font {
            text-align: center;
            padding-top: 0.5px;
            font-size: calc(0.50em + 4.5vmin);
            font-family: sans-serif;
            font-weight: bold;
        }
        </style>
        """, unsafe_allow_html = True)

    st.markdown('<p class="big-font">WAFIAPPS CATEGORY VIEWER</p>', unsafe_allow_html = True)

def main_heading_text_vendor():
    st.markdown("""

        <style>
        .big-font {
            text-align: center;
            padding-top: 0.5px;
            font-size: calc(0.50em + 4.5vmin);
            font-family: sans-serif;
            font-weight: bold;
        }
        </style>
        """, unsafe_allow_html = True)

    st.markdown('<p class="big-font">WAFIAPPS VENDOR PORTAL</p>', unsafe_allow_html = True)

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

def break_loop_vendor_viewer():
    i = 0
    while i < 1:
        st.markdown('<p></p>', unsafe_allow_html = True)
        i += 1

def break_loop_vendor_divider():
    i = 0
    while i < 4:
        st.markdown('<p></p>', unsafe_allow_html = True)
        i += 1

def hide_anchor_link():
    st.markdown("""
        <style>
        .css-15zrgzn {display: none}
        .css-eczf16 {display: none}
        .css-jn99sy {display: none}
        </style>
        """, unsafe_allow_html=True)

def hide_row_column_indices():
    # CSS to inject contained in a string
    hide_table_row_index = """
                <style>
                thead {display:none}
                tbody th {display:none}
                .blank {display:none}
                </style>
                """

    # Inject CSS with Markdown
    st.markdown(hide_table_row_index, unsafe_allow_html=True)