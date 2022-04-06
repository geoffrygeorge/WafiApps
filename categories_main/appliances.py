import streamlit as st
import time


def appliances_main():

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

    sub = col1.radio('Choose Sub Category :', ['Kitchen Appliances', 'Home Appliances', 'Washing Machines & Dryers', 'Cooktops & Ranges', 'Refrigerators & Freezers', 'Microwave Ovens', 'Air Conditioners', 'Heating Cooling & Air Quality'])



    if sub == 'Kitchen Appliances': ######

        root_cat = ['Coffee Machines & Grinders', 'Hand Blenders & Mixers', 'Electric Kettles', 'Fryers', 'Juicers', 'Rice Cookers', 'Food Processors', 'Toasters', 'Oven & Toaster Grills', 'Mixer Grinders', 'Induction Cooktops', 'Snack Maker', 'Sandwich Makers', 'Bread Maker', 'Electric Steamers', 'Microwave Ovens', 'Meat Grinders & Mincers', 'Choppers & Chippers', 'Milk Frothers', 'Waffle & Dessert Makers', 'Wet Grinders']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Home Appliances': ######

        root_cat = ['Irons & Steamers', 'Vacuum Cleaners', 'Water Dispensers & Purifiers', 'Dishwashers', 'Sewing Machine & Accessories', 'Inverters']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Washing Machines & Dryers': ######

        root_cat = ['Dryers', 'Fully Automatic Front Load', 'Semi Automatic Top Load', 'Fully Automatic Top Load']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Cooktops & Ranges': ######

        root_cat = ['Cooking Range', 'Cooktop', 'Cooker Hood']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Refrigerators & Freezers': ######

        root_cat = ['Single Door', 'Chest Freezer & Chiller', 'Double Door', 'Side by Side', 'Triple Door']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Microwave Ovens': ######

        root_cat = ['Solo', 'Grill', 'Convection']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Air Conditioners': ######

        root_cat = ['Split ACs', 'Window ACs']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Heating Cooling & Air Quality': ######

        root_cat = ['Air Purifiers', 'Fans', 'Humidifiers', 'Air Coolers', 'Heaters', 'Water Heater']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])