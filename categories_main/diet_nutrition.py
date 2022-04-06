import streamlit as st
import time


def diet_nutrition_main():

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

    sub = col1.radio('Choose Sub Category :', ['Vitamins & Supplements', 'Protein', 'Weight Management', 'Herbs & Natural Solutions', 'Performance', 'Digestion', 'Super Foods & Green Foods'])



    if sub == 'Vitamins & Supplements': ######

        root_cat = ['Multivitamins', 'Vitamins A-Z', 'Fish Oil & Omegas', 'Nutritional Supplements', 'Specialty Supplements', 'Antioxidants', 'Joint Support', 'Wellness Essentials', 'Minerals', 'Blended Vitamin & Mineral Supplements']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Protein': ######

        root_cat = ['Protein Drinks', 'Meal Replacements', 'Whey Protein', 'Mass Gainers', 'Protein Bars', 'Protein Blends', 'Casein Proteins', 'Plant Based Protein']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Weight Management': ######

        root_cat = ['Fat Burners & Thermogenics', 'Meal Replacements', 'Appetite Control & Diet Support', 'Ketogenic Friendly']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Herbs & Natural Solutions': ######

        root_cat = ['Natural Solutions', 'Herbs A-E', 'Herbs F-N', 'Herbs O-S', 'Herbs T-Z']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Performance': ######

        root_cat = ['Pre-Workout Supplements', 'Energy & Endurance', 'Muscle Builders', 'Performance Supplements']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Digestion': ######

        root_cat = ['Digestive Support', 'Cleansing & Detox']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Super Foods & Green Foods': ######

        root_cat = ['Super Foods', 'Green Foods']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])