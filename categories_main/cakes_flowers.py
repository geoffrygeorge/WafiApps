import streamlit as st
import time


def cakes_flowers_main():

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

    sub = col1.radio('Choose Sub Category :', ['Fresh Flower Arrangement', 'Cakes', 'Flowers', 'Combos', 'Plants'])



    if sub == 'Fresh Flower Arrangement': ######

        root_cat = ['Flower Bouquet', 'Vase Arrangement', 'Flowers in Sleeve', 'Flowers in Box', 'Valentine Boquets']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Cakes': ######

        root_cat = ['Cup Cakes', 'Frosting Cakes', 'Any Occassion', 'Cake Slices', 'Cake Shake', 'Designer Cakes', 'Donut', 'Heart Shaped Cakes', 'Cartoon Cakes', 'Eggless Cakes', 'Photo Cakes', 'Dry Cakes', 'Cake in Jar']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Flowers': ######

        root_cat = ['Roses', 'Orchids', 'Lillies', 'Carnations', 'Anthuriums']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Combos': ######

        root_cat = ['Flowers & Chocolate', 'Cake with Flowers', 'Cake with Chocolates', 'Flowers & Teddy', 'Flowers & Sweets', 'Flowers & Dry Fruits']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Plants': ######

        root_cat = ['Flowering Plants', 'Air Purifying Plants', 'Lucky Bamboo', 'Money Plants', 'Premium Plants']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])