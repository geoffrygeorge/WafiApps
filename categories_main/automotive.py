import streamlit as st
import time


def automotive_main():

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

    sub = col1.radio('Choose Sub Category :', ['Car Mobile Accessories', 'Car Services', 'Tires & Wheels'])

    if sub in ('Car Mobile Accessories', 'Car Services', 'Tires & Wheels'): ######

        col4.info('CURRENTLY, THERE ARE NO ROOT-CATEGORIES FOR THE SELECTED SUB-CATEGORY')