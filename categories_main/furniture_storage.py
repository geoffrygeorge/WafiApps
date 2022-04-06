import streamlit as st
import time


def furniture_storage_main():

    # defining columns for structure
    col1, col2, col3, col4 = st.columns([7.2,1,1,5])

    col2.empty()
    col3.empty()

    def root_cat_text():

        col4.subheader('ROOT CATEGORIES')

        with col4:

            with st.spinner(text = "Please Wait"):

                time.sleep(0.5)

    col1.subheader('SUB CATEGORIES')

    sub = col1.radio('Choose Sub Category :', ['Bathroom Storage & Organiser', 'Bedroom', 'Storage & Organisation', 'Living Room', 'Kitchen & Dining', 'Study Room', 'Home Bar', 'Kitchen & Dining', 'Outdoor Furniture'])



    if sub == 'Bathroom Storage & Organiser': ######

        root_cat = ['Soap Dishes', 'Bath Organizers', 'Toothbrush Holders', 'Toilet Brush Holders', 'Toilet Paper Holders', 'Dispensers', 'Bathroom Trash Bins', 'Tumblers', 'Towel Holders', 'Towel Hooks']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Bedroom': ######

        root_cat = ['Tv Stand & Media Centers', 'Chest of Drawers', 'Bedside Tables', 'Beds', 'Mattresses', 'Wardrobes', 'Dressing Tables']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Storage & Organisation': ######

        root_cat = ['Ironing Boards', 'Racks Shelves & Drawers', 'Cabinet Organizers & Storage Baskets', 'Laundry Storage', 'Clothing & Closet Storage', 'Storage Containers']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Living Room': ######

        root_cat = ['Center Tables', 'Chairs', 'Side Tables', 'Sofa Beds', 'Sofa Sets', 'L-Shaped Sofas', 'Recliners', 'TV & Entertainment Units', 'Nested Tables', 'Bean Bags', 'Shoe Racks', 'Wall Shelves', 'Magazine Racks', 'Footstools']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Study Room': ######

        root_cat = ['Desks', 'Bookcases', 'Office Chairs']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])


    
    if sub == 'Home Bar': ######

        root_cat = ['Bar Table', 'Bar Cabinets', 'Bar Stools', 'Serving Trolleys']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Kitchen & Dining': ######

        root_cat = ['Dining Table Sets', 'Dining Tables', 'Dining Chairs', 'Dining Bench', 'Kitchen Cabinets']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Outdoor Furniture': ######

        root_cat = ['Swing Chairs', 'Hammocks', 'Patio Umbrella', 'Outdoor Furniture Sets']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])