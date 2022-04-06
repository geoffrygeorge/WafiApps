import streamlit as st
import time


def home_decor_main():

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

    sub = col1.radio('Choose Sub Category :', ['Wall Decor', 'Home Decor', 'Kitchen Linen', 'Bathroom Linen', 'Bedroom Linen', 'Carpets & Rugs', 'Artworks', 'Curtains & Accessories'])



    if sub == 'Wall Decor': ######

        root_cat = ['Wall Decor & Hanging', 'Clocks', 'Stickers', 'Mirrors']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Home Decor': ######

        root_cat = ['Alarm Clocks', 'Cushion Covers', 'Home Fragrance']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Kitchen Linen': ######

        root_cat = ['Oven Gloves', 'Aprons', 'Table Cloths', 'Table Runners', 'Place Mats']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Bathroom Linen': ######

        root_cat = ['Towel Sets', 'Bath Robe', 'Hand Towels', 'Bath Towel', 'Bath Sheets', 'Face Towels', 'Beach Towels', 'Bath Mats & Rugs', 'Bath Slippers', 'Shower Curtains', 'Washcloths']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Bedroom Linen': ######

        root_cat = ['Bed Pillows', 'Kids Bedding', 'Pillow Cases', 'Sheets', 'Comforters', 'Duvets & Covers', 'Bedspreads', 'Blankets & Quilts', 'Mattress Toppers', 'Mattress & Pillow Protectors', 'Throws']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])

    

    if sub == 'Carpets & Rugs': ######

        root_cat = ['Carpets', 'Rugs', 'Door Mats']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])


    
    if sub == 'Artworks': ######

        root_cat = ['Canvas & Framed Paintings', 'Paintings', 'Wall Stickers', 'Posters & Prints']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Curtains & Accessories': ######

        root_cat = ['Curtains', 'Blinds', 'Valances', 'Tiers', 'Swags', 'Accessories']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])