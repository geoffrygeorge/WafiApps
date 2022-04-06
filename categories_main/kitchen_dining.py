import streamlit as st
import time


def kitchen_dining_main():

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

    sub = col1.radio('Choose Sub Category :', ['Cookware', 'Kitchen Tools', 'Serveware', 'Bakeware', 'Kitchen Storage & Containers', 'Dinner Sets'])



    if sub == 'Cookware': ######

        root_cat = ['Frying Pans & Saucepans', 'Cookpots & Casseroles', 'Cookware Sets', 'Pressure Cookers', 'Kadhais & Woks', 'Tawas', 'Cooking Spoons', 'Tadka Pans']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Kitchen Tools': ######

        root_cat = ['Knives', 'Utensils & Gadgets', 'Measures & Scales', 'Choppers & Chippers', 'Graters & Slicers', 'Kichen Ladels']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Serveware': ######

        root_cat = ['Hotpots', 'Cups & Mugs', 'Serving Bowls', 'Cutlery', 'Serving Trays', 'Glassware & Drinkware', 'Cookpots & Casseroles']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Bakeware': ######

        root_cat = ['Baking Tools', 'Cake & Muffin Moulds', 'Mixing Bowls', 'Decorative Tools', 'Cookie Cutters']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Kitchen Storage & Containers': ######

        root_cat = ['Water Bottles & Flasks', 'Jars & Containers', 'Food Savers', 'Countertop & Wall Organization', 'Lunch Boxes & Bags', 'Cooler', 'Trash & Recycling']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])   



    if sub == 'Dinner Sets': ######

        root_cat = ['Opalware & Glass', 'Plates', 'Bone China & Porcelain', 'Melamine', 'Metalware']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])