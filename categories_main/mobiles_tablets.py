import streamlit as st
import time


def mobiles_tablets_main():

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

    sub = col1.radio('Choose Sub Category :', ['Mobile Accessories', 'Mobile Phones', 'Tablets & iPad'])



    if sub == 'Mobile Accessories': ######

        root_cat = ['Mobile Cables', 'Mobile Chargers', 'Mobile Cases & Covers', 'Power Banks', 'Mobile Holders', 'Mobile Screen Protectors', 'SD Cards', 'Selfie Stick', 'Bluetooth Devices & Headsets']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Mobile Phones': ######

        root_cat = ['Nokia', 'Samsung', 'Huawei', 'iPhone', 'OnePlus', 'Xiaomi', 'Vivo', 'Alcatel', 'Ravoz', 'Oppo', 'Realme']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Tablets & iPad': ######

        root_cat = ['iPad', 'Samsung', 'Huawei', 'Alcatel', 'Lenovo']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])