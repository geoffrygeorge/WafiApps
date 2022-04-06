import streamlit as st
import time


def petsupplies_main():

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
    
    sub = col1.radio('Choose Sub Category :', ['Cat Food', 'Cat Care & Accessories', 'Dog Care & Accessories', 'Dog Food', 'Fish Food & Accessories'])



    if sub == 'Cat Food': ######

        root_cat = ['Dry Cat Food Adult', 'Wet Cat Food', 'Dry Food Kitten', 'Cat Treats']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Cat Care & Accessories': ######

        root_cat = ['Cat Grooming Supplies', 'Cat Litter & Accessories', 'Cat Vitamins & Supplements', 'Cat Scratcher & Furniture', 'Cat Toys', 'Cat Microchips', 'Cat Odor Removers & Cleaning', 'Cat Collar Leashes & Harness', 'Cat Parasites Control', 'Cat Feeding Accessories & Bowls', 'Cat Carriers & Crates', 'Cat Beds', 'Cat Travel Essentials']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Dog Care & Accessories': ######

        root_cat = ['Dog Feeding Accessories & Bowls', 'Dog Litter Accessories', 'Dog Odor Removers & Cleaning', 'Dog Toys', 'Dog Microchips', 'Dog Collar Leashes & Harness', 'Dog Carriers & Crates', 'Dog Beds', 'Dog Vitamins & Supplies', 'Dog Grooming Supplies', 'Dog Parasites Control', 'Dog Travel Essentials']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Dog Food': ######

        root_cat = ['Dog Treats & Chews', 'Wet Dog Food', 'Dry Food Puppy', 'Dry Food Adult']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Fish Food & Accessories': ######

        root_cat = ['Fish Food', 'Fish Tanks', 'Fish Pumps & Filter', 'Decors & Accessories', 'Equipments', 'Conditioner & Additives']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])