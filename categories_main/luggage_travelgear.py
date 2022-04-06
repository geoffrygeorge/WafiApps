import streamlit as st
import time


def luggage_travelgear_main():

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

    sub = col1.radio('Choose Sub Category :', ['Backpacks', 'Soft Trolley Bags', 'Hard Trolley Bags', 'Business & Laptop Bags', 'Duffel Bags', 'Cabin Baggage', 'Kids Bags', 'Luggage Accessories', 'Messenger Bags', 'Travel Plugs & Adapters', 'Luggage Sets', 'School Bags-Pencil Cases & Sets', 'Handbags & Shoulder Bags', 'Childrens Luggage', 'Suitcases', 'Waist Packs', 'Wallets & Card Cases', 'Money Organizers', 'Travel Garment Bags', 'Shopping Bags & Baskets'])
   


    if sub in ('Backpacks', 'Soft Trolley Bags', 'Hard Trolley Bags', 'Business & Laptop Bags', 'Duffel Bags', 'Cabin Baggage', 'Kids Bags', 'Luggage Accessories', 'Messenger Bags', 'Travel Plugs & Adapters'): ######

        col4.info('CURRENTLY, THERE ARE NO ROOT-CATEGORIES FOR THE SELECTED SUB-CATEGORY')

    elif sub in ('School Bags-Pencil Cases & Sets', 'Handbags & Shoulder Bags', 'Childrens Luggage', 'Suitcases', 'Waist Packs', 'Wallets & Card Cases', 'Money Organizers', 'Travel Garment Bags', 'Shopping Bags & Baskets'): ######

        col4.warning('CURRENTLY, THIS SUB-CATEGORY IS DISABLED & THERE ARE NO ROOT-CATEGORIES')