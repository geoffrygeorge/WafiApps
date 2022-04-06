import streamlit as st
import time


def baby_care_main():

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

    sub = col1.radio('Choose Sub Category :', ['Infant Milk & Food', 'Bottle Feeding', 'Baby Medical & Health Care', 'Bathing', 'Weaning & Toddler Feeding', 'Diapering', 'Baby Oral Care', 'Wipes & Accessories', 'Baby Skin Care', 'Bips Pacifiers & Teethers', 'Breast Feed', 'Baby Grooming', 'Travel Gear & High Chairs', 'Safety Equipment'])



    if sub == 'Infant Milk & Food': ######

        root_cat = ['Infant Milk', 'Baby Fruits & Vegetables', 'Baby Cereals', 'Baby Snacks']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Bottle Feeding': ######

        root_cat = ['Bottles', 'Bottle Nipples', 'Cleaning Accessories']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Baby Medical & Health Care': ######

        root_cat = ['Baby Thermometer']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Bathing': ######

        root_cat = ['Baby Soaps & Cleansers', 'Baby Body Wash', 'Baby Shampoo']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Weaning & Toddler Feeding': ######

        root_cat = ['Forks Knives & Spoons']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Diapering': ######

        root_cat = ['Size 5 (11 to 25kg)', 'Size 6 (16kg +)']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Baby Oral Care': ######

        root_cat = ['Baby Toothbrushes']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Wipes & Accessories': ######

        root_cat = ['Wet Wipes', 'Wipes & Refills']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Baby Skin Care': ######

        root_cat = ['Baby Rash Cream', 'Baby Powder', 'Baby Lotion & Cream', 'Baby Hair Oils', 'Baby Massage Oils', 'Baby Sunscreen']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Bips Pacifiers & Teethers': ######

        root_cat = ['Teethers', 'Pacifiers', 'Bips & Burp Towels']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Breast Feed': ######

        root_cat = ['Breast Pumps', 'Breast Pads', 'Breast Care', 'Breast Milk Containers', 'Nursing Pillows & Covers']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Baby Grooming': ######

        root_cat = ['Baby Hair Brush & Comb', 'Baby Nail Clippers', 'Baby Scissors']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Travel Gear & High Chairs': ######

        root_cat = ['Baby Carriers', 'High Chairs & Booster Seat', 'Car Seat & Accessories', 'Strollers Prams & Accessories']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Safety Equipment': ######

        root_cat = ['Baby Monitors']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])