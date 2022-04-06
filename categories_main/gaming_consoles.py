import streamlit as st
import time


def gaming_consoles_main():

    # defining columns for structure
    col1, col2, col3, col4 = st.columns([7.2,1,1,5])

    col2.empty()
    col3.empty()

    if False:
        def root_cat_text():

            col4.subheader('ROOT CATEGORIES')

            with col4:

                with st.spinner(text = "Please Wait"):

                    time.sleep(0.5)

    col1.subheader('SUB CATEGORIES')

    sub = col1.radio('Choose Sub Category :', ['Gaming Mice', 'Gaming Components', 'Gaming Headset', 'Gaming Chairs', 'Gaming Keyboard', 'Controllers-Joysticks & Accessories', 'PS4 Games', 'Xbox One Games', 'PS5 Games', 'Gaming Monitors', 'Gaming Consoles', 'Gaming Desktop', 'Gaming Laptop', 'Gaming Cases', 'PC Games'])

    if sub in ('Gaming Mice', 'Gaming Components', 'Gaming Headset', 'Gaming Chairs', 'Gaming Keyboard', 'Controllers-Joysticks & Accessories', 'PS4 Games', 'Xbox One Games', 'PS5 Games', 'Gaming Monitors', 'Gaming Consoles', 'Gaming Desktop'): ######

        col4.info('CURRENTLY, THERE ARE NO ROOT-CATEGORIES FOR THE SELECTED SUB-CATEGORY')

    elif sub in ('Gaming Laptop', 'Gaming Cases', 'PC Games'): ######

        col4.warning('CURRENTLY, THIS SUB-CATEGORY IS DISABLED')