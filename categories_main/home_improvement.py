import streamlit as st
import time


def home_improvement_main():

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

    sub = col1.radio('Choose Sub Category :', ['Functional Lighting', 'Electricals', 'Safes & Security', 'Fixtures', 'Bathroom & Kitchen Fixtures', 'Door Locks & Hardware', 'Patio Lawn & Garden'])



    if sub == 'Functional Lighting': ######

        root_cat = ['Desk Lights & Lamps']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Electricals': ######

        root_cat = ['Cables']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Safes & Security': ######

        root_cat = ['Video Door Phones']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Fixtures': ######

        root_cat = ['Ceiling Lights & Fans', 'Chandeliers', 'Office Ceiling Lights', 'Bathroom Lights', 'Picture & Display Lights', 'Track Rail & Cable Lighting Systems']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Bathroom & Kitchen Fixtures': ######

        root_cat = ['Shower Heads', 'Health Faucets', 'Bathroom Basin Taps', 'Shower & Bath Taps', 'Bathroom Hardware', 'Kitchen Fixtures']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Door Locks & Hardware': ######

        root_cat = ['Hooks', 'Door Locks', 'Door Hardware', 'Cabinet Hardware', 'Furniture Hardware', 'Ladders', 'Painting Supplies & Wall Treatments', 'Building Supplies']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Patio Lawn & Garden': ######

        root_cat = ['Outdoor Lighting', 'Gardening & Lawn Care', 'Farm & Ranch', 'Pest Control']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])