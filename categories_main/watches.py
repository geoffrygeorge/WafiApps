import streamlit as st
import time


def watches_main():

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

    sub = col1.radio('Choose Sub Category :', ['Mens Wrist Watch', 'Womens Wrist Watch', 'Boys Watches', 'Girls Watches', 'Couple Watches'])

    if sub in ('Mens Wrist Watch', 'Womens Wrist Watch', 'Boys Watches', 'Girls Watches'): ######

        col4.info('CURRENTLY, THERE ARE NO ROOT-CATEGORIES FOR THE SELECTED SUB-CATEGORY')

    elif sub == 'Couple Watches': ######

        col4.warning('CURRENTLY, THIS SUB-CATEGORY IS DISABLED & THERE ARE NO ROOT-CATEGORIES')
